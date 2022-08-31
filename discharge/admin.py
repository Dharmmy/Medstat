from django.contrib import admin
from .models import Dischargeddata
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ( 'user_time', 'User', 'Age', 'Sex', 'Disease',)
    search_fields=['Age', 'Disease', 'Sex', 'User__username', 'User__local_government', 'User__state', 'User__hospital_name', 'User__unit_name', 'user_time']
    list_filter =['Age', 'Disease', 'Sex', 'user_time', 'User__local_government', 'User__state', 'User__hospital_name']
admin.site.register(Dischargeddata, DataAdmin)
