from django.urls import path, include
from .views import BookViewSet, PersonViewSet, LoanViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'loans', LoanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
