from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.core import exceptions
from GLOBAL import GlobalAutoUse
from apps.ves.models import User, GlobalData
from django.core import serializers
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
from apps.ves.consumers import *
from apps.ves.forms import UserForm, UpdUserForm
from apps.ves.models import Auto, ActionUser, Agent, Vagon
from ves_n.setting_data import USER_ROLES_FOR_REDIRECTS_CHOICES, USER_ROLES_SETTINGS


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
        one_entry = GlobalData.objects.get(id=1)
        auto = Auto.objects.filter(status_in=True)
        agents = Agent.objects.all()
        print(GlobalAutoUse)
        if (one_entry.Auto == True):
            print('woops')
            raise exceptions.PermissionDenied
        data = {'auto_in': auto, 'agetns':agents}
        return render(request, 'ves/avto_ves.html', data)



    @login_required
    def avto_data(request):
        autoAll = Auto.objects.all()
        json =serializers.serialize('json', autoAll)
        paginator = Paginator(autoAll, 10)  # Show 25 contacts per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {'page_obj': page_obj,"data":json}
        return render(request, 'ves/avto_data.html', data)



    @login_required
    def zd_ves(request):
        one_entry = GlobalData.objects.get(id=1)
        if (one_entry.Zd == True):
            print('woops')
            raise exceptions.PermissionDenied
        zd = Vagon.objects.filter(status_in=True)
        agents = Agent.objects.all()
        data = {'zd_in': zd, 'agetns': agents}
        return render(request, 'ves/zd_ves.html',data)


    @login_required
    def zd_data(request):
        autoAll = Vagon.objects.all().order_by("-date_add")
        uniqZd = Vagon.objects.raw('SELECT * from ves_vagon GROUP BY (id,number) having COUNT(*) = 1 ORDER BY id')
        agent = Agent.objects.all()
        json =serializers.serialize('json', uniqZd)
        paginator = Paginator(autoAll, 10)  # Show 25 contacts per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {'page_obj': page_obj,"data":json,"agents":agent,"uniq":uniqZd}
        return render(request, 'ves/zd_data.html', data)



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
        action = ActionUser.objects.all().order_by("-date_add")
        paginator = Paginator(action, 10)  # Show 25 contacts per page
        #print(dir(action[0].parentId))
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {'page_obj': page_obj}
        return render(request, 'data/action_view.html', data)



    @login_required
    def AgentView(request):
        agent = Agent.objects.all()
        agent_json = serializers.serialize('json', agent)
        paginator = Paginator(agent, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {'page_obj': page_obj,"agents":agent_json}
        return render(request, 'data/data_agents.html', data)

    @login_required
    def UserView(request):
        users = User.objects.all()
        agent_json = serializers.serialize('json', users)
        paginator = Paginator(users, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        user_form = UserForm()
        if request.method == 'POST':
            user_form = UserForm(request.POST)

            if user_form.is_valid():
                user_form.save()

                messages.success(request, _('Your profile was successfully updated!'))
                print('Your profile was successfully updated!')
                return redirect('ves:users')
            else:
                messages.error(request, _('Please correct the error below.'))
                print('Please correct the error below.')
        print("======")
        #print(users[5].profile.descriptions)
        data = {'page_obj': page_obj, "users": agent_json,"roles":USER_ROLES_SETTINGS,"userform":user_form}
        return render(request, 'data/user_view.html', data)

    @login_required
    @transaction.atomic
    def updateUserView(request,usid):
        if(not request.user.is_admin()):
            return HttpResponseForbidden()
        userupd = User.objects.get(pk=usid)
        if request.method == 'POST':
            user_form = UpdUserForm(request.POST, instance=userupd)

            if user_form.is_valid():
                user_form.save()

                messages.success(request, _('Your profile was successfully updated!'))
                print('Your profile was successfully updated!')
                return redirect('ves:users')
            else:
                messages.error(request, _('Please correct the error below.'))
                print('Please correct the error below.')
                return render(request, 'data/update_user.html', {'user_form': user_form})
        else:

            print(dir(userupd))
            user_form = UpdUserForm(instance=userupd)
            return render(request, 'data/update_user.html',{'user_form':user_form})
