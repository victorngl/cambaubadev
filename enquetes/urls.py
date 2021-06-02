from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from .views import enquetes, EnqueteDetailView, RespostaEnqueteCreateView, EnqueteResultadoDetailView

urlpatterns = [
    path('', enquetes, name="enquetes"),
    path('<int:pk>', login_required(EnqueteDetailView.as_view(template_name="enquete_detail.html")), name="enquete_detail"),
    path('<int:pk>/resultados', login_required(EnqueteResultadoDetailView.as_view(template_name="enquete_resultados_detail.html")), name="enquete_resultados_detail"),
    path('<int:id>/responder_enquete', login_required(RespostaEnqueteCreateView.as_view(template_name="resposta_enquete_form.html")), name="resposta_enquete_create")
]