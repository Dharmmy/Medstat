from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
import datetime
from django.http import HttpRequest

# Create your models here.

Ages = (
    ('None', 'Select age'),
    ('0-5', '0-5'),
    ('6-10', '6-10'),
    ('11-15', '11-15' ),
    ('16-20', '16-20'),
    ('21-25', '21-25'),
    ('26-30', '26-30' ),
    ('31-35', '31-35'),
    ('36-40', '36-40'),
    ('41-45', '41-45'),
    ('46-50', '46-50'),
    ('51-55', '51-55'),
    ('56-60', '56-60'),
    ('61-65', '61-65'),
    ('66-70', '66-70'),
    ('71-75', '71-75'),
    ('76-80', '76-80'),
    ('81-85', '81-85' ),
    ('86-90', '86-90'),
    ('91-95', '91-95'),
    ('96-100', '96-100'),
    ('101 and above', '101 and above'),
)

Gender = (
    ('None', 'Select gender'),
    ('male', 'MALE'),
    ('female','FEMALE')
)




class MorbidityData (models.Model):
    Age = models.CharField(max_length=20, choices=Ages, default='')
    Sex = models.CharField(max_length=6, choices=Gender, default='')
    Disease =models.CharField('Morbidity disease', max_length=40, default='')
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)
    user_time = models.DateTimeField( default='')

    

    
    def __str__(self):
        return f"{self.user_time}, {self.Age}, {self.Sex}, {self.Disease}" 
