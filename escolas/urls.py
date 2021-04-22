from django.urls import path
from .views import AlunoDetailView, escolas
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('alunos/<int:pk>/', login_required(AlunoDetailView.as_view(template_name="aluno_detail.html")), name="aluno_detail"),
]