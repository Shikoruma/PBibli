"""pbibli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse_lazy, include, re_path
from django.views.generic.base import RedirectView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.http import HttpResponse

from django.views.generic.base import TemplateView

def adminTest(request):
    if not request.user.is_anonymous and request.user.is_staff:
        return HttpResponse('Ok', status=200)
    else:
        return HttpResponse('KO', status=403)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bibli.urls')),
    path('api/auth/', adminTest),

    re_path(r'^api/auth/obtain_token/', obtain_jwt_token),
    re_path(r'^api/auth/refresh_token/', refresh_jwt_token),
    re_path('^$', TemplateView.as_view(template_name="index.html"))
]