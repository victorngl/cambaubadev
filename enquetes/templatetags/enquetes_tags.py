from django import template
from enquetes.models import Enquete, RespostaEnquete
from crum import get_current_user
from django.db import connection
from datetime import date
 
register = template.Library()

""" @register.simple_tag()
def bloquear_enquete(enquete):
    user = get_current_user()
    enquetes_respondidas = RespostaEnquete.objects.filter(usuario_votante=user, enquete=enquete)
    if enquete and enquetes_respondidas:
        if enquete.voto_unico and enquetes_respondidas.count() < 1 and enquete.data_expiracao >= date.today() :
            return True
        else:
            return False
    else: return False """

@register.simple_tag()
def bloquear_enquete(enquete):
    user = get_current_user()
    enquetes_respondidas = RespostaEnquete.objects.filter(
        usuario_votante=user, 
        enquete=enquete 
    ).exists()

    if enquetes_respondidas and enquete.voto_unico:
        return False # Se respondeu a enquete && se o voto é unico
    else: 
        if enquete.data_expiracao < date.today(): 
            return False # Se a data foi inspirada
        else:
            return True # Se não respondeu a enquete
        
        