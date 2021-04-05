from django import forms
from .models import InscricaoOficina, InscricaoAtividadeExtra, InscricaoAtividadeNoturna

class InscricaoOficinaForm(forms.ModelForm):
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
