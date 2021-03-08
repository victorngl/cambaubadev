from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from .enquete import Enquete


class RespostaEnquete(models.Model):
    """
       Classe RespostaEnquete implementa as funções relacionadas a resposta de enquete na plataforma.
    """
    
    OPCOES_ENQUETE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    )

    usuario_inscricao = models.ForeignKey(
		User,
        on_delete=models.SET_NULL,
        null=True,
		verbose_name="Usuário Inscrição"
	)

    enquete = models.ForeignKey(
		Enquete,
        on_delete=models.SET_NULL,
        null=True,
		verbose_name="Enquete"
	)

    opcao = models.CharField(
        verbose_name="Opção escolhida:",
        max_length=1,
        choices=OPCOES_ENQUETE,
        blank=True, null=True
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
        return str(self.id)

    class Meta:
        app_label = "enquete"
        verbose_name = "Resposta da Enquete"
        verbose_name_plural = "Respostas da Enquete"