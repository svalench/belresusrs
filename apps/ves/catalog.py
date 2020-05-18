import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from apps.ves.models import CatalogAuto, Agent, CatalogTrailer, Production


class CatalogAutoView(LoginRequiredMixin, CreateView):
    template_name = 'data/catalog_auto.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    @login_required
    def showAuto(request):
        auto = CatalogAuto.objects.all()
        agent = Agent.objects.all()
        data = {'agent':agent,'auto':auto}
        return render(request, 'data/catalog_auto.html',data)

    @login_required
    def addAuto(request):
        form =request.POST
        auto = CatalogAuto(number=form['number'],agent_id=form['agent'],tara=form['ves'],model=form['model'])
        auto.save()
        payload = {'success': True}
        return HttpResponse(json.dumps(payload), content_type='application/json')

    @login_required
    def addUpdate(request):
        form = request.POST
        auto = CatalogAuto.objects.filter(pk=request.POST['id']).update(number=form['number'],agent_id=form['agent'],tara=form['ves'],model=form['model'])
        payload = {'success': True}
        return HttpResponse(json.dumps(payload), content_type='application/json')



class CatalogTrailerView(LoginRequiredMixin, CreateView):
    template_name = 'data/catalog_trailer.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    @login_required
    def showTrailer(request):
        auto = CatalogTrailer.objects.all()
        agent = Agent.objects.all()
        data = {'agent': agent, 'auto': auto}
        return render(request, 'data/catalog_trailer.html', data)

    @login_required
    def addTrailer(request):
        form = request.POST
        auto = CatalogTrailer(number=form['number'], agent_id=form['agent'], tara=form['ves'], model=form['model'])
        auto.save()
        payload = {'success': True}
        return HttpResponse(json.dumps(payload), content_type='application/json')

    @login_required
    def addUpdate(request):
        form = request.POST
        auto = CatalogTrailer.objects.filter(pk=request.POST['id']).update(number=form['number'], agent_id=form['agent'],
                                                                        tara=form['ves'], model=form['model'])
        payload = {'success': True}
        return HttpResponse(json.dumps(payload), content_type='application/json')


class CatalogProductView(LoginRequiredMixin, CreateView):
    template_name = 'data/catalog_trailer.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def sowCatalog(request):
        catalog = Production.objects.all()
        data = {'catalog':catalog}
        return render(request, 'data/catalog_production.html', data)

    @login_required
    def addProduction(request):
        form = request.POST
        print("-----------===================-=-==============----------------------")
        auto = Production(name=form['name'], number=form['number'])
        auto.save()
        payload = {'success': True}
        return HttpResponse(json.dumps(payload), content_type='application/json')