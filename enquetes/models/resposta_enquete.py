from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from djrichtextfield.models import RichTextField
from .enquete import Enquete
from crum import get_current_user


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

    opcao = models.CharField(
        verbose_name="Opção escolhida:",
        max_length=1,
        choices=OPCOES_ENQUETE,
        blank=True, null=True
    )

    usuario_votante = models.ForeignKey(
        User,
        related_name='%(class)s_requests_created',
        on_delete=models.SET_NULL,
        blank=True,null=True,
        default=None,
        verbose_name="Usuário votante"
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
        return str(self.id)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_votante = user
        super(RespostaEnquete, self).save(*args, **kwargs)
        
    class Meta:
        app_label = "enquetes"
        verbose_name = "Resposta da Enquete"
        verbose_name_plural = "Respostas da Enquete"