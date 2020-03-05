from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from apps.ves.consumers import *



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

        return render(request,'ves/menu_ves.html')

    @login_required
    def avto_ves(request):
        print(globalAuto)
        if (globalAuto == True):
            print('woops')
            return HttpResponseRedirect(403)

        return render(request, 'ves/avto_ves.html')

    @login_required
    def zd_ves(request):
        return render(request, 'ves/zd_ves.html')