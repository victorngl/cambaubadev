# Generated by Django 3.1.7 on 2021-05-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210427_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_sigma',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ID Sigma'),
        ),
    ]