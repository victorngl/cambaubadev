# Generated by Django 3.1.7 on 2021-04-21 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiais_didaticos', '0007_auto_20210421_0646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendarioatividade',
            old_name='retrato',
            new_name='foto',
        ),
        migrations.RenameField(
            model_name='comunicado',
            old_name='retrato',
            new_name='foto',
        ),
        migrations.RenameField(
            model_name='materialdidatico',
            old_name='retrato',
            new_name='foto',
        ),
    ]
