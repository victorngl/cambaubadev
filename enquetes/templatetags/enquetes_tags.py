from django import template
from enquetes.models import Enquete, RespostaEnquete
from crum import get_current_user
from django.db import connection
from datetime import date
 
register = template.Library()

@register.simple_tag()
def bloquear_enquete(enquete):
    user = get_current_user()
    enquetes_respondidas = RespostaEnquete.objects.filter(usuario_votante=user, enquete=enquete)
    if enquete.voto_unico and enquetes_respondidas.count() < 1 and enquete.data_expiracao >= date.today() :
        return True
    else:
        return False