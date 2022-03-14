from django.urls import path
from .views import home
from .views import gerar_boletos_boletins
from .views import get_calendario

urlpatterns = [
    path('', home, name="home"),
    # path('boletos_boletins/', gerar_boletos_boletins, name='boletos_boletins'),
    path('get_calendario/', get_calendario, name='get_calendario'),
]