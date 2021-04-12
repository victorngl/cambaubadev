from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import Balancete, BalancoPatrimonial, DocumentacaoObra, AtaReuniao

@login_required
def balancetes(request):
    balancetes = Balancete.objects.all()
    return render(
        request,
        'balancetes_list.html',
        {
            'balancetes': balancetes
        }
    )

@login_required
def balancos_patrimoniais(request):
    balancos_patrimoniais = BalancoPatrimonial.objects.all()
    return render(
        request,
        'balancos_patrimoniais_list.html',
        {
            'balancos_patrimoniais': balancos_patrimoniais
        }
    )

@login_required
def documentacoes_obras(request):
    documentacoes_obras = DocumentacaoObra.objects.all()
    return render(
        request,
        'documentacoes_obras_list.html',
        {
            'documentacoes_obras': documentacoes_obras
        }
    )
@login_required
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

class BalancoPatrimonialDetailView(DetailView):
    model = BalancoPatrimonial

class DocumentacaoObraDetailView(DetailView):
    model = DocumentacaoObra

class AtaReuniaoDetailView(DetailView):
    model = AtaReuniao