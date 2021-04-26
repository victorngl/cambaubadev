from django.urls import path
from .views import agenda, eventos_data

urlpatterns = [
    path('', agenda, name="agenda"),
    path('eventos_data/', eventos_data, name="eventos_data")
]