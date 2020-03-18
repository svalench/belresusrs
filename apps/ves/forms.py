from django import forms

from django.contrib.auth.forms import UserCreationForm

from apps.ves.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username', 'password1', 'password2','birth_date', 'name','secondName','lastName','role','phone','user_role','descriptions')

