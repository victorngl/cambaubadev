from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, date, timedelta
from processo_seletivo.models import Entrevista
from .models import Evento

# Create your views here.
def agenda(request):
    hoje = date.today()
    return render(request, 'calendario.html', {
        'hoje': hoje
    })

def eventos_data(request):
    data_inicio = request.GET['start'][:10]
    data_termino = request.GET['end'][:10]

    eventos = Evento.objects.filter(
        data__gte=data_inicio,
        data__lte=data_termino,
    )

    list_eventos = [
        {
            'id': evento.id, 
            'title': evento.nome,
            'start': '{}T{}'.format(evento.data, evento.hora_inicio),
            'end': '{}T{}'.format(evento.data, evento.hora_termino)
        } for evento in eventos
    ]
    
    return JsonResponse(list_eventos, safe=False)

def criar_evento(request):
    print("Recebi a solicitação")