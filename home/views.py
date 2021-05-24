from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator
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
        pagina_atual = request.GET.get('page', 1)
        alunos = None
        enquetes = None
        aluno = None
        materiais_didaticos = None
        comunicados = []
        paginacao_comunicados = None
        if request.user.profile:
            perfil = request.user.profile.perfil
            if perfil == 'Aluno':
                aluno=Aluno.objects.get(usuario=request.user)
                template_name = 'home_aluno.html'

                comunicados = aluno.turma.comunicado_set.all().order_by('-id')
                paginacao_comunicados = Paginator(comunicados, 2)
                pagina_atual = paginacao_comunicados.page(pagina_atual)
            elif perfil == 'Responsável' or perfil == 'Professor/Responsavel':
                alunos=Aluno.objects.filter(
                    Q(responsavel1=request.user) | 
                    Q(responsavel2=request.user) | 
                    Q(responsavel3=request.user) | 
                    Q(responsavel4=request.user) | 
                    Q(responsavel5=request.user)
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
            'hoje': date.today(),
            'paginacao_comunicados': paginacao_comunicados,
            'pagina_atual': pagina_atual
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
    try:
        calendarios_atividades = CalendarioAtividade.objects.filter(
            turmas__in=request.user.profile.turmas
        )
    except:
        calendarios_atividades = CalendarioAtividade.objects.all()
    
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
    
    return JsonResponse(list_eventos, safe=False)
