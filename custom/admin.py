from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account 
# Register your models here.

class UserAdminConfig(UserAdmin):
    list_display=['username', 'email', 'hospital_name','unit_name','local_government', 'state']
    search_fields=['email','username','hospital_name','unit_name','local_government', 'state']
    readonly_fields=['date_joined','last_login']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email','hospital_name','unit_name','local_government', 'state')}),
        ('Activity', {'fields': ('date_joined','last_login')}),
        ('Permissions', {'fields': ('is_admin','is_active','is_staff','is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'hospital_name','unit_name','local_government', 'state', 'password1', 'password2'),
        }),
    )

admin.site.register(Account,UserAdminConfig)