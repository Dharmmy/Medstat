"""custom_user_model URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.views.static import serve


admin.site.site_title = 'Medstat Admin Portal'
admin.site.index_title = 'Welcome to Medstat Admin Portal'

urlpatterns = [
    path('medstat/admin/o', admin.site.urls),
    path('', include('login.urls') ),
    path('discharge/', include('discharge.urls') ),
    path('mortality/', include('mortality.urls') ),
    path('morbidity/', include('morbidity.urls') ),
    path('morbiditychart/', include('morbiditychart.urls') ),
    path('mortalitychart/', include('mortalitychart.urls') ),
    path('dischargedchart/', include('dischargedchart.urls') ),
    path('datavisual/', include('Data_Visualization.urls') ),
   
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
