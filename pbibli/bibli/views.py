from django.shortcuts import render
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import filters
import requests, re
from xml.etree import ElementTree

from .serializers import BookSerializer, LoanSerializer, PersonSerializer, AddBookSerializer

from .models import Book, Loan, Person
# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'author')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    @action(methods=['post'], detail=False, serializer_class=AddBookSerializer)
    def find_book(self, request):
        """
        """
        serializer = AddBookSerializer(data=request.data)
        if serializer.is_valid():
            r = requests.get('http://www.sudoc.fr/services/isbn2ppn/'+serializer.data['isbn'])
            tree = ElementTree.fromstring(r.content)
            ppn=tree[0][1][0].text
            r = requests.get('http://www.sudoc.fr/'+ppn+'.xml')
            tree = ElementTree.fromstring(r.content)
            bo = {}
            bo['isbn']=serializer.data['isbn']
            bo['title']=tree.findtext("./datafield[@tag='200']/subfield[@code='a']")
            bo['author']=tree.findtext("./datafield[@tag='200']/subfield[@code='f']")
            bo['serie_title']=tree.findtext("./datafield[@tag='461']/subfield[@code='t']")
            bo['num_volume']=tree.findtext("./datafield[@tag='461']/subfield[@code='v']")
            if(bo['serie_title'] is None):
                bo['serie_title']=tree.findtext("./datafield[@tag='517']/subfield[@code='a']")
                bo['num_volume']=tree.findtext("./datafield[@tag='517']/subfield[last()]")
            if(bo['serie_title'] is None):
                bo['serie_title']=tree.findtext("./datafield[@tag='454']/subfield[@code='t']")
                bo['num_volume']=tree.findtext("./datafield[@tag='454']/subfield[last()]")

            if bo['num_volume'] is None:
                bo['num_volume']=1
            elif not bo['num_volume'].isdigit():
                digits = re.findall(r'(\d+)',bo['num_volume'])
                if len(digits) > 0:
                    bo['num_volume']=digits[0]
            bo['demat']=False
            boser=BookSerializer(data=bo)
            if boser.is_valid():
                return Response(boser.data, status=status.HTTP_200_OK)
            else:
                return Response(boser.errors,
                        status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated,)

class LoanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = (IsAuthenticated,)
