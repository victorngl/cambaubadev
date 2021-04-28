from django.db import models
from datetime import datetime
from colorfield.fields import ColorField

class Materia(models.Model):
    """
       Classe Materia implementa as funções relacionadas a uma materia na plataforma.
    """

    titulo = models.CharField(
        verbose_name="Título",
        max_length=200
    )

    hexadecimal = ColorField(
        default='#FF0000', 
        format='hexa'
    )

    data_alteracao = models.DateTimeField(
        verbose_name="Data de Alteração",
        auto_now=True
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        auto_now_add=True
    )

    foto_capa = models.ImageField(
        verbose_name='Foto de Capa',  
        null=True
    )
    
    def __str__(self):
        return self.titulo

    class Meta:
        app_label="escolas"
        verbose_name="Matéria"
        verbose_name_plural="Matérias"
