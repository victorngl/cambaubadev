# Generated by Django 2.1.5 on 2020-08-18 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_auto_20200812_1700'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='templateemail',
            options={'verbose_name': 'Template do email', 'verbose_name_plural': 'Templates dos emails'},
        ),
    ]
