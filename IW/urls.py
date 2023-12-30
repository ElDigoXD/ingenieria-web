"""
URL configuration for IW project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

from IW.views.login import login_form

from .views import *

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', index, name="home"),
    path('contact', contact, name="contact"),
    path('contact-form', contact_form, name="contact-form"),
    path('about', about, name="about"),
    path('login', login, name="login"),
    path('login-form', login_form, name="login-form"),
    path('logout', lambda x: redirect("home") if logout(x) else redirect("home") , name="logout"),  # type: ignore
)
