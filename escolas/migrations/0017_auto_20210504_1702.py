# Generated by Django 3.1.7 on 2021-05-04 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0016_auto_20210503_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='foto_capa',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto de Capa'),
        ),
    ]
