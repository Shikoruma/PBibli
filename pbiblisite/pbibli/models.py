from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

class Book(models.Model):
    """
    Book
    """
    isbn = models.CharField(max_length=20)
    serie_title = models.CharField(max_length=50,null=True, blank=True)
    title = models.CharField(max_length=50)
    num_volume = models.IntegerField(default=1,null=True, blank=True)
    author = models.CharField(max_length=40)
    localisation = models.CharField(max_length=30,null=True, blank=True)
    demat = models.BooleanField(default=False)
    abstract = models.CharField(max_length=200,null=True, blank=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='books')

    class Meta:
        unique_together = [['isbn', 'owner']]

    def __str__(self):
        prefix=""
        if(self.serie_title):
            prefix=self.serie_title+"("+str(self.num_volume)+"): "
        return prefix+self.title

class Loan(models.Model):
    """
    Loan
    """
    borrower = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE, related_name='myloans')
    borrowerext = models.CharField(max_length=30,null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans")
    checkout_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    def __str__(self):
        name = ""
        if(self.borrower):
            name=self.borrower.username
        else:
            name = self.borrowerext
        return str(self.book)+" "+name
