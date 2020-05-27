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
import asyncio
from apps.ves.catalog import CatalogAutoView, CatalogTrailerView, CatalogProductView
from apps.ves.views import StartView, DataView

app_name = 'ves'
urlpatterns = [
    path('',  StartView.as_view(), name = 'start'),
    path('ves',  StartView.menu_ves, name = 'menu_ves'),
    path('ves/avto',  StartView.avto_ves, name = 'avto_ves'),
    path('ves/avtodata',  StartView.avto_data, name = 'avto_data'),
    path('ves/zd',  StartView.zd_ves, name = 'zd_ves'),
    path('ves/zddata',  StartView.zd_data, name = 'zd_data'),
    # path('<str:room_name>/', views.room, name='room'),

    path('data',  DataView.menu_data, name = 'menu_data'),
    path('data/contragents',  DataView.AgentView, name = 'contragents'),
    path('data/actions',  DataView.ActionView, name = 'actions'),
    path('ves/users', DataView.UserView, name='users'),
    path('ves/users/<int:usid>/', DataView.updateUserView, name='usersUpd'),

    #catalog views
    path('data/catalog/auto',CatalogAutoView.showAuto,name='catalogAuto'),
    path('data/catalog/auto/addAuto',CatalogAutoView.addAuto,name='catalogAutoAdd'),
    path('data/catalog/auto/updAuto',CatalogAutoView.addUpdate,name='catalogAutoUpd'),

    path('data/catalog/trailer',CatalogTrailerView.showTrailer,name='catalogTrailer'),
    path('data/catalog/trailer/addTrailer',CatalogTrailerView.addTrailer,name='catalogTrailerAdd'),
    path('data/catalog/trailer/updTrailer',CatalogTrailerView.addUpdate,name='catalogTrailerUpd'),

    path('data/catalog/production', CatalogProductView.sowCatalog, name='catalogProduction'),
    path('data/catalog/production/addProduction', CatalogProductView.addProduction, name='catalogProductionAdd'),
    path('data/catalog/production/updProduction', CatalogTrailerView.addUpdate, name='catalogProductionUpd'),


]




