from django.urls import path

from . import views

urlpatterns = [
   # path("", views.index, name="index"),
    path("", views.Chart, name="mortalitychart"),
    path("disease", views.diseaseChart, name="mortalitydiseasechart")

]