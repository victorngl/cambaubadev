# Generated by Django 3.1.7 on 2021-07-22 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informativos', '0012_auto_20210614_1626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentacaoobra',
            options={'ordering': ['-data'], 'verbose_name': 'AEMC Notícia', 'verbose_name_plural': 'AEMC Notícias'},
        ),
    ]
