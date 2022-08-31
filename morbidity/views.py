from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .form import dataForm
import datetime
from django.contrib.auth.decorators import login_required
# Create your views here

@login_required
def morbidity (request):
    submitted = False
    if request.method == 'POST':
        form = dataForm(request.POST)
        if form.is_valid():
            user_detail = form.save(commit=False)
            user_detail.User = request.user
            user_detail.user_time = datetime.datetime.now()
            user_detail.save()
            return HttpResponseRedirect('morbidity?submitted=True')
    else:
        form = dataForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "morbidity/morbidity.html",{
        'form':form,
        'submitted':submitted
    })
