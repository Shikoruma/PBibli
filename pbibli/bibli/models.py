from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Book(models.Model):
    """
    Type of organization (Labo,School, ...)
    """
    isbn = models.CharField(max_length=20)
    serie_title = models.CharField(max_length=30,null=True, blank=True)
    title = models.CharField(max_length=30)
    num_volume = models.IntegerField(default=1)
    author = models.CharField(max_length=30)
    localisation = models.CharField(max_length=20,null=True, blank=True)
    demat = models.BooleanField()
    abstract = models.CharField(max_length=200,null=True, blank=True)
    

    def __str__(self):
        return self.title

