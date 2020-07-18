from django.urls import path, include
from .views import BookViewSet, LoanViewSet, UserViewSet, SelfView, AllBooksView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('self/', SelfView.as_view()),
    path('allbooks/', AllBooksView.as_view()),
    path('', include(router.urls)),
]
