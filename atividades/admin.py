from django.contrib import admin
from .models import Oficina, AtividadeExtra, AtividadeNoturna, InscricaoOficina, InscricaoAtividadeExtra, InscricaoAtividadeNoturna

admin.site.register(Oficina)
admin.site.register(AtividadeExtra)
admin.site.register(AtividadeNoturna)
admin.site.register(InscricaoOficina)
admin.site.register(InscricaoAtividadeExtra)
admin.site.register(InscricaoAtividadeNoturna)
