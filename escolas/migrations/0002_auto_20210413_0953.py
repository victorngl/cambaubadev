# Generated by Django 3.1.7 on 2021-04-13 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('escolas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario_aluno', to=settings.AUTH_USER_MODEL, verbose_name='Usuário do Aluno'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='responsavel1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsavel1_aluno', to=settings.AUTH_USER_MODEL, verbose_name='Responsável 1'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='responsavel2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsavel2_aluno', to=settings.AUTH_USER_MODEL, verbose_name='Responsável 2'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='responsavel3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsavel3_aluno', to=settings.AUTH_USER_MODEL, verbose_name='Responsável 3'),
        ),
    ]
