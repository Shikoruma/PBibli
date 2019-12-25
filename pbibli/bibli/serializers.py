from collections import OrderedDict
from django.contrib.auth.models import User, Group
from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model

from .models import Book 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
