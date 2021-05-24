from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.views.generic import DetailView
from .models import Balancete, BalancoPatrimonial, DocumentacaoObra, AtaReuniao
from django.http import HttpResponseForbidden

@permission_required("core.pode_acessar_informativos")
def balancetes(request):
    balancetes = Balancete.objects.all()
    return render(
        request,
        'balancetes_list.html',
        {
            'balancetes': balancetes
        }
    )

@permission_required("core.pode_acessar_informativos")
def balancos_patrimoniais(request):
    balancos_patrimoniais = BalancoPatrimonial.objects.all()
    return render(
        request,
        'balancos_patrimoniais_list.html',
        {
            'balancos_patrimoniais': balancos_patrimoniais
        }
    )

@permission_required("core.pode_acessar_informativos")
def documentacoes_obras(request):
    documentacoes_obras = DocumentacaoObra.objects.all()
    return render(
        request,
        'documentacoes_obras_list.html',
        {
            'documentacoes_obras': documentacoes_obras
        }
    )

@permission_required("core.pode_acessar_informativos")
def atas_reunioes(request):
    atas_reunioes = AtaReuniao.objects.all()
    return render(
        request,
        'atas_reunioes_list.html',
        {
            'atas_reunioes': atas_reunioes
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