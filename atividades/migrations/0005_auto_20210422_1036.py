# Generated by Django 3.1.7 on 2021-04-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0004_auto_20210421_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividadeextra',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='atividadenoturna',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='oficina',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto'),
        ),
    ]
