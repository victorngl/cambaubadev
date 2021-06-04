__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2019, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from core.models import Endereco
from crum import get_current_user


class Evento(models.Model):
    """
    Classe Evento implementa as funções relacionadas a um evento de agenda na plataforma.
    """
    nome = models.CharField(
        verbose_name="Nome",
        max_length=150,
        blank=True, null=True
    )

    descricao = models.TextField(
        verbose_name="Descrição",
        blank=True, null=True
    )

    data = models.DateField(
        verbose_name="Data"
    )

    hora_inicio = models.TimeField(
        verbose_name="Hora de Início",
        blank=True, null=True
    )

    hora_termino = models.TimeField(
        verbose_name="Hora de Término",
        blank=True, null=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="User",
        blank=True,
        null=True
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

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        default=datetime.now
    )

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(Evento, self).save(*args, **kwargs)

    class Meta:
        app_label = "calendario"
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

