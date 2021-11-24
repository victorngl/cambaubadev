from django.db import models
from datetime import datetime
from escolas.models import Turma
from crum import get_current_user
from django.utils import timezone

class AtividadeExtra(models.Model):
	"""
	   Classe AtividadeExtra implementa as funções relacionadas a uma atividade extra na plataforma.
	"""

	titulo = models.CharField(
		max_length=250,
		verbose_name="Título",
		help_text="Campo Obrigatório*"
	)

	vagas = models.IntegerField(
		verbose_name="Vagas",
		blank=True, null=True
	)

	horario = models.CharField(
		max_length=250,
		verbose_name="Horário",
		blank=True
	)
	
	data_inicial = models.DateField(
		verbose_name="Data Inicial",
		blank=True, null=True
	)

	data_final = models.DateField(
		verbose_name="Data Final",
		blank=True, null=True
	)
	
	inicio_inscricoes = models.DateTimeField(
		verbose_name="Início das Inscrições",
		blank=False, null=True
	)
	
	fim_inscricoes = models.DateTimeField(
		verbose_name="Fim das Inscrições",
		blank=False, null=True
	)

	descricao = models.TextField(
		verbose_name="Descrição",
		blank=True, null=True
	)

	turmas = models.ManyToManyField(
		Turma,
		verbose_name=("Turmas"),
		blank=True
	)
	
	foto = models.ImageField(
		verbose_name='Foto',  
		null=True, blank=True
	) 

	foto_capa = models.ImageField(
		verbose_name='Foto de Capa',  
		null=True, blank=True
	) 

	data_alteracao = models.DateTimeField(
		verbose_name="Data de Alteração",
		auto_now=True
	)

	data_criacao = models.DateTimeField(
		verbose_name="Data de Criação",
		auto_now_add=True
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
	def inscricoes_abertas(self):
		try:
			if self.inicio_inscricoes <= timezone.now() <= self.fim_inscricoes:
				return True
			else: 
				return False
		except:
			return True

	@property
	def quantidade_inscritos(self):
		return self.inscricaoatividadeextra_set.all().count()

	def __str__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		user = get_current_user()
		if user and not user.pk:
			user = None
		if not self.pk:
			self.usuario_criacao = user
		self.usuario_atualizacao = user
		super(AtividadeExtra, self).save(*args, **kwargs)
	class Meta:
		app_label = "atividades"
		verbose_name = "Atividade Extra"
		verbose_name_plural = "Atividades Extras"