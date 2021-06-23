# Generated by Django 3.1.7 on 2021-06-10 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atividades_escolares', '0013_auto_20210608_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividadeescolar',
            name='anexos',
        ),
        migrations.AddField(
            model_name='anexosatividadeescolar',
            name='atividade_escolare',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='atividades_escolares.atividadeescolar', verbose_name='Atividade Escolar'),
        ),
    ]