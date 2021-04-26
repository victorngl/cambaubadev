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

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        default=datetime.now
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "calendario"
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

