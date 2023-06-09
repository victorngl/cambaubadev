# Generated by Django 3.1.7 on 2021-04-24 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('escolas', '0003_materia_hexadecimal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.pessoa')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario_professor', to=settings.AUTH_USER_MODEL, verbose_name='Usuário do Professor')),
            ],
            bases=('core.pessoa',),
        ),
        migrations.AddField(
            model_name='turma',
            name='professores',
            field=models.ManyToManyField(blank=True, to='escolas.Professor', verbose_name='Professor'),
        ),
    ]
