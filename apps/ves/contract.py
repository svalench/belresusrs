import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from apps.ves.models import *


def showContract(request):
    contract = CatalogContract.objects.all()
    agent = Agent.objects.all()
    tmc= Production.objects.all()
    data = {'contract':contract,'agent':agent,'tmc':tmc}
    return render(request, 'newData/catalog_contract.html', data)


def AddContract(request):
    form = request.POST
    contract = CatalogContract(name=form['name'], parentContragentId_id=form['agent'],parentMaterialId_id=form['tmc'],date=form['dateDogovor'],
                               typeOfOperation=form['typeOperation'],typeOfArrival=form['viewComing'],salesAccount=form['salesAccount'])
    contract.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')


def UpdContract(request):
    form = request.POST
    contract = CatalogContract.objects.filter(id=form['id'])
    contract.update(name=form['name'], parentContragentId_id=form['agent'],parentMaterialId_id=form['tmc'],date=form['dateDogovor'],
                               typeOfOperation=form['typeOperation'],typeOfArrival=form['viewComing'],salesAccount=form['salesAccount'])
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')


def deleteContract(request):
    form = request.POST
    contract = CatalogContract.objects.filter(id=form['id'])
    contract.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')
