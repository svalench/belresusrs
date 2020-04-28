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
    path('addautoPOST/',addAutoView, name='addautoPOST'),
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
]
