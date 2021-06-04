__author__ = "Francisco Flávio Nogueira da Silva"
__copyright__ = "Copyright 2020, Flávio Silva"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Francisco Flávio Nogueira da Silva"
__email__ = "flavio981895788@gmail.com"
__status__ = "Production"


from django.db import models
from django.contrib.auth.models import User
from .destinatario import Destinatario
from djrichtextfield.models import RichTextField
from crum import get_current_user

class TemplateEmail(models.Model):
    """
    Classe que serve para o usuário fazer o template do seu email
    """
    assunto = models.CharField(
        max_length = 200,
        verbose_name = "Assunto"
    )

    corpo_email = RichTextField(
        verbose_name = "Corpo do email"
    )

    codigo = models.CharField(
        max_length = 50,
        verbose_name = "Código",
        unique = True
    )

    enviar_usuario_criacao = models.BooleanField(
        verbose_name = "Enviar usuário de criação"
    )

    destinatarios = models.ManyToManyField(
        Destinatario,
        verbose_name="Destinatários"
    )

    usuario_criacao = models.ForeignKey(
		'auth.User', 
		related_name='%(class)s_requests_created',
		blank=True, null=True,
		default=None,
		on_delete=models.SET_NULL
	)

    usuario_atualizacao = models.ForeignKey(
		'auth.User', 
		related_name='%(class)s_requests_modified',
		blank=True, null=True,
		default=None,
		on_delete=models.SET_NULL
	)

    def __str__(self):
        return self.assunto

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(TemplateEmail, self).save(*args, **kwargs)

    class Meta:
        app_label = "emails"
        verbose_name = "Template do email"
        verbose_name_plural = "Templates dos emails"
