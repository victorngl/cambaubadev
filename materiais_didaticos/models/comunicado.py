from typing import OrderedDict
from django.db import models
from datetime import datetime
from crum import get_current_user
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

    foto = models.ImageField(
        verbose_name='Foto',  
        null=True,
        blank=True
    ) 

    foto_capa = models.ImageField(
        verbose_name='Foto de Capa',  
        null=True,
        blank=True
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

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        super(Comunicado, self).save(*args, **kwargs)

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
        ordering = ["-id"]