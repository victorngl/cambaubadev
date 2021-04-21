from django.db import models
from datetime import datetime
from escolas.models import Turma
from django_quill.fields import QuillField

class Comunicado(models.Model):
    """
       Classe Comunicado implementa as funções relacionadas a um comunicado na plataforma.
    """

    titulo = models.CharField(
		max_length=250,
		verbose_name="Título",
		help_text="Campo Obrigatório*"
	)

    data = models.DateField(
        verbose_name="Data",
		blank=True, null=True
    )
    
    resumo = QuillField(
        verbose_name='Resumo',
        blank=False, null=True
    )
    descricao = QuillField(
        verbose_name="Descrição",
        blank=True, null=True
    )

    turmas = models.ManyToManyField(
        Turma,
        verbose_name=("Turmas"),
        blank=True
    )
    
    anexo = models.FileField(
        verbose_name="Anexo",
        upload_to ='uploads/',
        blank=True
    )

    retrato = models.ImageField(
        verbose_name='Retrato',  
        null=True
    ) 

    foto_capa = models.ImageField(
        verbose_name='Foto de Capa',  
        null=True
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
    
    @property
    def turmas_vinculadas(self):
        turmas_formatadas=""
        for turma in self.turmas.all():
            turmas_formatadas+="{} ".format(turma)
            
        return (turmas_formatadas)

    class Meta:
        app_label = "materiais_didaticos"
        verbose_name = "Comunicado"
        verbose_name_plural = "Comunicados"