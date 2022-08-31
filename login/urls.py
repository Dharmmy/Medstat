from django.urls import path
from django.conf.urls import include
from . import views
from .views import Registration

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('registration/', Registration.as_view(), name="registration")
]