"""
URL configuration for keyword_monitor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from main.views import *
from users.views import *
from keywords.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView.as_view(), name='index'),
    path('about/', aboutView.as_view(), name='about'),
    path('contact/', contactView.as_view(), name='contact'),
    path('signup/', signUpView.as_view(), name='signup'),
    path('signin/', signInView.as_view(), name='signin'),
    path('signout/',signOutView.as_view(), name='signout')
]
