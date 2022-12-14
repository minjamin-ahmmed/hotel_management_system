"""pythonproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from home import views

import home.views
import django.contrib.auth.views as auth_views

from home.forms import Login_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home_view,name='home'),
    path('about/', home.views.about,name='about'),
    path('contacts/', home.views.contacts,name='contacts'),
    path('gallery/', home.views.gallery,name='gallery'),
    path('meetingandevents/', home.views.meetingandevents,name='meetingandevents'),
    path('recreation/', home.views.recreation,name='recreation'),
    path('restaurant/', home.views.restaurant,name='restaurant'),
    path('accomodation/', home.views.accomodation,name='accomodation'),
    path('view/', home.views.view,name='view'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('login/', auth_views.LoginView.as_view(template_name='Login_Page.html',authentication_form=Login_form), name = 'login'),

    path('logout/', auth_views.LogoutView.as_view(template_name ='Logout_Page.html '), name = 'logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html')),
    path('change_password_done/', auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'), name='password_change_done'),



]



