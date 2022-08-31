# Generated by Django 4.0.5 on 2022-06-30 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MorbidityData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.CharField(choices=[('None', 'Select age'), ('0-5', '0-5'), ('6-10', '6-10'), ('11-15', '11-15'), ('16-20', '16-20'), ('21-25', '21-25'), ('26-30', '26-30'), ('31-35', '31-35'), ('36-40', '36-40'), ('41-45', '41-45'), ('46-50', '46-50'), ('51-55', '51-55'), ('56-60', '56-60'), ('61-65', '61-65'), ('66-70', '66-70'), ('71-75', '71-75'), ('76-80', '76-80'), ('81-85', '81-85'), ('86-90', '86-90'), ('91-95', '91-95'), ('96-100', '96-100'), ('101 and above', '101 and above')], default='', max_length=20)),
                ('Sex', models.CharField(choices=[('None', 'Select gender'), ('male', 'MALE'), ('female', 'FEMALE')], default='', max_length=6)),
                ('Disease', models.CharField(default='', max_length=40, verbose_name='Morbidity disease')),
                ('user_time', models.DateTimeField(default='')),
                ('User', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
