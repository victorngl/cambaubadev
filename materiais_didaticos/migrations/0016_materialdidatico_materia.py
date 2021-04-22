# Generated by Django 3.1.7 on 2021-04-22 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0006_merge_20210422_1003'),
        ('materiais_didaticos', '0015_tipomaterialdidatico_icone'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialdidatico',
            name='materia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escolas.materia', verbose_name='Materia'),
        ),
    ]
