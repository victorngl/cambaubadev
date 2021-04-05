from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from .views import enquetes, RespostaEnqueteCreateView

urlpatterns = [
    path('', enquetes, name="enquetes"),
    path('<int:id>/responder_enquete', login_required(RespostaEnqueteCreateView.as_view(template_name="resposta_enquete_form.html")), name="resposta_enquete_create"),
]