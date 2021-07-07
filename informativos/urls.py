from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from .views import balancetes, balancos_patrimoniais, documentacoes_obras, atas_reunioes,contato_representantes, BalancetesDetailView, BalancoPatrimonialDetailView, DocumentacaoObraDetailView, AtaReuniaoDetailView

urlpatterns = [
    path('balancetes/', balancetes, name="balancetes"),
    # path('balancos_patrimoniais/', balancos_patrimoniais, name="balancos_patrimoniais"),
    path('relatorios_trimestrais/', balancos_patrimoniais, name="balancos_patrimoniais"),
    # path('documentacoes_obras/', documentacoes_obras, name="documentacoes_obras"),
    path('aemc_noticias/', documentacoes_obras, name="documentacoes_obras"),
    # path('atas_reunioes/', atas_reunioes, name="atas_reunioes"),
    path('grupo_de_pais_representantes/atas_reunioes', atas_reunioes, name="atas_reunioes"),
    path('grupo_de_pais_representantes/contato', contato_representantes, name="contato_representantes"),
    path('balancetes/<int:pk>/', login_required(BalancetesDetailView.as_view(template_name="balancete_detail.html")), name="balancete_detail"),
    # path('balancos_patrimoniais/<int:pk>/', login_required(BalancoPatrimonialDetailView.as_view(template_name="balanco_patrimonial_detail.html")), name="balanco_patrimonial_detail"),
    path('relatorios_trimestrais/<int:pk>/', login_required(BalancoPatrimonialDetailView.as_view(template_name="balanco_patrimonial_detail.html")), name="balanco_patrimonial_detail"),
    # path('documentacoes_obras/<int:pk>/', login_required(DocumentacaoObraDetailView.as_view(template_name="documentacao_obra_detail.html")), name="documentacao_obra_detail"),
    path('aemc_noticias/<int:pk>/', login_required(DocumentacaoObraDetailView.as_view(template_name="documentacao_obra_detail.html")), name="documentacao_obra_detail"),
    path('grupo_de_pais_representantes/atas_reunioes/<int:pk>/', login_required(AtaReuniaoDetailView.as_view(template_name="ata_reuniao_detail.html")), name="ata_reuniao_detail")
]