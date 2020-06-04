
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
        if (not 'WeightInvoice' in form):
            form['WeightInvoice'] = None
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
        if (not 'UnitWeight' in form):
            form['UnitWeight'] = None
        if (not 'TypeArrival' in form):
            form['TypeArrival'] = None
        if (not 'NdsPercent' in form):
            form['NdsPercent'] = None
        if (not 'TypeInvoice' in form):
            form['TypeInvoice'] = None
        if (not 'TypeMaterialOut' in form):
            form['TypeMaterialOut'] = None
        if (not 'NumberWayList' in form):
            form['NumberWayList'] = None
        if (not 'NumberAccompanyingPassport' in form):
            form['NumberAccompanyingPassport'] = None
        #in_ter.update(last_out=last_in,weghtOut=form['ves'],status_in=False,netto=abs(in_ter[0].weghtIn-int(form['ves'])))
        in_ter.update(netto=abs(in_ter[0].weghtIn-int(form['ves'])), agents_id=form['Contragent'], driver=form['NameDriver'], parentcontractid_id=form['Contract'],
                    number_pricep=form['gos_num_pricep'],  last_out=last_in, catalog_id=form['DataAuto'], catalogpricep=form['DataTrailer'],
                    description= form['Description'], seria=form['SeriesInvoice'],numberNakladnaia=form['NumberInvoice'], nakladnayaDate = form['DateInvoice'],
                    ves_nakladnaya=form['WeightInvoice'], price_ed_iz=form['ContractPrice'], discont= form['DirtPercent'],
                     weghtOut=float(form['ves']), parentuserid_id=request.user.id,operatrion = form['operation'],
                    type=form['TypeInvoice'], nds=form['NdsPercent'], ves_ed= form['UnitWeight'], typeOperation= form['TypeArrival'],
                    typeMaterial= form['TypeMaterialOut'], numberPasport= form['NumberAccompanyingPassport'], numberPassportList = form['NumberWayList'],
                status_in=False)
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
        if (not 'UnitWeight' in form):
            form['UnitWeight'] = None
        if (not 'TypeArrival' in form):
            form['TypeArrival'] = None
        if (not 'NdsPercent' in form):
            form['NdsPercent'] = None
        if (not 'TypeInvoice' in form):
            form['TypeInvoice'] = None
        if (not 'TypeMaterialOut' in form):
            form['TypeMaterialOut'] = None
        if (not 'NumberWayList' in form):
            form['NumberWayList'] = None
        if (not 'NumberAccompanyingPassport' in form):
            form['NumberAccompanyingPassport'] = None
        auto = Auto(number=form['gos_num_avto'], agents_id=form['Contragent'], driver=form['NameDriver'], parentcontractid_id=form['Contract'],
                    number_pricep=form['gos_num_pricep'],  last_in=last_in, catalog_id=form['DataAuto'], catalogpricep=form['DataTrailer'],
                    description= form['Description'], seria=form['SeriesInvoice'],numberNakladnaia=form['NumberInvoice'], nakladnayaDate = form['DateInvoice'],
                    ves_nakladnaya=form['WeightInvoice'], price_ed_iz=form['ContractPrice'], discont= form['DirtPercent'],
                     weghtIn=float(form['ves']), parentuserid_id=request.user.id,operatrion = form['operation'],
                    type=form['TypeInvoice'], nds=form['NdsPercent'], ves_ed= form['UnitWeight'], typeOperation= form['TypeArrival'],
                    typeMaterial= form['TypeMaterialOut'], numberPasport= form['NumberAccompanyingPassport'], numberPassportList = form['NumberWayList'],
                status_in=True)
        auto.save()
    allIn = Auto.objects.filter( status_in=True)
    all= my_custom_sql()
    allIn = serializers.serialize('json', allIn)
    print("==================================================")
    print(all[0])
    payload = {'success': True,'autoIn':allIn,"all":all}

    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')



from django.db import connection

def my_custom_sql():
    with connection.cursor() as cursor:
        sql = "SELECT ag.name as nameAgent, c.name as contractName, c.id as contractId, c.*,ag.*,a.* FROM ves_auto a " \
              "LEFT JOIN ves_agent ag ON ag.id=a.agents_id" \
              " LEFT JOIN ves_catalogcontract c ON c.id=a.parentContractId_id  WHERE a.status_in=true"
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


def vagonSql():
    with connection.cursor() as cursor:
        sql = "SELECT ag.name as nameAgent, c.name as contractName, c.id as contractId, c.*,ag.*,a.* FROM ves_vagon a " \
              "LEFT JOIN ves_agent ag ON ag.id=a.agent_vagon_id" \
              " LEFT JOIN ves_catalogcontract c ON c.id=a.parentContractId_id  WHERE a.status_in=true"
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]






def addVagonNew(request):
    form = request.POST
    form._mutable = True
    print(form)
    for key in form.keys():
        if(form[key]==''):
            form[key]=None
    last_in = datetime.now()
    in_ter = Vagon.objects.filter(number=form['gos_num_avto'], status_in=True)
    if in_ter.exists():
        in_ter[0].last_out=last_in
        in_ter[0].weghtOut=form['ves']
        in_ter[0].status_in=False
        if (not 'WeightInvoice' in form):
            form['WeightInvoice'] = None
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
        if (not 'UnitWeight' in form):
            form['UnitWeight'] = None
        if (not 'TypeArrival' in form):
            form['TypeArrival'] = None
        if (not 'NdsPercent' in form):
            form['NdsPercent'] = None
        if (not 'TypeInvoice' in form):
            form['TypeInvoice'] = None
        if (not 'TypeMaterialOut' in form):
            form['TypeMaterialOut'] = None
        if (not 'NumberWayList' in form):
            form['NumberWayList'] = None
        if (not 'NumberAccompanyingPassport' in form):
            form['NumberAccompanyingPassport'] = None
        #in_ter.update(last_out=last_in,weghtOut=form['ves'],status_in=False,netto=abs(in_ter[0].weghtIn-int(form['ves'])))
        in_ter.update(number=form['gos_num_avto'], agent_vagon_id=form['Contragent'],    last_out=last_in, parentcontractid_id=form['Contract'],
                    description= form['Description'], seria=form['SeriesInvoice'],numberNakladnaia=form['NumberInvoice'], nakladnayaDate = form['DateInvoice'],
                    ves_nakladnaya=form['WeightInvoice'], price_ed_iz=form['ContractPrice'], discont= form['DirtPercent'],
                     weghtOut=float(form['ves']),netto=abs(in_ter[0].weghtIn-int(form['ves'])), parentuserid_id=request.user.id,operatrion = form['operation'],
                    type=form['TypeInvoice'], nds=form['NdsPercent'], ves_ed= form['UnitWeight'], typeOperation= form['TypeArrival'],
                    typeMaterial= form['TypeMaterialOut'], numberPasport= form['NumberAccompanyingPassport'], numberPassportList = form['NumberWayList'],
                status_in=False)
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
        if (not 'UnitWeight' in form):
            form['UnitWeight'] = None
        if (not 'TypeArrival' in form):
            form['TypeArrival'] = None
        if (not 'NdsPercent' in form):
            form['NdsPercent'] = None
        if (not 'TypeInvoice' in form):
            form['TypeInvoice'] = None
        if (not 'TypeMaterialOut' in form):
            form['TypeMaterialOut'] = None
        if (not 'NumberWayList' in form):
            form['NumberWayList'] = None
        if (not 'NumberAccompanyingPassport' in form):
            form['NumberAccompanyingPassport'] = None
        auto = Vagon(number=form['gos_num_avto'], agent_vagon_id=form['Contragent'],    last_in=last_in, parentcontractid_id=form['Contract'],
                    description= form['Description'], seria=form['SeriesInvoice'],numberNakladnaia=form['NumberInvoice'], nakladnayaDate = form['DateInvoice'],
                    ves_nakladnaya=form['WeightInvoice'], price_ed_iz=form['ContractPrice'], discont= form['DirtPercent'],
                     weghtIn=float(form['ves']), parentuserid_id=request.user.id,operatrion = form['operation'],
                    type=form['TypeInvoice'], nds=form['NdsPercent'], ves_ed= form['UnitWeight'], typeOperation= form['TypeArrival'],
                    typeMaterial= form['TypeMaterialOut'], numberPasport= form['NumberAccompanyingPassport'], numberPassportList = form['NumberWayList'],
                status_in=True)
        auto.save()
    allIn = Auto.objects.filter( status_in=True)
    all= vagonSql()
    allIn = serializers.serialize('json', allIn)
    print("==================================================")
    print(all[0])
    payload = {'success': True,'autoIn':allIn,"all":all}

    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')








