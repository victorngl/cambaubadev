from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from .views import atas_reunioes, calendarios_atividades, comunicados, materiais_didaticos, AtasReunioesDetailView, CalendariosAtividadesDetailView, ComunicadosDetailView, MateriaisDidaticosDetailView

urlpatterns = [
    path('atas_reunioes/', atas_reunioes, name="atas_reunioes"),
    path('calendarios_atividades/', calendarios_atividades, name="calendarios_atividades"),
    path('comunicados/', comunicados, name="comunicados"),
    path('', materiais_didaticos, name="materiais_didaticos"),
    path('<int:pk>/', login_required(MateriaisDidaticosDetailView.as_view(template_name="material_didatico_detail.html")), name="material_didatico_detail"),
    path('calendarios_atividades/<int:pk>/', login_required(CalendariosAtividadesDetailView.as_view(template_name="material_didatico_detail.html")), name="calendario_atividade_detail"),
    path('comunicados/<int:pk>/', login_required(ComunicadosDetailView.as_view(template_name="material_didatico_detail.html")), name="comunicado_detail"),
    path('atas_reunioes/<int:pk>/', login_required(AtasReunioesDetailView.as_view(template_name="material_didatico_detail.html")), name="ata_reuniao_detail")
]