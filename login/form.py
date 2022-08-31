from django import forms
from django.contrib.auth.forms import UserCreationForm
from custom.models import Account

class SignUpForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'hospital_name', 'unit_name', 'local_government', 'state', 'password1', 'password2', )
