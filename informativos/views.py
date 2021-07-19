from escolas.models.turma import Turma
from core.models.profile import Profile
from django.contrib.auth.models import User
from escolas.models.aluno import Aluno
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.views.generic import DetailView
from .models import Balancete, BalancoPatrimonial, DocumentacaoObra, AtaReuniao
from django.http import HttpResponseForbidden
from datetime import date
from django.db.models import Q
import itertools

@permission_required("core.pode_acessar_informativos")
def balancetes(request):
    balancetes = Balancete.objects.all()
    data_hoje = date.today()
    return render(
        request,
        'balancetes_list.html',
        {
            'data_hoje': data_hoje,
            'balancetes': balancetes
        }
    )

@permission_required("core.pode_acessar_informativos")
def balancos_patrimoniais(request):
    balancos_patrimoniais = BalancoPatrimonial.objects.all()
    data_hoje = date.today()
    return render(
        request,
        'balancos_patrimoniais_list.html',
        {
            'data_hoje' : data_hoje,
            'balancos_patrimoniais': balancos_patrimoniais
        }
    )

@permission_required("core.pode_acessar_informativos")
def documentacoes_obras(request):
    documentacoes_obras = DocumentacaoObra.objects.all()
    data_hoje = date.today()
    return render(
        request,
        'documentacoes_obras_list.html',
        {
            'data_hoje' : data_hoje,
            'documentacoes_obras': documentacoes_obras
        }
    )

@permission_required("core.pode_acessar_informativos")
def atas_reunioes(request):
    atas_reunioes = AtaReuniao.objects.all()
    data_hoje = date.today()
    return render(
        request,
        'atas_reunioes_list.html',
        {
            'data_hoje': data_hoje,
            'atas_reunioes': atas_reunioes
        }
    )



@permission_required("core.pode_acessar_informativos")
def contato_representantes(request):
    responsaveis = Aluno.objects.all().filter(
        Q(responsavel1__email__isnull=False)|  
        Q(responsavel2__email__isnull=False)|  
        Q(responsavel3__email__isnull=False)|  
        Q(responsavel4__email__isnull=False) 
        ).values_list(
            'responsavel1__email',
            'responsavel2__email',
            'responsavel3__email',
            'responsavel4__email'
        ).distinct()
    usuarios = User.objects.all()
    nome_completo = []
    dados = [{

    }]
    email_responsaveis = Turma.objects.all()
    list_responsaveis = list(itertools.chain(*responsaveis))
    list_responsaveis = set(list_responsaveis)
    lista_dos_responsaveis = []

    for email_responsavel in email_responsaveis:
        for email in list_responsaveis:
            if(email != None):
                if(email_responsavel.email_pai_responsavel == email):
                    lista_dos_responsaveis.append(email_responsavel)
                    dados.append(
                         {'turma' : email_responsavel.nome,
                          'nome' : User.objects.all().get(email=email),
                          'email' : email,
                         }
                    )

    return render(
        request,
        'contato_email.html',
        {
            'dados_responsaveis' : dados,
        }
    )

class BalancetesDetailView(DetailView):
    model = Balancete
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('core.pode_acessar_informativos'):
            return super(BalancetesDetailView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

class BalancoPatrimonialDetailView(DetailView):
    model = BalancoPatrimonial
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('core.pode_acessar_informativos'):
            return super(BalancoPatrimonialDetailView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

class DocumentacaoObraDetailView(DetailView):
    model = DocumentacaoObra
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('core.pode_acessar_informativos'):
            return super(DocumentacaoObraDetailView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

class AtaReuniaoDetailView(DetailView):
    model = AtaReuniao
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('core.pode_acessar_informativos'):
            return super(AtaReuniaoDetailView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()