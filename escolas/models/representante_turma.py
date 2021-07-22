__author__ = "Francisco Flávio Nogueira da Silva"
__copyright__ = "Francisco Flávio Nogueira da Silva"
__credits__ = ["Nova Data"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Francisco Flávio Nogueira da Silva"
__email__ = "flavio.nogueira.profissional@gmail.com"
__status__ = "Production"

from .turma import Turma
from django.db import models

'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

class RepresentanteTurma(models.Model):
    '''
    Classe para implementar as funções relacionadas aos responsáveis das turmas
    '''

    turma = models.ForeignKey(
        Turma,
        verbose_name='Turma',
        null=True,
        on_delete=models.SET_NULL
    )

    pai_representante = models.CharField(
        verbose_name='Pai representante',
        max_length=70
    )

    aluno = models.CharField(
        verbose_name='Aluno',
        max_length=70,
        null=True
    )

    assinatura = models.EmailField(
        verbose_name='Assinatura',
        null=True
    )

    def __str__(self):
        return '{} - {}'.format(self.pai_representante, self.turma)
    
    class Meta:
        app_label='escolas'
        verbose_name='Representante de turma'
        verbose_name_plural='Representantes de turma'