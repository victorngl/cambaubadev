# Generated by Django 3.1.7 on 2021-04-20 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informativos', '0004_auto_20210420_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentacaoobra',
            name='foto_capa',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto de Capa'),
        ),
        migrations.AddField(
            model_name='documentacaoobra',
            name='retrato',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Retrato'),
        ),
    ]