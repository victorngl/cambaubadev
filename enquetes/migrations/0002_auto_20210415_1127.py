# Generated by Django 3.1.7 on 2021-04-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquetes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquete',
            name='foto_capa',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto de Capa'),
        ),
        migrations.AddField(
            model_name='enquete',
            name='retrato',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Retrato'),
        ),
    ]
