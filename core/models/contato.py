__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2020, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from crum import get_current_user

class Contato(models.Model):
	"""
	Classe Contato implementa as funções relacionadas a um contato de um cliente na plataforma.
	"""

	nome = models.CharField(
		max_length=200,
		verbose_name="Nome"
	)

	email = models.EmailField(
		max_length=200,
		verbose_name="E-mail",
		blank=True
	)

	telefone = models.CharField(
		max_length=30,
		verbose_name="Telefone",
		blank=True
	)

	celular = models.CharField(
		max_length=30,
		verbose_name="Celular",
		blank=True
	)

	ativo = models.BooleanField(
		verbose_name="Ativo",
		default=True
	)

	observacoes = models.TextField(
		verbose_name="Observações",
		blank=True
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

	def __str__(self):
		return self.nome

	def save(self, *args, **kwargs):
		user = get_current_user()
		if user and not user.pk:
			user = None
		if not self.pk:
			self.usuario_criacao = user
		self.usuario_atualizacao = user
		super(Contato, self).save(*args, **kwargs)

	class Meta:
		app_label = "core"
		verbose_name = "Contato"
		verbose_name_plural = "Contatos"

