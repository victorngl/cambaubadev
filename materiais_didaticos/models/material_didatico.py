from django.db import models
from datetime import datetime
from escolas.models import Turma, Materia
from .tipo_material_didatico import TipoMaterialDidatico
class MaterialDidatico(models.Model):
    """
       Classe MaterialDidatico implementa as funções relacionadas a um material didático na plataforma.
    """

    titulo = models.CharField(
		max_length=250,
		verbose_name="Título",
		help_text="Campo Obrigatório*"
	)

    tipo = models.ForeignKey(
        TipoMaterialDidatico,
        verbose_name="Tipo",
        on_delete=models.SET_NULL,
        null=True,
    )

    materia = models.ForeignKey(
        Materia,
        verbose_name="Materia",
        on_delete=models.SET_NULL,
        null=True,
    )

    data = models.DateField(
        verbose_name='Data',
        blank=True, null=True
    )

    descricao = models.TextField(
        verbose_name="Descrição",
        blank=True, null=True
    )

    turmas = models.ManyToManyField(
        Turma,
        verbose_name=("Turmas"),
        blank=True
    )
    
    anexo = models.FileField(
        verbose_name="Anexo",
        upload_to ='uploads/',
        blank=True
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

    def __str__(self):
        return self.titulo

    @property
    def turmas_vinculadas(self):
        turmas_formatadas=""
        for turma in self.turmas.all():
            turmas_formatadas+="{} ".format(turma)
            
        return (turmas_formatadas)
        
    class Meta:
        app_label = "materiais_didaticos"
        verbose_name = "Material Didático"
        verbose_name_plural = "Materiais Didáticos"