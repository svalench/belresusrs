
# класс для просмотра данных
import json
from datetime import datetime

from aioredis.commands import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib import messages
from apps.ves.forms import UserForm, UpdUserForm
from apps.ves.models import *
from ves_n.setting_data import USER_ROLES_SETTINGS


def addAutoNew(request):
    form = request.POST
    form._mutable = True
    print(form)
    for key in form.keys():
        if(form[key]==''):
            form[key]=None
    last_in = datetime.now()
    in_ter = Auto.objects.filter(number=form['gos_num_avto'], status_in=True)
    if in_ter.exists():
        in_ter[0].last_out=last_in
        in_ter[0].weghtOut=form['ves']
        in_ter[0].status_in=False
        in_ter.update(last_out=last_in,weghtOut=form['ves'],status_in=False,netto=abs(in_ter[0].weghtIn-int(form['ves'])))
    else:
        if(not 'WeightInvoice' in form):
            form['WeightInvoice']=None
        if (not 'DirtPercent' in form):
            form['DirtPercent'] = None
        if (not 'DateInvoice' in form):
            form['DateInvoice'] = None
        if (not 'Contragent' in form):
            form['Contragent'] = None
        if (not 'Contract' in form):
            form['Contract'] = None
        if (not 'SeriesInvoice' in form):
            form['SeriesInvoice'] = None
        if (not 'NumberInvoice' in form):
            form['NumberInvoice'] = None
        if (not 'DateInvoice' in form):
            form['DateInvoice'] = None
        if (not 'ContractPrice' in form):
            form['ContractPrice'] = None
        auto = Auto(number=form['gos_num_avto'], agents_id=form['Contragent'], driver=form['NameDriver'], parentContractId_id=form['Contract'],
                    number_pricep=form['gos_num_pricep'],  last_in=last_in, catalog_id=form['DataAuto'], catalogPricep=form['DataTrailer'],
                    description= form['Description'], seria=form['SeriesInvoice'],numberNakladnaia=form['NumberInvoice'], nakladnayaDate = form['DateInvoice'],
                    ves_nakladnaya=form['WeightInvoice'], price_ed_iz=form['ContractPrice'], discont= form['DirtPercent'],
                     weghtIn=float(form['ves']),
                status_in=True)
        auto.save()
    allIn = Auto.objects.filter( status_in=True)
    allIn = serializers.serialize('json', allIn)
    payload = {'success': True,'autoIn':allIn}

    return HttpResponse(json.dumps(payload), content_type='application/json')