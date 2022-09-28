"""password_generator URL Configuration

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
from django.urls import path
from generator import views                                           # import from generator folder views.py file

urlpatterns = [
    path('', views.home, name='home'),                                # url address of our main page (code in views.py,
                                                                      # markup in home.html)
    path('generatedpassword', views.password, name='password'),       # url with the name of the password page
                                                                      # (code in views.py, markup in password.html)
    path('about', views.about, name='about')                          # url with the name of the about page
                                                                      # (code in views.py, markup in about.html)
]
