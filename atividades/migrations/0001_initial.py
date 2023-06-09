# Generated by Django 3.1.7 on 2021-04-12 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('escolas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AtividadeExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Campo Obrigatório*', max_length=250, verbose_name='Título')),
                ('vagas', models.IntegerField(blank=True, null=True, verbose_name='Vagas')),
                ('data_inicial', models.DateField(blank=True, null=True, verbose_name='Data Inicial')),
                ('data_final', models.DateField(blank=True, null=True, verbose_name='Data Final')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('retrato', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Retrato')),
                ('foto_capa', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto de Capa')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('turmas', models.ManyToManyField(blank=True, to='escolas.Turma', verbose_name='Turmas')),
            ],
            options={
                'verbose_name': 'Atividade Extra',
                'verbose_name_plural': 'Atividades Extras',
            },
        ),
        migrations.CreateModel(
            name='AtividadeNoturna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Campo Obrigatório*', max_length=250, verbose_name='Título')),
                ('vagas', models.IntegerField(blank=True, null=True, verbose_name='Vagas')),
                ('data_inicial', models.DateField(blank=True, null=True, verbose_name='Data Inicial')),
                ('data_final', models.DateField(blank=True, null=True, verbose_name='Data Final')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('retrato', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Retrato')),
                ('foto_capa', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto de Capa')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('turmas', models.ManyToManyField(blank=True, to='escolas.Turma', verbose_name='Turmas')),
            ],
            options={
                'verbose_name': 'Atividade Noturna',
                'verbose_name_plural': 'Atividades Noturnas',
            },
        ),
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Campo Obrigatório*', max_length=250, verbose_name='Título')),
                ('vagas', models.IntegerField(blank=True, null=True, verbose_name='Vagas')),
                ('data_inicial', models.DateField(blank=True, null=True, verbose_name='Data Inicial')),
                ('data_final', models.DateField(blank=True, null=True, verbose_name='Data Final')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('retrato', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Retrato')),
                ('foto_capa', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto de Capa')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('turmas', models.ManyToManyField(blank=True, to='escolas.Turma', verbose_name='Turmas')),
            ],
            options={
                'verbose_name': 'Oficina',
                'verbose_name_plural': 'Oficinas',
            },
        ),
        migrations.CreateModel(
            name='InscricaoOficina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('aluno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escolas.aluno', verbose_name='Aluno')),
                ('oficina', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='atividades.oficina', verbose_name='Oficina')),
                ('usuario_inscricao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário inscrito')),
            ],
            options={
                'verbose_name': 'Inscrição na Oficina',
                'verbose_name_plural': 'Inscrições na Oficina',
            },
        ),
        migrations.CreateModel(
            name='InscricaoAtividadeNoturna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('aluno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escolas.aluno', verbose_name='Aluno')),
                ('atividade_noturna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='atividades.atividadenoturna', verbose_name='Atividade Noturna')),
                ('usuario_inscricao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário Inscrição')),
            ],
            options={
                'verbose_name': 'Inscrição na Atividade Noturna',
                'verbose_name_plural': 'Inscrições na Atividade Noturna',
            },
        ),
        migrations.CreateModel(
            name='InscricaoAtividadeExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data de Alteração')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('aluno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='escolas.aluno', verbose_name='Aluno')),
                ('atividade_extra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='atividades.atividadeextra', verbose_name='Atividade Extra')),
                ('usuario_inscricao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário Inscrição')),
            ],
            options={
                'verbose_name': 'Inscrição na Atividade Extra',
                'verbose_name_plural': 'Inscrições na Atividade Extra',
            },
        ),
    ]
