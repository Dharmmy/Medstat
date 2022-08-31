from django import forms
from django.forms import ModelForm
from .models import MorbidityData


class dataForm (ModelForm):
    class Meta:
        model = MorbidityData
        fields = ('Age', 'Sex', 'Disease')
        widgets = {
        'Age'  : forms.Select(attrs= {'class':'form-control'}),
        'Sex' : forms.Select(attrs= {'class':'form-control'}),
        'Disease': forms.TextInput(attrs = {'class':'form-control'})
        }