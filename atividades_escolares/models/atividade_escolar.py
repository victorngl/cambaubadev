from django.db import models
from datetime import datetime
from escolas.models import Turma, Materia

class AtividadeEscolar(models.Model):
    """
       Classe AtividadeEscolar implementa as funções relacionadas a uma atividade escolar na plataforma.
    """

    titulo = models.CharField(
		max_length=250,
		verbose_name="Título",
		help_text="Campo Obrigatório*"
	)

    descricao = models.TextField(
        verbose_name="Descrição",
        blank=True, null=True
    )

    horario_inicio = models.CharField(
		max_length=250,
		verbose_name="Horário de Início",
        blank=True
	)

    horario_fim = models.CharField(
		max_length=250,
		verbose_name="Horário de Fim",
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
    
    anexo = models.FileField(
        verbose_name="Anexo",
        upload_to ='uploads/',
        blank=True
    )

    turmas = models.ManyToManyField(
        Turma,
        verbose_name=("Turmas"),
        blank=True
    )

    materia = models.ForeignKey(
        Materia,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Matéria"
    )

    data_alteracao = models.DateTimeField(
        verbose_name="Data de Alteração",
        auto_now=True
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = "atividades_escolares"
        verbose_name = "Atividade Escolar"
        verbose_name_plural = "Atividades Escolares"