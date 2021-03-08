from django.db import models
from datetime import datetime
from escolas.models import Escola


class Balancete(models.Model):
    """
       Classe Balancete implementa as funções relacionadas a um balancete na plataforma.
    """

    titulo = models.CharField(
		max_length=300,
		verbose_name="Título",
		help_text="Campo Obrigatório*"
	)

    data = models.DateField(
        verbose_name="Data",
        blank=True,
        null=True
    )

    descricao = models.TextField(
		verbose_name="Descrição",
		blank=True, null=True
	)
    
    anexo = models.FileField(
        verbose_name="Anexo",
        upload_to ='uploads/',
        blank=True
    )

    escola = models.ForeignKey(
        Escola,
        on_delete=models.SET_NULL,
        verbose_name='Escola',
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

    class Meta:
        app_label = "informativos"
        verbose_name = "Balancete"
        verbose_name_plural = "Balancetes"