# Generated by Django 3.1.7 on 2021-07-22 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0022_auto_20210722_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representanteturma',
            name='aluno',
            field=models.CharField(max_length=70, null=True, verbose_name='Aluno'),
        ),
    ]
