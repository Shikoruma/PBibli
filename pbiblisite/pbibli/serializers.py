from collections import OrderedDict
from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model

from .models import Book, Loan 


class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class of the User Model
    The class member person is a nested representation
    """

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email',
                  'first_name', 'last_name', 'is_staff')
        read_only_fields = ('username',)

class UserPublicSerializer(serializers.ModelSerializer):
    """
    Public Serializer class for User objects
    Only visible to manager and only show username first_name and last_name and email
    """
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name')
        read_only_fields = ('username', 'first_name', 'last_name')

class BookSerializer(serializers.ModelSerializer):
    
    prettytitle = serializers.SerializerMethodField()
    def get_prettytitle(self, obj):
        title=""
        if isinstance(obj, OrderedDict):
            if obj['serie_title']:
                title = obj['serie_title']+"("+str(obj['num_volume'])+"): "
            return title+obj['title']
        else:
            if obj.serie_title:
                title = obj.serie_title+"("+str(obj.num_volume)+"): "
            return title+obj.title

    class Meta:
        model = Book
        fields = '__all__'
        #exclude = ['owner']
        read_only_fields = ('prettytitle',)

class LoanSerializer(serializers.ModelSerializer):
    
    borrowername = serializers.SerializerMethodField()
    def get_borrowername(self, obj):
        name=""
        if isinstance(obj, OrderedDict):
            if obj['borrower']:
                name = obj['borrower'].username
            else:
                name = obj['borrowerext']
        else:
            if obj.borrower:
                name = obj.borrower.username
            else:
                name = obj.borrowerext
        return name
    class Meta:
        model = Loan
        fields = '__all__'
        read_only_fields = ('borrowername',)

class AddBookSerializer(serializers.Serializer):
    """
    Serializer for bulk add book
    """
    isbn = serializers.CharField(required=True)

