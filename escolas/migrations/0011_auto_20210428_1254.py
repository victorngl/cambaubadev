# Generated by Django 3.1.7 on 2021-04-28 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escolas', '0010_auto_20210428_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={'verbose_name': 'Aluno', 'verbose_name_plural': 'Alunos'},
        ),
        migrations.AlterModelOptions(
            name='escola',
            options={'verbose_name': 'Escola', 'verbose_name_plural': 'Escolas'},
        ),
        migrations.AlterModelOptions(
            name='materia',
            options={'verbose_name': 'Matéria', 'verbose_name_plural': 'Matérias'},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name': 'Professor', 'verbose_name_plural': 'Professores'},
        ),
        migrations.AlterModelOptions(
            name='serie',
            options={'verbose_name': 'Série', 'verbose_name_plural': 'Séries'},
        ),
        migrations.AlterModelOptions(
            name='tiposerie',
            options={'verbose_name': 'Tipo de Série', 'verbose_name_plural': 'Tipos de série'},
        ),
        migrations.AlterModelOptions(
            name='turma',
            options={'verbose_name': 'Turma', 'verbose_name_plural': 'Turmas'},
        ),
    ]