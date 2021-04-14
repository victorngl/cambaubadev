from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from escolas.models import Aluno, Turma
from enquetes.models import Enquete
from django.db.models import Q

@login_required
def home(request):
    perfil = 'Sem Vínculo'
    alunos = None
    enquetes = None
    aluno = None
    materiais_didaticos = None
    if request.user.profile:
        perfil = request.user.profile.perfil
        if perfil == 'Aluno':
            aluno=Aluno.objects.get(usuario=request.user)
            template_name = 'home_aluno.html'
        elif perfil == 'Responsável':
            alunos=Aluno.objects.filter(
                Q(responsavel1=request.user) | 
                Q(responsavel2=request.user) | 
                Q(responsavel3=request.user)
            )
            enquetes = Enquete.objects.all()
            template_name = 'home_responsavel.html'
        else:
            aluno=Aluno.objects.filtar(
                Q(nome=request.user)  
            )
            template_name = 'home.html'

    return render(
        request,
        template_name,
        {   
            'aluno': aluno,
            'enquetes': enquetes,
            'perfil': perfil,
            'alunos': alunos
        }
    )

@login_required
def gerar_boletos_boletins(request):
    try:
        return render(
            request,
            'boletos_boletins.html',
            {}
        )
    except:
        return HttpResponseForbidden()