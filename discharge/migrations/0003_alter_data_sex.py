# Generated by Django 4.0.5 on 2022-07-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discharge', '0002_alter_data_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='Sex',
            field=models.CharField(choices=[('None', 'Select gender'), ('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='', max_length=6),
        ),
    ]
