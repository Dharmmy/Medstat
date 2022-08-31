from django.utils.html import format_html
from django.contrib import admin

# Register your models here.

class dataVisualization(admin.ModelAdmin):
    list_display = ['show_firm_url']

    def show_firm_url(self, obj):
      return  format_html("<a href='{morbiditychart}>{morbiditychart}</a>", url=obj.morbiditychart_urls)