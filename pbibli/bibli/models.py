from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Book(models.Model):
    """
    Book
    """
    isbn = models.CharField(max_length=20, unique=True)
    serie_title = models.CharField(max_length=30,null=True, blank=True)
    title = models.CharField(max_length=30)
    num_volume = models.IntegerField(default=1)
    author = models.CharField(max_length=30)
    localisation = models.CharField(max_length=20,null=True, blank=True)
    demat = models.BooleanField()
    abstract = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.title

class Person(models.Model):
    """
    Person who loan a book
    """
    nickname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=30)

    def __str__(self):
        return self.nickname

class Loan(models.Model):
    """
    Loan
    """
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField()
    due_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return str(self.person)+" "+str(self.book)
