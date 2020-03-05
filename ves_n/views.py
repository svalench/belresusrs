import abc
import threading
from abc import ABCMeta

from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    return redirect('login')