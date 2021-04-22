from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from .models import CalendarioAtividade, Comunicado, MaterialDidatico

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
def materiais_didaticos(request):
    materiais_didaticos = MaterialDidatico.objects.all()
    return render(
        request,
        'materiais_didaticos_list.html',
        {
            'materiais_didaticos': materiais_didaticos
        }
    )


class CalendariosAtividadesDetailView(DetailView):
    model = CalendarioAtividade

class ComunicadosDetailView(DetailView):
    model = Comunicado

class MateriaisDidaticosDetailView(DetailView):
    model = MaterialDidatico

class ComunicadoListView(ListView):
    model = Comunicado
    paginate_by = 10
    template_name='comunicados_list.html'
    
    def get_queryset(self):
        queryset = super(ComunicadoListView, self).get_queryset()
        return queryset