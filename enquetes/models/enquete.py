from django.db import models
from datetime import datetime
from django_quill.fields import QuillField
from django.contrib.auth.models import Group
from crum import get_current_user

class Enquete(models.Model):
    """
       Classe Enquete implementa as funções relacionadas a uma enquete na plataforma.
    """

    titulo = models.CharField(
		max_length=300,
		verbose_name="Título",
		help_text="Campo Obrigatório*"
	)

    descricao = QuillField(
		verbose_name="Descrição",
        null=True,
        blank=True
	)
    
    anexo = models.FileField(
        verbose_name="Anexo",
        upload_to ='uploads/',
        blank=True
    )

    data_expiracao = models.DateField(
        verbose_name="Data de Expiração",
        blank=True, null=True
    )

    mostrar_resultado = models.BooleanField(
        verbose_name="Mostrar Resultado?",
        default=False
    )

    voto_unico = models.BooleanField(
		verbose_name="Voto Único Por Usuário?",
        default=True
	)

    grupo_usuarios = models.ManyToManyField(
        Group,
        verbose_name='Grupo de Usuários',
        blank=True
    )

    data_alteracao = models.DateTimeField(
        verbose_name="Data de Alteração",
        auto_now=True
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )
    
    foto = models.ImageField(
        verbose_name='Foto',  
        null=True, blank=True
    ) 

    foto_capa = models.ImageField(
        verbose_name='Foto de Capa',  
        null=True, blank=True
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

    @property
    def quantidade_respostas(self):
        from .resposta_enquete import RespostaEnquete
        
        quantidade = RespostaEnquete.objects.filter(
            enquete=self,
        ).count()
        
        return quantidade

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.usuario_criacao = user
        self.usuario_atualizacao = user
        super(Enquete, self).save(*args, **kwargs)

    class Meta:
        app_label = "enquetes"
        verbose_name = "Enquete"
        verbose_name_plural = "Enquetes"