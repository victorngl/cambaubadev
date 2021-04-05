from django import forms
from .models import Enquete, RespostaEnquete

class RespostaEnqueteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RespostaEnqueteForm, self).__init__(*args, **kwargs)
        opcoes = Enquete.objects.get(id=kwargs['initial']['enquete'])
        self.fields['opcao'] = forms.ChoiceField(
            choices=(opcoes.lista_opcoes),
            widget=forms.RadioSelect
        )
    
    class Meta:
        model = RespostaEnquete
        fields = [
            'enquete',
            'opcao'
        ]
