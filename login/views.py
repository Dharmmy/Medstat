from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .form import SignUpForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .form import SignUpForm
# Create your views here.


def index (request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "login/homepage.html")


def login_view (request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render (request,"login/login.html",{
                "message": "Invalid credentials"
            })
    return render(request, "login/login.html")

def logout_view (request):
    logout (request)
    return render (request,"login/login.html",{
                "message": "You've been logged out"
            })



class Registration (CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'login/signup.html'
