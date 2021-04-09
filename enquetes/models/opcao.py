from django.db import models
from datetime import datetime
from django_quill.fields import QuillField
from .enquete import Enquete

class Opcao(models.Model):
    """
       Classe Opcao implementa as funções relacionadas a uma opção na plataforma.
    """

    titulo = QuillField(
        verbose_name = "Título"
    )

    enquete = models.ForeignKey(
        Enquete,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Enquete"
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
        return str(self.titulo)

    class Meta:
        app_label = "enquetes"
        verbose_name = "Opção"
        verbose_name_plural = "Opções"