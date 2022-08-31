from django.urls import path

from . import views

urlpatterns = [
   # path("", views.index, name="index"),
    path("", views.Chart, name="morbiditychart"),
    path("disease", views.diseaseChart, name="morbidityDiseasechart")

]