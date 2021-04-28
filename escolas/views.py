from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Turma, Aluno
from materiais_didaticos.models import Comunicado
from atividades_escolares.models import AtividadeEscolar
from materiais_didaticos.models import MaterialDidatico
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import date

@login_required
def escolas(request):
    return render(request)

class AlunoDetailView(DetailView):
    model = Aluno

class TurmaDetailView(DetailView):
    model = Turma

    def get_context_data(self, **kwargs):
        context = super(TurmaDetailView, self).get_context_data(**kwargs)
        pagina_atual = self.request.GET.get('page', 1)
        turma = get_object_or_404(Turma, pk=self.kwargs['pk'])
        comunicados = Comunicado.objects.filter(turmas=turma).order_by('-id')
        atividades_escolares = AtividadeEscolar.objects.filter(
            Q(turmas=turma) &
            Q(data_final__gte=date.today())
        ).order_by('data_final')
        materiais_didaticos = MaterialDidatico.objects.filter(
            Q(turmas=turma) &
            Q(data__gte=date.today())
        ).order_by('data')
        
        paginacao_comunicados = Paginator(comunicados, 2)

        pagina_atual = paginacao_comunicados.page(pagina_atual)
        
        context.update(
            {
                'comunicados': comunicados,
                'atividades_escolares': atividades_escolares,
                'materiais_didaticos': materiais_didaticos,
                'hoje': date.today(),
                'paginacao_comunicados': paginacao_comunicados,
                'pagina_atual': pagina_atual
            }
        )
        return context
