# Generated by Django 3.1.7 on 2021-04-29 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiais_didaticos', '0018_auto_20210426_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='foto_capa',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto de Capa'),
        ),
    ]
