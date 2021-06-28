from escolas.models.aluno import Aluno
from atividades.models.atividade_extra import AtividadeExtra
from django import forms
from django.db.models import Q
from .models import InscricaoOficina, InscricaoAtividadeExtra, InscricaoAtividadeNoturna

class InscricaoOficinaForm(forms.Form, forms.ModelForm):
    class Meta:
        model = InscricaoOficina
        fields = [
            'oficina',
            'aluno',
            'usuario_inscricao'
        ]
        widgets = {
            'oficina': forms.HiddenInput(),
            'usuario_inscricao': forms.HiddenInput(),
        }

class InscricaoAtividadeExtraForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InscricaoAtividadeExtraForm, self).__init__(*args, **kwargs)
        atividade_extra = AtividadeExtra.objects.get(titulo=kwargs['initial']['atividade_extra'])
        self.fields['aluno'].queryset = self.fields['aluno'].queryset.filter(turma__in = atividade_extra.turmas.all())

    class Meta:
        model = InscricaoAtividadeExtra
        fields = [
            'atividade_extra',
            'aluno',
            'usuario_inscricao'
        ]
        widgets = {
            'atividade_extra': forms.HiddenInput(),
            'usuario_inscricao': forms.HiddenInput(),
        }

class InscricaoAtividadeNoturnaForm(forms.ModelForm):
    class Meta:
        model = InscricaoAtividadeNoturna
        fields = [
            'atividade_noturna',
            'aluno',
            'usuario_inscricao'
        ]
        widgets = {
            'atividade_noturna': forms.HiddenInput(),
            'usuario_inscricao': forms.HiddenInput(),
        }
