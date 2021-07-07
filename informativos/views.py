from django.contrib.auth.models import User
from escolas.models.aluno import Aluno
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.views.generic import DetailView
from .models import Balancete, BalancoPatrimonial, DocumentacaoObra, AtaReuniao
from django.http import HttpResponseForbidden
from datetime import date

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
def grupo_de_pais_representantes(request):
    atas_reunioes = AtaReuniao.objects.all()
    alunos = Aluno.objects.all()
    responsaveis = []
    dados_responsaveis = []
    for aluno in alunos:
        if(aluno.responsavel1):
            responsaveis.append(aluno.responsavel1)
        if(aluno.responsavel2):
            responsaveis.append(aluno.responsavel2)
        if(aluno.responsavel3):
            responsaveis.append(aluno.responsavel3)
        if(aluno.responsavel4):
            responsaveis.append(aluno.responsavel4)
        if(aluno.responsavel5):
            responsaveis.append(aluno.responsavel5)

    for responsavel in responsaveis:
        dados = User.objects.get(username=responsavel)
        dados_responsaveis.append(dados)

    dados_responsaveis = list(set(dados_responsaveis))
    data_hoje = date.today()
    return render(
        request,
        'grupo_de_pais_representantes.html',
        {
            'data_hoje': data_hoje,
            'atas_reunioes': atas_reunioes,
            'dados_responsaveis' : dados_responsaveis
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