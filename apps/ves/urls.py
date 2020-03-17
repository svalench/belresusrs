"""ves_n URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from apps.ves.views import StartView, DataView

app_name = 'ves'
urlpatterns = [
    path('',  StartView.as_view(), name = 'start'),
    path('ves',  StartView.menu_ves, name = 'menu_ves'),
    path('ves/avto',  StartView.avto_ves, name = 'avto_ves'),
    path('ves/zd',  StartView.zd_ves, name = 'zd_ves'),
    # path('<str:room_name>/', views.room, name='room'),

    path('data',  DataView.menu_data, name = 'menu_data'),
    path('data/contragents',  DataView.AgentView, name = 'contragents'),
    path('data/actions',  DataView.ActionView, name = 'actions'),


]
