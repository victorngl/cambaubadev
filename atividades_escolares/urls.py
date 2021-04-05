from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from .views import atividades_escolares, AtividadesEscolaresDetailView

urlpatterns = [
    path('', atividades_escolares, name="atividades_escolares"),
    path('<int:pk>/', login_required(AtividadesEscolaresDetailView.as_view(template_name="atividade_escolar_detail.html")), name="atividade_escolar_detail")
]