from django.shortcuts import render
from .models import Aluno, Escola
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def escolas(request):
    return render(request)

class AlunoDetailView(DetailView):
    model = Aluno