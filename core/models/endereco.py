__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2020, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from .pessoa import Pessoa
from .cidade import Cidade
from .estado import Estado
from .pais import Pais
from core.managers import EnderecoManager
from datetime import datetime
from crum import get_current_user


class Endereco(models.Model):
	"""
	Classe Endereco implementa as funções relacionadas a um endereço na plataforma.
	"""

	logradouro = models.CharField(
		max_length=200,
		verbose_name="Logradouro",
		help_text="Campo Obrigatório*"
	)

	complemento = models.CharField(
		max_length=100,
		verbose_name="Complemento",
		blank=True
	)

	numero = models.CharField(
		max_length=10,
		verbose_name="Número",
		help_text="Campo Obrigatório*"
	)

	bairro = models.CharField(
		max_length=200,
		verbose_name="Bairro",
		help_text="Campo Obrigatório*"
	)

	cep = models.CharField(
		max_length=9,
		verbose_name="CEP",
		help_text="Campo Obrigatório*"
	)

	cidade = models.CharField(
		max_length=200,
		null=True,
		verbose_name="Cidade",
		help_text="Campo Obrigatório*"
	)

	estado = models.CharField(
		max_length=200,
		null=True,
		verbose_name="Estado",
		help_text="Campo Obrigatório*"
	)

	pais = models.CharField(
		max_length=200,
		null=True,
		verbose_name="País",
		help_text="Campo Obrigatório*"
	)

	pessoa = models.OneToOneField(
		Pessoa,
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		verbose_name="Pessoa"
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

	objects = EnderecoManager()

	def __str__(self):
		return self.logradouro

	def save(self, *args, **kwargs):
		user = get_current_user()
		if user and not user.pk:
			user = None
		if not self.pk:
			self.usuario_criacao = user
		self.usuario_atualizacao = user
		super(Endereco, self).save(*args, **kwargs)

	class Meta:
		app_label = "core"
		verbose_name = "Endereço"
		verbose_name_plural = "Endereços"

