from django.urls import path
from .views import home
from .views import gerar_boletos_boletins

urlpatterns = [
    path('', home, name="home"),
    path('boletos_boletins/', gerar_boletos_boletins, name='boletos_boletins'),
]