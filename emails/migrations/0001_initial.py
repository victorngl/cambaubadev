# Generated by Django 2.1.1 on 2020-08-11 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destinatario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Destinatário',
                'verbose_name_plural': 'Destinatários',
            },
        ),
        migrations.CreateModel(
            name='MensagemEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enviado', models.BooleanField(default=False, verbose_name='Enviado')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
            ],
            options={
                'verbose_name': 'Mensagem do email',
                'verbose_name_plural': 'Mensagens dos emails',
            },
        ),
        migrations.CreateModel(
            name='TemplateEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', djrichtextfield.models.RichTextField(max_length=200, verbose_name='Assunto')),
                ('corpo_email', models.TextField(verbose_name='Corpo do email')),
                ('codigo', models.CharField(max_length=50, unique=True, verbose_name='Código')),
                ('enviar_usuario_criacao', models.BooleanField(verbose_name='Enviar usuário de criação')),
                ('destinatarios', models.ManyToManyField(to='emails.Destinatario', verbose_name='Destinatários')),
            ],
            options={
                'verbose_name': 'Template do Email',
                'verbose_name_plural': 'Templates dos Emails',
            },
        ),
        migrations.AddField(
            model_name='mensagememail',
            name='template_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emails.TemplateEmail', verbose_name='Template do email'),
        ),
        migrations.AddField(
            model_name='mensagememail',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mensagememail_requests_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
