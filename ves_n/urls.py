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
from django.urls import path, include

from apps.ves.add_in_db import addAutoNew, addVagonNew
from apps.ves.contract import showContract, AddContract, UpdContract, deleteContract
from apps.ves.production import showProduction, AddProduction, UpdProduction, deleteProduction
from apps.ves.responseblePerson import showPerson, AddPerson, UpdPerson, deletePerson
from apps.ves.trailer import showTrailer, UpdTrailer, AddTrailer, deleteTrailer
from ves_n.views import *

from channels.routing import ProtocolTypeRouter
from django.views.defaults import server_error, page_not_found, permission_denied
application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
})

urlpatterns = [
    path('', include('apps.ves.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout', logout_view, name = 'logout'),
    path('addaction/',addactionView, name='addaction'),

    path('addvagonPOST/',addVagonPost, name='addVagonPOST'),
    path('addcontragentPOST/',addContragentView, name='addcontragentPOST'),
    path('updcontragentPOST/',updContragentView, name='updcontragentPOST'),
    path('getDataAuto/', GetDataAuto, name='getDataAuto'),
    path('getDataZd/', GetDataZd, name='getDataZd'),
    path('getDataStatus/', GetDataStatus, name='getDataStatus'),
    path('getDataZd/getzdnumbler', GetZdNumber, name='getZdNumber'),
    path('getDataZd/getzdagent', GetZdAgent, name='getZdAgent'),
    path('getDataZd/getzddate', GetZdDate, name='getZdDate'),

    path('getDataAuto/getautonumbler', GetAutoNumber, name='getAutoNumber'),
    path('getDataAuto/getautoagent', GetAutoAgent, name='getAutoAgent'),
    path('getDataAuto/getautodate', GetAutoDate, name='getAutoDate'),

    path('onoff/svet1/',onOffS1,name='on1'),
    path('onoff/zd/svet1/',onOffZd,name='onoffzd'),
    path('add/auto/new',addAutoNew,name='newAddAuto'),
    path('add/train/new',addVagonNew,name='newAddVagon'),

    #данные бд контрагент
    path('data/catalogContract',showContract,name='catalogcontract'),
    path('data/catalogContractAdd',AddContract,name='catalogcontractAdd'),
    path('data/catalogContractUpd',UpdContract,name='catalogcontractUpd'),
    path('data/catalogContractDel', deleteContract, name='catalogcontractDel'),

    # прицепы
    path('data/trailerShow',showTrailer,name='trailerShow'),
    path('data/trailerAdd',AddTrailer,name='trailerAdd'),
    path('data/trailerUpd',UpdTrailer,name='trailerUpd'),
    path('data/trailerDel', deleteTrailer, name='trailerDel'),
    # дукция
    path('data/productionShow', showProduction, name='productionShow'),
    path('data/productionAdd', AddProduction, name='productionAdd'),
    path('data/productionUpd', UpdProduction, name='productionUpd'),
    path('data/productionDel', deleteProduction, name='productionDel'),
    # отвественные лица
    path('data/personShow', showPerson, name='personShow'),
    path('data/personAdd', AddPerson, name='personAdd'),
    path('data/personUpd', UpdPerson, name='personnUpd'),
    path('data/personDel', deletePerson, name='personDel'),

    #отчеты
    path('reportAutoAgent/get', reportAutoAgent, name='reportAutoAgent'),

    path('search/', serchAuto, name='search'),
]
