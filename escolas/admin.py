from django.contrib import admin
from .models import Aluno, Escola, Serie, TipoSerie, Turma

admin.site.register(Aluno)
admin.site.register(Escola)
admin.site.register(Serie)
admin.site.register(TipoSerie)
admin.site.register(Turma)
