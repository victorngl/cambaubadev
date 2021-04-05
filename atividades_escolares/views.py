from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from atividades_escolares.models import AtividadeEscolar

@login_required
def atividades_escolares(request):
    atividades_escolares = AtividadeEscolar.objects.all()
    return render(
        request,
        'atividades_escolares_list.html',
        {
            'atividades_escolares': atividades_escolares
        }
    )

class AtividadesEscolaresDetailView(DetailView):
    model = AtividadeEscolar
