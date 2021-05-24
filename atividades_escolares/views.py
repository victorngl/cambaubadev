from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.views.generic import DetailView
from django.http import JsonResponse, HttpResponseForbidden
from atividades_escolares.models import AtividadeEscolar

@permission_required("core.pode_acessar_atividades_escolares")
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
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('core.pode_acessar_atividades_escolares'):
            return super(AtividadesEscolaresDetailView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
