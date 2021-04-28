from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from escolas.models import Aluno, Turma
from enquetes.models import Enquete
from django.db.models import Q
from django.http import JsonResponse
from datetime import datetime, date
from materiais_didaticos.models import CalendarioAtividade
from atividades_escolares.models import AtividadeEscolar

@login_required
def home(request):
    try:
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
                aluno=Aluno.objects.filter(
                    Q(nome=request.user)  
                )
                template_name = 'home.html'
    except:
        template_name = 'home.html'
        

    return render(
        request,
        template_name,
        {   
            'aluno': aluno,
            'enquetes': enquetes,
            'perfil': perfil,
            'alunos': alunos,
            'hoje': date.today()
        }
    )

@permission_required("core.pode_acessar_boletos_boletins")
def gerar_boletos_boletins(request):
    try:
        request.user.profile.id_sigma
        return render(
            request,
            'boletos_boletins.html',
            {}
        )
    except:
        return HttpResponseForbidden()


@login_required
def get_calendario(request):
    calendarios_atividades = CalendarioAtividade.objects.all()
    atividades_escolares = AtividadeEscolar.objects.all()

    list_eventos = [
        {
            'id': evento.id, 
            'title': evento.titulo,
            'start': evento.data_inicial,
            'end': evento.data_final,
            'materia': evento.materia.titulo,
            'descricao': evento.descricao
        } for evento in calendarios_atividades
    ]
    '''
    list_eventos_atividades_escolares = [
        {
            'id': evento.id, 
            'title': evento.titulo,
            #'start': '{}T{}'.format(evento.data_inicial, evento.hora_inicio),
            'start': evento.data_inicial,
            #'end': '{}T{}'.format(evento.data_final, evento.hora_termino)
            'end': evento.data_final
        } for evento in atividades_escolares
    ]

    list_eventos = list_eventos_calendario_atividades + list_eventos_atividades_escolares
    '''
    return JsonResponse(list_eventos, safe=False)
