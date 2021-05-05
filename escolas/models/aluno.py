from django.db import models
from django.contrib.auth.models import User, Group
from datetime import datetime
from core.models import Pessoa
from .turma import Turma

class Aluno(Pessoa):
    """
       Classe Aluno implementa as funções relacionadas a um aluno na plataforma.
    """

    qtd_atividades_permitidas = models.IntegerField(
		verbose_name="Quantidade de Atividades Permitidas",
        default=1,
		blank=True, null=True
	)

    foto = models.ImageField(
        verbose_name='Foto',  
        null=True,  blank=True
    )

    turma = models.ForeignKey(
        Turma,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Turma"
    )

    usuario = models.ForeignKey(
        User,
        verbose_name="Usuário do Aluno",
        related_name="usuario_aluno",
        on_delete=models.SET_NULL,
        unique=True,
        blank=True,
        null=True
    )

    responsavel1 = models.ForeignKey(
        User,
        verbose_name="Responsável 1",
        related_name="responsavel1_aluno",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    responsavel2 = models.ForeignKey(
        User,
        verbose_name="Responsável 2",
        related_name="responsavel2_aluno",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    responsavel3 = models.ForeignKey(
        User,
        verbose_name="Responsável 3",
        related_name="responsavel3_aluno",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    responsavel4 = models.ForeignKey(
        User,
        verbose_name="Responsável 4",
        related_name="responsavel4_aluno",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    responsavel5 = models.ForeignKey(
        User,
        verbose_name="Responsável 5",
        related_name="responsavel5_aluno",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    observacao = models.TextField(
		verbose_name="Observação",
		blank=True, null=True
	)

    matricula = models.CharField(
        max_length=200,
        verbose_name="Matrícula",
        blank=True, null=True
    )

    id_sigma = models.CharField(
        max_length=200,
        verbose_name="ID Sigma",
        blank=True, null=True
    )

    username = models.CharField(
        max_length=200,
        verbose_name="Usuário",
        unique=True,
        blank=True, null=True
    )

    senha = models.CharField(
        max_length=200,
        verbose_name="Senha",
        blank=True, null=True
    )

    def sincronizar_aluno(self):
        from core.models import Profile
        if self.username and not self.usuario:
            novo_usuario = User.objects.create(
                username=self.username
            )
            novo_usuario.set_password(self.senha)
            novo_usuario.save()

            grupo_professor = Group.objects.get(name='Aluno') 
            grupo_professor.user_set.add(novo_usuario)

            self.usuario = novo_usuario
            self.save()

            novo_profile = Profile.objects.create(
                user=novo_usuario,
                id_sigma=self.id_sigma
            )

    def __str__(self):
        return self.nome

    class Meta:
        app_label="escolas"
        verbose_name="Aluno"
        verbose_name_plural="Alunos"
