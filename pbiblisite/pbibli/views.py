from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import viewsets, mixins, status, generics, serializers
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import filters
import requests, re
from xml.etree import ElementTree

from .serializers import PasswordSerializer, UserSerializer, UserPublicSerializer, BookSerializer, LoanSerializer, AddBookSerializer

from .models import Book, Loan
from .permissions import IsOwnerOrReadOnly, LoanPermission, IsAdminOrIsSelf


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email')

    def get_serializer_class(self):
        """
        Non admin user cannot see private user attribute for privacy reason
        """
        if self.action == "list":
            return UserPublicSerializer
        else:
            return UserSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'retrieve', 'set_password']:
            permission_classes = [IsAdminOrIsSelf, IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(methods=['put'], detail=True, serializer_class=PasswordSerializer)
    def set_password(self, request, pk):
        """
        Special endpoint to change password
        """
        serializer = PasswordSerializer(data=request.data)
        user = get_user_model().objects.get(pk=pk)
        # only an admin or the own user can change the password
        if request.user.is_staff or user == request.user:
            if serializer.is_valid():
                if not user.check_password(serializer.data.get('old_password')):
                    return Response({'old_password': ['Wrong password.']},
                                    status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request,user)
                return Response({'status': 'password set'}, status=status.HTTP_200_OK)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

class SelfView(APIView):
    """
    Endpoint to see personals informations/profile
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        instance = UserSerializer(request.user, context={'request': request})
        return Response({"user": instance.data})

class AllBooksView(mixins.ListModelMixin,
                generics.GenericAPIView):
    """
    Endpoint to see book of all people
    """
    queryset = Book.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'author')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'author')
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)

    def get_queryset(self):
        return self.queryset.filter(owner = self.request.user)

    def perform_create(self, serializer):
        try:
            Book.objects.get(owner=self.request.user, isbn=serializer.validated_data['isbn'])
            raise serializers.ValidationError({'non_field_error':'Vous possèdez déjà un livre avec cet isbn'})
        except Book.DoesNotExist:
            serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        try:
            book = Book.objects.get(owner=self.request.user, isbn=serializer.validated_data['isbn'])
            if(book.id != serializer.instance.id):
                raise serializers.ValidationError({'non_field_error':'Vous possèdez déjà un livre avec cet isbn'})
        except Book.DoesNotExist:
            pass
        serializer.save(owner=self.request.user)
    
    @action(methods=['post'], detail=False, serializer_class=AddBookSerializer)
    def find_book(self, request):
        """
        """
        serializer = AddBookSerializer(data=request.data)
        if serializer.is_valid():
            r = requests.get('http://www.sudoc.fr/services/isbn2ppn/'+serializer.data['isbn'])
            tree = ElementTree.fromstring(r.content)
            ppn=tree.findtext("./query/*[last()]/ppn")
            if ppn is not None:
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
                    else:
                        bo['serie_title']=None
                        bo['num_volume']=1
                bo['demat']=False
                bo['owner']=request.user.id
                boser=BookSerializer(data=bo)
                if boser.is_valid():
                    return Response(boser.data, status=status.HTTP_200_OK)
                else:
                    return Response(boser.errors,
                            status=status.HTTP_400_BAD_REQUEST)
            else: 
                return Response({'error': 'Aucune notice n\'est associée a cet isbn.'},
                        status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

class LoanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = (IsAuthenticated,LoanPermission)

    def get_queryset(self):
        if(self.request.user.is_staff):
            return self.queryset.all()
        return self.queryset.filter(Q(borrower=self.request.user) | Q(book__owner = self.request.user)).distinct()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if(request.user != serializer.validated_data['book'].owner):
            raise PermissionDenied("Vous ne pouvez pas prêtez un livre qui ne vous appartient pas")
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if(request.user != serializer.validated_data['book'].owner):
            raise PermissionDenied("Vous ne pouvez pas prêtez un livre qui ne vous appartient pas")
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
