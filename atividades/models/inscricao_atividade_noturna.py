from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .atividade_noturna import AtividadeNoturna
from escolas.models import Aluno
from crum import get_current_user

class InscricaoAtividadeNoturna(models.Model):
    """
       Classe InscricaoAtividadeNoturna implementa as funções relacionadas a inscrição em atividade noturna na plataforma.
    """

    atividade_noturna = models.ForeignKey(
		AtividadeNoturna,
        on_delete=models.SET_NULL,
        null=True,
		verbose_name="Atividade Noturna"
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

    def validate_unique(self,exclude=None):
        try:
            super(InscricaoAtividadeNoturna,self).validate_unique()
        except ValidationError as e:
            raise ValidationError("Não é possivel inscrever " + str(self.aluno) + " em " + str(self.atividade_noturna) + " duas vezes!")

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_inscricao = user
        super(InscricaoAtividadeNoturna, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = "atividades"
        verbose_name = "Inscrição na Atividade Noturna"
        verbose_name_plural = "Inscrições na Atividade Noturna"
        unique_together = [['aluno', 'atividade_noturna']]