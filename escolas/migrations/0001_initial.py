# Generated by Django 3.1.7 on 2021-04-12 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Escola')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Série')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('escola', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escolas.escola', verbose_name='Escola')),
            ],
        ),
        migrations.CreateModel(
            name='TipoSerie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Título')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('serie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escolas.serie', verbose_name='Série')),
            ],
        ),
        migrations.AddField(
            model_name='serie',
            name='tipo_serie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escolas.tiposerie', verbose_name='Tipo da Série'),
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.pessoa')),
                ('qtd_atividades_permitidas', models.IntegerField(blank=True, default=1, null=True, verbose_name='Quantidade de Atividades Permitidas')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('responsavel1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsavel1_aluno', to=settings.AUTH_USER_MODEL, verbose_name='Responsável 1')),
                ('responsavel2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsavel2_aluno', to=settings.AUTH_USER_MODEL, verbose_name='Responsável 2')),
                ('responsavel3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsavel3_aluno', to=settings.AUTH_USER_MODEL, verbose_name='Responsável 3')),
                ('turma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escolas.turma', verbose_name='Turma')),
            ],
            bases=('core.pessoa',),
        ),
    ]
