import abc
import json
import threading
from abc import ABCMeta

from django.contrib.auth import logout
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import redirect, render

from apps.ves.models import ActionUser


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
