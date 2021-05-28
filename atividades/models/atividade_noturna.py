from django.db import models
from datetime import datetime
from escolas.models import Turma

class AtividadeNoturna(models.Model):
	"""
	   Classe AtividadeNoturna implementa as funções relacionadas a uma atividade noturna na plataforma.
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

	@property
	def quantidade_inscritos(self):
		return self.inscricaoatividadenoturna_set.all().count()

	@property
	def inscricoes_abertas(self):
		try:
			if self.data_inicial < datetime.now().date() < self.data_final:
				return True
			else: 
				return False
		except:
			return True

	def __str__(self):
		return self.titulo

	class Meta:
		app_label = "atividades"
		verbose_name = "Atividade Noturna"
		verbose_name_plural = "Atividades Noturnas"