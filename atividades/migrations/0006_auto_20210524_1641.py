# Generated by Django 3.1.7 on 2021-05-24 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0018_auto_20210505_1307'),
        ('atividades', '0005_auto_20210422_1036'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inscricaoatividadeextra',
            unique_together={('aluno', 'atividade_extra')},
        ),
    ]