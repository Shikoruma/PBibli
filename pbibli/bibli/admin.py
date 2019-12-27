from django.contrib import admin
from .models import  Book, Person, Loan

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
        pass

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
        pass

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
        pass
