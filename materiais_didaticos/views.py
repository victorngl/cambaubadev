from materiais_didaticos.models import comunicado
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.views.generic import DetailView, ListView
from django.http import JsonResponse, HttpResponseForbidden
from escolas.models import Materia
from .models import CalendarioAtividade, Comunicado, MaterialDidatico
from escolas.models import Aluno
from django.db.models import Q

@permission_required("core.pode_acessar_materiais_didaticos")
def calendarios_atividades(request):
    calendarios_atividades = CalendarioAtividade.objects.all()
    return render(
        request,
        'calendarios_atividades_list.html',
        {
            'calendarios_atividades': calendarios_atividades
        }
    )


@permission_required("core.pode_acessar_materiais_didaticos")
def get_calendarios_atividades(request):
    calendarios_atividades = CalendarioAtividade.objects.all()

    list_eventos = [
        {
            'id': evento.id, 
            'title': evento.nome,
            #'start': '{}T{}'.format(evento.data_inicial, evento.hora_inicio),
            'start': evento.data_inicial,
            #'end': '{}T{}'.format(evento.data_final, evento.hora_termino)
            'end': evento.data_final
        } for evento in calendarios_atividades
    ]
    
    return JsonResponse(list_eventos, safe=False)

@permission_required("core.pode_acessar_materiais_didaticos")
def materiais_didaticos(request):
    materiais_didaticos = MaterialDidatico.objects.all()
    materias = Materia.objects.all()
    materia = request.GET.get('materia', '')
    materiais_didaticos = materiais_didaticos.filter(materia__id=materia) if materia else materiais_didaticos
    
    return render(
        request,
        'materiais_didaticos_list.html',
        {
            'materias': materias,
            'materiais_didaticos': materiais_didaticos
        }
    )


class CalendariosAtividadesDetailView(DetailView):
    model = CalendarioAtividade
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('core.pode_acessar_materiais_didaticos'):
            return super(CalendariosAtividadesDetailView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

class ComunicadosDetailView(DetailView):
    model = Comunicado
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('core.pode_acessar_materiais_didaticos'):
            return super(ComunicadosDetailView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

class MateriaisDidaticosDetailView(DetailView):
    model = MaterialDidatico
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('core.pode_acessar_materiais_didaticos'):
            return super(MateriaisDidaticosDetailView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

class ComunicadoListView(ListView):
    model = Comunicado
    paginate_by = 10
    template_name='comunicados_list.html'
    
    def get_queryset(self):
        queryset = super(ComunicadoListView, self).get_queryset().order_by('-data_alteracao').distinct()
        if self.request.user.profile:
            queryset = queryset.filter(
                turmas__in = self.request.user.profile.turmas
            ).order_by('-data_alteracao')
        return queryset

    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('core.pode_acessar_materiais_didaticos'):
            return super(ComunicadoListView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()