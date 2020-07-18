from django.contrib import admin
from .models import  Book, Loan

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
        pass

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
        pass
