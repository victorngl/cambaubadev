from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from .views import TurmaDetailView

urlpatterns = [
    path('<int:pk>', login_required(TurmaDetailView.as_view(template_name="turma_detail.html")), name="turma_detail")
]