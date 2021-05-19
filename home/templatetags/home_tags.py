from django import template
from django.db.models import Q
from escolas.models import Aluno, Turma, Professor
from crum import get_current_user
from django.db import connection
from datetime import date
 
register = template.Library()


@register.simple_tag()
def minha_turma():
    user = get_current_user()
    aluno = Aluno.objects.filter(
        usuario=user
    ).first()

    return aluno.turma

@register.simple_tag()
def minhas_turmas():
    user = get_current_user()
    alunos=Aluno.objects.filter(
        Q(responsavel1=user) | 
        Q(responsavel2=user) | 
        Q(responsavel3=user) | 
        Q(responsavel4=user) | 
        Q(responsavel5=user)
    )

    turmas = [
        aluno.turma for aluno in alunos
    ]

    turmas = list(set(turmas))

    return turmas

@register.simple_tag()
def minhas_turmas_professor():
    user = get_current_user()
    professor = Professor.objects.filter(
        usuario=user
    ).first()

    turmas = Turma.objects.filter(
        professores__in=[professor]
    )

    return turmas

@register.simple_tag()
def minhas_turmas_professor_responsavel():
    user = get_current_user()
    professor = Professor.objects.filter(
        usuario=user
    ).first()

    turmas_professor = Turma.objects.filter(
        professores__in=[professor]
    )

    alunos=Aluno.objects.filter(
        Q(responsavel1=user) | 
        Q(responsavel2=user) | 
        Q(responsavel3=user) | 
        Q(responsavel4=user) | 
        Q(responsavel5=user)
    )

    turmas = [
        aluno.turma for aluno in alunos
    ]

    for turma in turmas_professor:
        turmas.append(turma)

    turmas = list(set(turmas))

    return turmas

@register.simple_tag()
def meus_alunos():
    user = get_current_user()
    alunos=Aluno.objects.filter(
        Q(responsavel1=user) | 
        Q(responsavel2=user) | 
        Q(responsavel3=user) | 
        Q(responsavel4=user) | 
        Q(responsavel5=user)
    )

    return alunos

@register.simple_tag()
def index_aluno(alunos, aluno):
    for idx, obj in enumerate(alunos):
        if obj == aluno:
            index = idx + 1
            return index
        