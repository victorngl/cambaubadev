from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from atividades.models import Oficina
from crum import get_current_user
from escolas.models import Aluno


class InscricaoOficina(models.Model):
    """
       Classe InscricaoOficina implementa as funções relacionadas a inscrição na oficina na plataforma.
    """

    oficina = models.ForeignKey(
        Oficina,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Oficina"
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
        verbose_name="Usuário inscrito"
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
            super(InscricaoOficina,self).validate_unique()
        except ValidationError as e:
            raise ValidationError("Não é possivel inscrever " + str(self.aluno) + " em " + str(self.oficina) + " duas vezes!")


    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_inscricao = user
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(InscricaoOficina, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = "atividades"
        verbose_name = "Inscrição na Oficina"
        verbose_name_plural = "Inscrições na Oficina"
        unique_together = [['aluno', 'oficina']]