# Generated by Django 3.1.7 on 2021-04-26 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atividades_escolares', '0005_auto_20210422_1036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividadeescolar',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='atividadeescolar',
            name='foto_capa',
        ),
    ]
