# Generated by Django 3.1.7 on 2021-06-04 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('atividades', '0007_auto_20210524_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividadeextra',
            name='usuario_atualizacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atividadeextra_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='atividadeextra',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atividadeextra_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='atividadenoturna',
            name='usuario_atualizacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atividadenoturna_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='atividadenoturna',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atividadenoturna_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inscricaoatividadeextra',
            name='usuario_atualizacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inscricaoatividadeextra_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inscricaoatividadeextra',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inscricaoatividadeextra_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inscricaoatividadenoturna',
            name='usuario_atualizacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inscricaoatividadenoturna_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inscricaoatividadenoturna',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inscricaoatividadenoturna_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inscricaooficina',
            name='usuario_atualizacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inscricaooficina_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inscricaooficina',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inscricaooficina_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='oficina',
            name='usuario_atualizacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oficina_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='oficina',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oficina_requests_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='olimpiada',
            name='usuario_atualizacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olimpiada_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='olimpiada',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olimpiada_requests_created', to=settings.AUTH_USER_MODEL),
        ),
    ]