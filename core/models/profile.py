from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Q
from escolas.models import Aluno, Professor


class Profile(models.Model):
    """
    Classe Profile implementa as funções relacionadas a um profile na plataforma.
    """

    id_sigma = models.CharField(
        max_length=200,
        verbose_name="ID Sigma",
        blank=True, null=True
    )

    user = models.OneToOneField(
		User, 
		on_delete=models.CASCADE
	)

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )

    data_atualizacao = models.DateTimeField(
        verbose_name="Data de Atualização",
        auto_now=True
    )

    @property
    def perfil(self):
        if Aluno.objects.filter(usuario=self.user).exists():
            return 'Aluno'
        elif Professor.objects.filter(usuario=self.user).exists():
            return 'Professor'
        else:
            alunos_responsaveis = Aluno.objects.filter(
                Q(responsavel1=self.user) | 
                Q(responsavel2=self.user) | 
                Q(responsavel3=self.user) | 
                Q(responsavel4=self.user) | 
                Q(responsavel5=self.user)
            ).exists()

            if alunos_responsaveis:
                return "Responsável"
            else:
                return "Sem vínculo"


    def __str__(self):
        return self.user.username

    class Meta:
        permissions = (
			('pode_acessar_materiais_didaticos', 'pode_acessar_materiais_didaticos'),
			('pode_acessar_boletos_boletins', 'pode_acessar_boletos_boletins'),
			('pode_acessar_enquetes', 'pode_acessar_enquetes'),
			('pode_acessar_atividades', 'pode_acessar_atividades'),
			('pode_acessar_atividades_escolares', 'pode_acessar_atividades_escolares'),
			('pode_acessar_informativos', 'pode_acessar_informativos')
		)
        app_label = "core"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

