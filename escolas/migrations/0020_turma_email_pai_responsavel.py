# Generated by Django 3.1.7 on 2021-07-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0019_auto_20210604_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='email_pai_responsavel',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Email do Pai Responsável'),
        ),
    ]
