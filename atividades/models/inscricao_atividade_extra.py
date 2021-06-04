from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from django.db.models import fields
from .atividade_extra import AtividadeExtra
from escolas.models import Aluno
from django.core.exceptions import ValidationError
from crum import get_current_user

class InscricaoAtividadeExtra(models.Model):
    """
       Classe InscricaoAtividadeExtra implementa as funções relacionadas a inscrição de uma atividade extra na plataforma.
    """

    atividade_extra = models.ForeignKey(
		AtividadeExtra,
        on_delete=models.SET_NULL,
        null=True,
		verbose_name="Atividade Extra"
	)

    aluno = models.ForeignKey(
		Aluno,
        on_delete=models.SET_NULL,
        null=True,
		verbose_name="Aluno"
	)

    usuario_inscricao = models.ForeignKey(
		User,
        on_delete=models.SET_NULL,
        null=True,
		verbose_name="Usuário Inscrição"
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

    def validate_unique(self,exclude=None):
        try:
            super(InscricaoAtividadeExtra,self).validate_unique()
        except ValidationError as e:
            raise ValidationError("Não é possivel inscrever " + str(self.aluno) + " em " + str(self.atividade_extra) + " duas vezes!")

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_inscricao = user
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(InscricaoAtividadeExtra, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)    

    class Meta:
        app_label = "atividades"
        verbose_name = "Inscrição na Atividade Extra"
        verbose_name_plural = "Inscrições na Atividade Extra"
        unique_together = [['aluno', 'atividade_extra']]

    

