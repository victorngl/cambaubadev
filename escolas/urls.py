from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from .views import TurmaDetailView
from .views import AlunoDetailView, escolas
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('<int:pk>', login_required(TurmaDetailView.as_view(template_name="turma_detail.html")), name="turma_detail"),
    path('alunos/<int:pk>/', login_required(AlunoDetailView.as_view(template_name="aluno_detail.html")), name="aluno_detail")
]