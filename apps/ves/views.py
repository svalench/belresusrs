from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from apps.ves.consumers import *
from apps.ves.models import Auto, ActionUser, Agent


class StartView(LoginRequiredMixin, CreateView):
    template_name = 'ves/start.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        return context


    def get(self, request, **kwargs):
        # if (request.user.is_anonymous):
        #     return HttpResponseRedirect(reverse('login'))

        return render(request, self.template_name)

    @login_required
    def menu_ves(request):
        return render(request, 'ves/menu_ves.html')


    @login_required
    def avto_ves(request):
        auto = Auto.objects.filter(status_in=True)
        print(auto)
        if (globalAuto == True):
            print('woops')
            return HttpResponseRedirect(403)
        data = {'auto_in': auto }
        return render(request, 'ves/avto_ves.html', data)

    @login_required
    def zd_ves(request):
        return render(request, 'ves/zd_ves.html')



# класс для просмотра данных
class DataView(LoginRequiredMixin, CreateView):
    template_name = 'ves/start.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    @login_required
    def menu_data(request):
        return render(request, 'data/menu_data.html')

    @login_required
    def ActionView(request):
        action = ActionUser.objects.all()
        data = {'actions': action}
        return render(request, 'data/action_view.html', data)

    @login_required
    def AgentView(request):
        agent = Agent.objects.all()
        data = {'actions': agent}
        return render(request, 'data/data_agents.html', data)

