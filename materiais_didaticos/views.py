from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import AtaReuniao, CalendarioAtividade, Comunicado, MaterialDidatico

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

@login_required
def calendarios_atividades(request):
    calendarios_atividades = CalendarioAtividade.objects.all()
    return render(
        request,
        'calendarios_atividades_list.html',
        {
            'calendarios_atividades': calendarios_atividades
        }
    )

@login_required
def comunicados(request):
    comunicados = Comunicado.objects.all()
    return render(
        request,
        'comunicados_list.html',
        {
            'comunicados': comunicados
        }
    )

@login_required
def materiais_didaticos(request):
    materiais_didaticos = MaterialDidatico.objects.all()
    return render(
        request,
        'materiais_didaticos_list.html',
        {
            'materiais_didaticos': materiais_didaticos
        }
    )

class AtasReunioesDetailView(DetailView):
    model = AtaReuniao

class CalendariosAtividadesDetailView(DetailView):
    model = CalendarioAtividade

class ComunicadosDetailView(DetailView):
    model = Comunicado

class MateriaisDidaticosDetailView(DetailView):
    model = MaterialDidatico