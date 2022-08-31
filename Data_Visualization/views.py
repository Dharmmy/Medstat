from django.shortcuts import render
# Create your views here.

def index(request):
    if request.user.is_superuser:
        return render (request,'Data_visualization/data_visual.html')
    