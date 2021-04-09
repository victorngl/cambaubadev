from django.db import models
from datetime import datetime
from django.contrib.auth.models import Group

class Enquete(models.Model):
    """
       Classe Enquete implementa as funções relacionadas a uma enquete na plataforma.
    """

    titulo = models.CharField(
		max_length=300,
		verbose_name="Título",
		help_text="Campo Obrigatório*"
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

    data_expiracao = models.DateField(
        verbose_name="Data de Expiração",
        blank=True, null=True
    )

    mostrar_resultado = models.BooleanField(
        verbose_name="Mostrar Resultado",
        default=False
    )

    qtd_votos_permitidos = models.IntegerField(
		verbose_name="Quantidade de Votos Permitidos",
        default=1,
		blank=True, null=True
	)

    grupo_usuarios = models.ManyToManyField(
        Group,
        verbose_name='Grupo de Usuários',
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

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = "enquetes"
        verbose_name = "Enquete"
        verbose_name_plural = "Enquetes"