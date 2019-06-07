"""smalllibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from dechlib.views import home1, list_book, list_borrower, list_publisher, list_binding, logoutdech, dech_page

app_name = 'dechlib'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home1, name='home1'),
    path('dech_page/', dech_page, name='dech_page'),
    path('logout/', logoutdech, name='logoutdech'),
    path('listbook/', list_book, name='list_book'),
    path('borrower/', list_borrower, name='list_borrower'),
    path('publisher/', list_publisher, name='list_publisher'),
    path('binding/', list_binding, name='list_binding'),
]