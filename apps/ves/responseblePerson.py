import json
from datetime import datetime

import numpy
from django.http import HttpResponse
from django.shortcuts import render

from apps.ves.models import *


def showPerson(request):
    person = CatalogResponsiblePerson.objects.all()
    agent = Agent.objects.all()
    data = {'person':person,'agent':agent}
    return render(request, 'newData/responciblePerson.html', data)


def AddPerson(request):
    form = request.POST
    person = CatalogResponsiblePerson(first_name=form['first_name'], second_name=form['second_name'], last_name=form['last_name'],
                         role=form['role'])
    person.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')


def UpdPerson(request):
    form = request.POST
    person = CatalogResponsiblePerson.objects.filter(id=form['id'])
    person.update(first_name=form['first_name'], second_name=form['second_name'], last_name=form['last_name'],
                         role=form['role'])
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')


def deletePerson(request):
    form = request.POST
    trailer = CatalogTrailer.objects.filter(id=form['id'])
    trailer.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')
