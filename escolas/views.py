from django.shortcuts import render, get_object_or_404
from .models import Turma
from materiais_didaticos.models import Comunicado
from atividades_escolares.models import AtividadeEscolar
from materiais_didaticos.models import MaterialDidatico
from django.views.generic import DetailView
from django.db.models import Q
from datetime import date

class TurmaDetailView(DetailView):
    model = Turma

    def get_context_data(self, **kwargs):
        context = super(TurmaDetailView, self).get_context_data(**kwargs)
        turma = get_object_or_404(Turma, pk=self.kwargs['pk'])
        comunicados = Comunicado.objects.filter(turmas=turma)
        atividades_escolares = AtividadeEscolar.objects.filter(
            Q(turmas=turma) &
            Q(data_final__gte=date.today())
        ).order_by('data_final')
        materiais_didaticos = MaterialDidatico.objects.filter(
            Q(turmas=turma) &
            Q(data__gte=date.today())
        ).order_by('data')
        print(materiais_didaticos)
        context.update(
            {
                'comunicados': comunicados,
                'atividades_escolares': atividades_escolares,
                'materiais_didaticos': materiais_didaticos
            }
        )
        return context
