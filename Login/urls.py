"""
URL configuration for Login project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from website import views

urlpatterns = [
    path('',views.Register),
    path('create_account/',views.create_account),
    path('login/',views.login),
    path('login_process/',views.login_process),
    path('list_Register/',views.list_Register),
    path('home/',views.home),
    path('edit_Organization/',views.edit_Organization),
    path('update_file/',views.update_file),
    path('admin/', admin.site.urls),
]
