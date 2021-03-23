from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from atividades.models import Oficina
from escolas.models import Aluno
from crum import get_current_user

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

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_inscricao = user
        super(InscricaoOficina, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = "atividades"
        verbose_name = "Inscrição na Oficina"
        verbose_name_plural = "Inscrições na Oficina"