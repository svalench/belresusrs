import abc
from openpyxl_templates import TemplatedWorkbook, TemplatedWorksheet
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
import json
import threading
from abc import ABCMeta
from django.core.serializers import serialize
from django.db.models import Q
from datetime import datetime
from django.contrib.auth import logout

from docxtpl import DocxTemplate


from django.http import HttpResponse
from django.shortcuts import redirect, render

from apps.ves.models import ActionUser, Auto, Agent, DataNakladnayaAuto, Vagon, DataNakladnayaVagon, User, GlobalData, \
    Production
from apps.ves.snap7_plc import PlcRemoteUse


def logout_view(request):
    logout(request)
    return redirect('login')

def addactionView(request, *args, **kwargs):
    form = request.POST
    model = ActionUser(where=form['where'], action=form['action'], parentId=User(id=form['user']))
    model.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')




def addAutoView(request):
    form = request.POST
    last_in = datetime.now()
    in_ter = Auto.objects.filter(number=form['numAuto'], status_in=True)
    if in_ter.exists():
        in_ter[0].last_out=last_in
        in_ter[0].ves_out=form['ves']
        in_ter[0].status_in=False
        in_ter[0].netto = abs(in_ter[0].ves_in-int(form['ves']))
        in_ter.update(last_out=last_in,ves_out=form['ves'],status_in=False,netto=abs(in_ter[0].ves_in-int(form['ves'])))
    else:
        dataNakl = form.getlist('nakladnaya')
        agent = Agent.objects.get(pk=form['contragent'])
        print(form)
        auto = Auto(number=form['numAuto'], agents=agent, tara=int(form['typeCar']), catalog_id=int(form['catalogId']),
                    number_pricep=form['numPricep'], last_in=last_in, ves_in=float(form['ves']),
                status_in=True)
        auto.save()

        arr=[]
        for a in dataNakl:
            r = a.split(",")
            product = Production.objects.get(id=r[18])
            arr.append(DataNakladnayaAuto(type=r[8],number=r[10],seria=r[9],
                                          name=r[0],ves_ed=r[2],ves_nakladnaya=r[1],
                                          name_drive=r[15], osnovanie=r[17], pogruzka=r[12],
                                          prinyal=r[14], putlist=r[13], razreshil=r[11],
                                          price_ed=r[5],price_one=r[3],price_no_nds=r[4],nds=r[7], date=r[19],
                                          price=r[6], parentId = auto,productionId_id=r[18]))
        DataNakladnayaAuto.objects.bulk_create(arr)
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')





def addVagonPost(request):
    form = request.POST
    last_in = datetime.now()
    in_ter = Vagon.objects.filter(number=form['numAuto'], status_in=True)
    if in_ter.exists():
        in_ter.update(last_out=last_in, ves_out=form['ves'], status_in=False,netto=abs(in_ter[0].ves_in-int(form['ves'])))
    else:
        agent = Agent.objects.get(id=form['contragent'])
    #///////////////////////////////
        zd = Vagon(number=form['numAuto'], agent_vagon=agent, nakladnaya=form['nakladnaya'],
                last_in=last_in, ves_in=form['ves'],
                status_in=True)
        zd.save()
        dataNakl = form.getlist('dataNakladnay')
        arr = []
        for a in dataNakl:
            r = a.split(",")
            arr.append(
            DataNakladnayaVagon(number=r[0], name=r[1], price=r[2], price_ed=r[3], ves_nakladnaya=r[4], ves_ed=r[5],
                               parentId=zd))
        DataNakladnayaVagon.objects.bulk_create(arr)
    #//////////////////////////////
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')




def addContragentView(request):
    form = request.POST
    now = datetime.now()
    agent = Agent(name=form['name'],unp=form["unp"], description=form['description'], address=form['address'])
    agent.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')


def updContragentView(request):
    form = request.POST
    now = datetime.now()
    address = form['address']
    agetnt = Agent.objects.get(id=form['id'])
    agetnt.name = form['name']
    agetnt.unp = form['unp']
    agetnt.description = form['description']
    agetnt.address = address
    agetnt.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload), content_type='application/json')

def GetDataAuto(request):
    try:
        one_entry = GlobalData.objects.get(id=1)
    except ObjectDoesNotExist:
        one_entry = GlobalData(Auto=False)

    form = request.POST
    if (form["all"]=="true"):
        one_entry.Auto=False
        one_entry.Zd=False
    else:
        if(form['zanyato']):
            one_entry.Auto = True
    one_entry.save()
    print(one_entry.Auto)
    try:
        ves = PlcRemoteUse('192.168.0.1')
        ves.getWeight()
        bitmask = ves.getSatusBit(0)
        weight = ves.ves
    except:
        weight="error"
        bitmask = "error"
    dataRecive = {
        'plc':"1200",
        "type":"vrs",
	"ves":weight,
        "bits":bitmask,
        'global':one_entry.Auto,
    }
    return HttpResponse(json.dumps(dataRecive), content_type='application/json')



def GetDataZd(request):
    try:
        one_entry = GlobalData.objects.get(id=1)
    except ObjectDoesNotExist:
        one_entry = GlobalData(Auto=False)

    form = request.POST

    if(form['zanyato']):
        one_entry.Zd = True
    one_entry.save()

    try:
        ves = PlcRemoteUse('192.168.0.2')
        ves.getWeight()
        bitmask = ves.getSatusBit(0)
        weight = ves.ves
    except:
        weight="error"
        bitmask = "error"
    dataRecive = {
        'plc':"1200",
        'ves':weight,
        'bits':bitmask,
        "type":"vrs",
        'global':one_entry.Auto,
    }
    return HttpResponse(json.dumps(dataRecive), content_type='application/json')

def GetDataStatus(request):
    try:
        one_entry = GlobalData.objects.get(id=1)
    except ObjectDoesNotExist:
        one_entry = GlobalData(Auto=False)
    dataRecive = {
        'plc':"1200",
        "type":"vrs",
        'auto':one_entry.Auto,
        'zd': one_entry.Zd,
    }
    return HttpResponse(json.dumps(dataRecive), content_type='application/json')


def GetZdNumber(request):
    form = request.POST
    allZdNum =Vagon.objects.filter(number=form['num'], status_in=False)
    if allZdNum.exists():
        col =allZdNum.count();
        sum=0
        for a in allZdNum:
            sum=sum+a.netto
        srednee = sum/col
    else:
        sum=0
        srednee=0
        col=0
    dataRecive = {
        'sum': sum,
        "srednee": srednee,
        "col":col
    }
    return HttpResponse(json.dumps(dataRecive), content_type='application/json')


def GetZdAgent(request):
    form = request.POST
    allZdAgent = Vagon.objects.filter(agent_vagon=form['agentId'], status_in=False)
    if allZdAgent.exists():
        col = allZdAgent.count()
        sum = 0
        for a in allZdAgent:
            sum = sum + a.netto
        srednee = sum / col
    else:
        col=0
        sum=0
        srednee=0
    dataRecive = {
        'sum': sum,
        "srednee": srednee,
        "col": col
    }
    return HttpResponse(json.dumps(dataRecive), content_type='application/json')


def GetZdDate(request):
    form = request.POST
    allZdAgent = Vagon.objects.filter(last_in__gte=form['start'],last_out__lte=form['end'], status_in=False)
    if allZdAgent.exists():
        col = allZdAgent.count()
        sum = 0
        for a in allZdAgent:
            sum = sum + a.netto
        srednee = sum / col
    else:
        col=0
        sum=0
        srednee=0
    dataRecive = {
        'sum': sum,
        "srednee": srednee,
        "col": col
    }
    return HttpResponse(json.dumps(dataRecive), content_type='application/json')





def GetAutoNumber(request):
    form = request.POST
    allZdNum =Auto.objects.filter(number=form['num'], status_in=False)
    auto_json = serializers.serialize('json', allZdNum)
    if allZdNum.exists():
        col =allZdNum.count();
        sum=0
        for a in allZdNum:
            sum=sum+a.netto
        srednee = sum/col
    else:
        sum=0
        srednee=0
        col=0
    dataRecive = {
        'sum': sum,
        "srednee": srednee,
        "col":col,
        "auto":auto_json
    }
    return HttpResponse(json.dumps(dataRecive), content_type='application/json')





def GetAutoAgent(request):
    form = request.POST
    allZdAgent = Auto.objects.filter(agents=form['agentId'], status_in=False)
    if allZdAgent.exists():
        auto_json = serializers.serialize('json', allZdAgent)
        col = allZdAgent.count()
        sum = 0
        for a in allZdAgent:
            sum = sum + a.netto
        srednee = sum / col
    else:
        col=0
        sum=0
        srednee=0
    dataRecive = {
        'sum': sum,
        "srednee": srednee,
        "col": col,
        "auto": auto_json
    }
    return HttpResponse(json.dumps(dataRecive), content_type='application/json')


def GetAutoDate(request):
    form = request.POST
    allZdAgent = Auto.objects.filter(last_in__gte=form['start'],last_out__lte=form['end'], status_in=False)
    if allZdAgent.exists():
        col = allZdAgent.count()
        sum = 0
        for a in allZdAgent:
            sum = sum + a.netto
        srednee = sum / col
    else:
        col=0
        sum=0
        srednee=0
    dataRecive = {
        'sum': sum,
        "srednee": srednee,
        "col": col
    }
    return HttpResponse(json.dumps(dataRecive), content_type='application/json')

#метод вовращает данные исходя из строки поиска для модели
def serchAuto(request):
    form = request.POST
    result=""
    search = form['search']
    if(form['request']=="auto"):
        if(form['case']=="auto"):
            result =Auto.objects.filter(Q(number__contains=search) | Q(number_pricep__contains=search) | Q(last_in__contains=search) | Q(last_out__contains=search) | Q(nakladnaya__contains=search))
    elif(form['request']=="zd"):
        result = Vagon.objects.filter(
            Q(number__contains=search)  | Q(last_in__contains=search) | Q(
                last_out__contains=search) | Q(nakladnaya__contains=search))

    res = serializers.serialize('json', result)
    print(res)
    return HttpResponse(res, content_type='application/json')


class DemoTemplatedWorkbook(TemplatedWorkbook):
    sheet1 = TemplatedWorksheet()
    sheet2 = TemplatedWorksheet()



#
def reportAutoAgent(request):
    form = request.GET

    #tpl = DocxTemplate('templates/doc/template_execel.xls')
    tpl = DemoTemplatedWorkbook('templates/doc/template_execel.xlsx')
    context = {
        'agent':'str',
        'agent_adress': 'str',
        'agent_unp': 'str',
        'col_labels': ['вес на въезде', 'вес на выезде', 'дата въезда', 'дата выезда',"нетто"],
        'tbl_contents': [
            {'label': 'yellow', 'cols': ['banana', 'capsicum', 'pyrite', 'taxi']},
            {'label': 'red', 'cols': ['apple', 'tomato', 'cinnabar', 'doubledecker']},
            {'label': 'green', 'cols': ['guava', 'cucumber', 'aventurine', 'card']},
        ],
    } 
    print(dir(tpl))
    tpl.sheet1.write(context)

    #application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
    #response = HttpResponse( content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    #response = HttpResponse( content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    response['Content-Disposition'] = 'attachment; filename='+dt_string+'.xlsx'
    tpl.save(response)
    return response


def onOffS1(request):
    bit=request.POST['bit']
    byte=request.POST['byte']
    try:
        ves = PlcRemoteUse('192.168.0.1')
        answ = ves.changeBit(byte,bit)
    except:
        answ="error"
    dataRecive = {
        'answer':answ,
        'sum': 'good'
    }
    return HttpResponse(json.dumps(dataRecive), content_type='application/json')



def onOffZd(request):
    bit=request.POST['bit']
    byte=request.POST['byte']
    try:
        ves = PlcRemoteUse('192.168.0.2')
        answ = ves.changeBit(byte,bit)
    except:
        answ="error"
    dataRecive = {
        'answer':answ,
        'sum': 'good'
    }
    return HttpResponse(json.dumps(dataRecive), content_type='application/json')

