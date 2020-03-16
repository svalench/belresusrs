import abc

import json
import threading
from abc import ABCMeta

from datetime import datetime
from django.contrib.auth import logout
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import redirect, render

from apps.ves.models import ActionUser, Auto, Agent


def logout_view(request):
    logout(request)
    return redirect('login')

def addactionView(request, *args, **kwargs):
    form = request.POST
    print(form)
    model = ActionUser(where=form['where'], action=form['action'], parentId=User(form['user']))
    model.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')

def addAutoView(request):
    form = request.POST
    print(form)
    last_in = datetime.now()
    auto = Auto(number=form['numAuto'], number_pricep=form['numPricep'], last_in=last_in, ves_in=form['ves'], status_in=True)
    auto.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')

def addContragentView(request):
    form = request.POST
    now = datetime.now()
    cities = {
        'gorod': 'г.',
        'gp': "гп.",
        'derev': "поселок"
    }
    streets = {
        'prospect': "проспект",
        'bulvar': "бульвар",
        'street': "улица",
        'per': "переулок",
        'proezd': 'проезд'
    }
    address = form['city'] +" "+ cities[form['typeCity']] + ", " + streets[form['typeStreet']] + " " + form['street'] + ", " + form['numHouse']
    agent = Agent(name=form['name'],unp=form["unp"], description=form['description'], address=address)
    agent.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')