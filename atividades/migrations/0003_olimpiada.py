# Generated by Django 3.1.7 on 2021-04-12 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0002_auto_20210411_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Olimpiada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Campo Obrigatório*', max_length=250, verbose_name='Título')),
                ('data_inicial', models.DateField(blank=True, null=True, verbose_name='Data Inicial')),
                ('data_final', models.DateField(blank=True, null=True, verbose_name='Data Final')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
            ],
            options={
                'verbose_name': 'Olimpíada',
                'verbose_name_plural': 'Olimpíadas',
            },
        ),
    ]
