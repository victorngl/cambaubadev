# Generated by Django 3.1.7 on 2021-06-08 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividades_escolares', '0010_auto_20210608_0946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anexosatividadeescolar',
            options={'ordering': ['-id'], 'verbose_name': 'Anexo', 'verbose_name_plural': 'Anexos'},
        ),
        migrations.RemoveField(
            model_name='atividadeescolar',
            name='anexos',
        ),
        migrations.AddField(
            model_name='atividadeescolar',
            name='anexos',
            field=models.ManyToManyField(blank=True, to='atividades_escolares.AnexosAtividadeEscolar', verbose_name='Anexo'),
        ),
    ]
