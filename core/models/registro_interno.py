__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2020, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from crum import get_current_user


class RegistroInterno(models.Model):
	"""
	Classe Registro Interno realiza um registro interno de mensagens/observações no sistema.
	"""

	mensagem = models.TextField(
		verbose_name="Mensagem"
	)

	arquivo = models.FileField(
		verbose_name="Arquivo",
		upload_to='registro_interno/',
		blank=True
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
		auto_now_add=True
	)

	data_atualizacao = models.DateTimeField(
		verbose_name="Data de Atualização",
		auto_now=True
	)

	def save(self, *args, **kwargs):
		user = get_current_user()
		if user and not user.pk:
			user = None
		if not self.pk:
			self.usuario_criacao = user
		self.usuario_atualizacao = user
		super(RegistroInterno, self).save(*args, **kwargs)

	def __str__(self):
		return self.mensagem

	class Meta:
		app_label = "core"
		verbose_name = "Registro Interno"
		verbose_name_plural = "Registros Internos"
		ordering = ["-id"]

