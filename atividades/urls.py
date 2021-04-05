from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from .views import oficinas, atividades_extras, atividades_noturnas, InscricaoOficinaCreateView, InscricaoAtividadeExtraCreateView, InscricaoAtividadeNoturnaCreateView

urlpatterns = [
    path('oficinas/', oficinas, name="oficinas"),
    path('atividades_extras/', atividades_extras, name="atividades_extras"),
    path('atividades_noturnas/', atividades_noturnas, name="atividades_noturnas"),
    path('oficinas/<int:id>/inscricao_oficina', login_required(InscricaoOficinaCreateView.as_view(template_name="inscricao_oficina_form.html")), name="inscricao_oficina_create"),
    path('atividades_extras/<int:id>/inscricao_atividade_extra', login_required(InscricaoAtividadeExtraCreateView.as_view(template_name="inscricao_atividade_extra_form.html")), name="inscricao_atividade_extra_create"),
    path('atividades_noturnas/<int:id>/inscricao_atividade_noturna', login_required(InscricaoAtividadeNoturnaCreateView.as_view(template_name="inscricao_atividade_noturna_form.html")), name="inscricao_atividade_noturna_create")
]