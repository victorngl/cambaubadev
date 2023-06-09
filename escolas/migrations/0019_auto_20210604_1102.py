# Generated by Django 3.1.7 on 2021-06-04 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('escolas', '0018_auto_20210505_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='escola',
            name='usuario_atualizacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='escola_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='escola',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='escola_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='materia',
            name='usuario_atualizacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='materia_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='materia',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='materia_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='serie',
            name='usuario_atualizacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='serie_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='serie',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='serie_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tiposerie',
            name='usuario_atualizacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tiposerie_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tiposerie',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tiposerie_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='turma',
            name='usuario_atualizacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turma_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='turma',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turma_requests_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
