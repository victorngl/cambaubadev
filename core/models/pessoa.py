__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2020, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from crum import get_current_user


class Pessoa(models.Model):
	"""
	Classe Pessoa implementa as funções relacionadas a uma pessoa da plataforma.
	"""

	nome = models.CharField(
		max_length=200,
		verbose_name="Nome",
		help_text="Campo Obrigatório*"
	)

	is_empresa = models.BooleanField(
		verbose_name="É uma empresa?",
		default=False
	)

	cpf_cnpj = models.CharField(
		max_length=18,
		verbose_name="CPF/CNPJ",
		unique=True,
		blank=True, null=True
	)

	rg = models.CharField(
		max_length=30,
		verbose_name="RG",
		blank=True,
		null=True
	)

	telefone = models.CharField(
		max_length=30,
		verbose_name="Telefone",
		blank=True,
		null=True
	)

	celular = models.CharField(
		max_length=30,
		verbose_name="Celular",
		blank=True, null=True
	)

	email = models.EmailField(
		max_length=150,
		verbose_name="Email",
		blank=True, null=True
	)

	user = models.OneToOneField(
		User,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		verbose_name="User"
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
		super(Pessoa, self).save(*args, **kwargs)

	class Meta:
		app_label = "core"
		verbose_name = "Pessoa"
		verbose_name_plural = "Pessoas"

