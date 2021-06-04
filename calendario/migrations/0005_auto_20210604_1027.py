# Generated by Django 3.1.7 on 2021-06-04 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendario', '0004_auto_20200108_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='usuario_atualizacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evento_requests_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='evento',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evento_requests_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
