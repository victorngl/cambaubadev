from django.db import models
from datetime import datetime
from escolas.models import Turma, Materia
from crum import get_current_user

class CalendarioAtividade(models.Model):
    """
       Classe CalendarioAtividade implementa as funções relacionadas a um calendário de atividade na plataforma.
    """

    titulo = models.CharField(
		max_length=250,
		verbose_name="Título",
		help_text="Campo Obrigatório*"
	)

    descricao = models.TextField(
        verbose_name="Descrição",
        blank=True, null=True
    )

    data_inicial = models.DateTimeField(
        verbose_name="Data Inicial",
		blank=True, null=True
    )

    data_final = models.DateTimeField(
        verbose_name="Data Final",
		blank=True, null=True
    )

    turmas = models.ManyToManyField(
        Turma,
        verbose_name=("Turmas"),
        blank=True
    )
    
    materia = models.ForeignKey(
        Materia,
        verbose_name="Matéria",
		    help_text="Somente se for relacionado a uma matéria",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    foto = models.ImageField(
        verbose_name='Foto',   
        null=True, blank=True
    ) 

    foto_capa = models.ImageField(
        verbose_name='Foto de Capa',  
        null=True, blank=True
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

    def __str__(self):
        return self.titulo
        
    @property
    def turmas_vinculadas(self):
        turmas_formatadas=""
        for turma in self.turmas.all():
            turmas_formatadas+="{} ".format(turma)
            
        return (turmas_formatadas)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(CalendarioAtividade, self).save(*args, **kwargs)

    class Meta:
        app_label = "materiais_didaticos"
        verbose_name = "Calendário de Atividade"
        verbose_name_plural = "Calendário de Atividades"