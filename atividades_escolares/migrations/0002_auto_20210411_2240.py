# Generated by Django 3.1.7 on 2021-04-12 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividades_escolares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividadeescolar',
            name='horario_fim',
            field=models.CharField(blank=True, max_length=250, verbose_name='Horário de Fim'),
        ),
        migrations.AddField(
            model_name='atividadeescolar',
            name='horario_inicio',
            field=models.CharField(blank=True, max_length=250, verbose_name='Horário de Início'),
        ),
    ]
