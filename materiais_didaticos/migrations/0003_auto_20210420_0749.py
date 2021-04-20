# Generated by Django 3.1.7 on 2021-04-20 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiais_didaticos', '0002_delete_atareuniao'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarioatividade',
            name='foto_capa',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto de Capa'),
        ),
        migrations.AddField(
            model_name='calendarioatividade',
            name='retrato',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Retrato'),
        ),
        migrations.AddField(
            model_name='comunicado',
            name='foto_capa',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto de Capa'),
        ),
        migrations.AddField(
            model_name='comunicado',
            name='retrato',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Retrato'),
        ),
        migrations.AddField(
            model_name='materialdidatico',
            name='foto_capa',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto de Capa'),
        ),
        migrations.AddField(
            model_name='materialdidatico',
            name='retrato',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Retrato'),
        ),
    ]