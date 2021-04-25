from django.urls import path
from .views import home
from .views import gerar_boletos_boletins
from escolas import urls as escolas_urls

urlpatterns = [
    path('', home, name="home"),
    path('boletos_boletins/', gerar_boletos_boletins, name='boletos_boletins'),
]