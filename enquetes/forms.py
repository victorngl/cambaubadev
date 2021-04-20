from django import forms
from .models import Enquete, RespostaEnquete, Opcao
from django.utils.safestring import mark_safe

class RespostaEnqueteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RespostaEnqueteForm, self).__init__(*args, **kwargs)
        opcoesArray = Opcao.objects.filter(enquete=kwargs['initial']['enquete'])
        opcoes = list()
        for idx, opcao in enumerate(opcoesArray):
            opcoes += [(str(opcao.id), mark_safe(opcao.titulo.html))]
        self.fields['opcao'] = forms.ChoiceField(
            choices=(opcoes),
            widget=forms.RadioSelect
        )
    
    class Meta:
        model = RespostaEnquete
        fields = [
            'enquete',
            'opcao'
        ]
        widgets = {
            'enquete': forms.HiddenInput()
        }
