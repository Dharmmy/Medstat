from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
# Create your models here.


class profile (models.Model):
    username      = models.CharField(max_length=30,unique=True)
    email         = models.EmailField(_('email address'),max_length=60,unique=True)
    hospital_name    = models.CharField(max_length=60,blank=True)
    unit_name     = models.CharField(max_length=60,blank=True)
    local_government  = models.CharField(max_length=100,blank=True)
    state  = models.CharField(max_length=100,blank=True)




@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

