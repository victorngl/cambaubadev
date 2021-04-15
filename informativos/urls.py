from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from .views import balancetes, balancos_patrimoniais, documentacoes_obras, atas_reunioes, BalancetesDetailView, BalancoPatrimonialDetailView, DocumentacaoObraDetailView, AtaReuniaoDetailView

urlpatterns = [
    path('balancetes/', balancetes, name="balancetes"),
    path('balancos_patrimoniais/', balancos_patrimoniais, name="balancos_patrimoniais"),
    path('documentacoes_obras/', documentacoes_obras, name="documentacoes_obras"),
    path('atas_reunioes/', atas_reunioes, name="atas_reunioes"),
    path('balancetes/<int:pk>/', login_required(BalancetesDetailView.as_view(template_name="informativo_detail.html")), name="balancete_detail"),
    path('balancos_patrimoniais/<int:pk>/', login_required(BalancoPatrimonialDetailView.as_view(template_name="informativo_detail.html")), name="balanco_patrimonial_detail"),
    path('documentacoes_obras/<int:pk>/', login_required(DocumentacaoObraDetailView.as_view(template_name="informativo_detail.html")), name="documentacao_obra_detail"),
    path('atas_reunioes/<int:pk>/', login_required(AtaReuniaoDetailView.as_view(template_name="ata_reuniao_detail.html")), name="ata_reuniao_detail")
]