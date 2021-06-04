__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2020, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from .estado import Estado
from datetime import datetime
from crum import get_current_user

class Cidade(models.Model):
    """
    Classe Cidade implementa as funções relacionadas a uma cidade na plataforma.
    """

    nome = models.CharField(
        max_length=200,
        verbose_name="Nome"
    )

    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        verbose_name="Estado"
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name="Data de Atualização",
        auto_now=True
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

    @property
    def pais(self):
        return self.estado.pais

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(Cidade, self).save(*args, **kwargs)

    class Meta:
        app_label = "core"
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ['estado', 'nome']

