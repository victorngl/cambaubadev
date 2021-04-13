from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    perfil = 'Sem Vínculo'
    if request.user.profile:
        perfil = request.user.profile.perfil
        if perfil == 'Aluno':
            template_name = 'home_aluno.html'
        elif perfil == 'Responsável':
            template_name = 'home_responsavel.html'
        else:
            template_name = 'home.html'

    return render(
        request,
        template_name,
        {
            'perfil': perfil
        }
    )
