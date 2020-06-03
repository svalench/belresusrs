import json
from datetime import datetime

import numpy
from django.http import HttpResponse
from django.shortcuts import render

from apps.ves.models import *


def showProduction(request):
    production = Production.objects.all()
    agent = Agent.objects.all()
    data = {'production':production,'agent':agent}
    return render(request, 'newData/catalog_production.html', data)


def AddProduction(request):
    form = request.POST
    production = Production(characteristicTMC=form['characteristicTmc'], number=form['nameInvoice'], name=form['name'], score = form['account'],
                         typeTMC=form['typeTmc'],scoreTMC=form['accountTmc'], typeOfAccountTMC = form['typeAccountingTmc'])
    production.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')


def UpdProduction(request):
    form = request.POST
    production = Production.objects.filter(id=form['id'])
    production.update(characteristicTMC=form['characteristicTmc'], number=form['nameInvoice'], name=form['name'], score = form['account'],
                         typeTMC=form['typeTmc'],scoreTMC=form['accountTmc'], typeOfAccountTMC = form['typeAccountingTmc'])
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')


def deleteProduction(request):
    form = request.POST
    trailer = CatalogTrailer.objects.filter(id=form['id'])
    trailer.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')
