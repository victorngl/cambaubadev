# Generated by Django 2.2.4 on 2020-01-08 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('data', models.DateField(verbose_name='Data')),
                ('hora_inicio', models.TimeField(verbose_name='Hora de Início')),
                ('hora_termino', models.TimeField(verbose_name='Hora de Término')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
    ]
