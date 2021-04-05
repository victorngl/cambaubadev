from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from atividades.models import Oficina, AtividadeExtra, AtividadeNoturna, InscricaoOficina, InscricaoAtividadeExtra, InscricaoAtividadeNoturna
from .forms import InscricaoOficinaForm, InscricaoAtividadeExtraForm, InscricaoAtividadeNoturnaForm
from django.urls import reverse, reverse_lazy

@login_required
def oficinas(request):
    oficinas = Oficina.objects.all()
    return render(
        request,
        'oficinas_list.html',
        {
            'oficinas': oficinas
        }
    )

@login_required
def atividades_extras(request):
    atividades_extras = AtividadeExtra.objects.all()
    return render(
        request,
        'atividades_extras_list.html',
        {
            'atividades_extras': atividades_extras
        }
    )

@login_required
def atividades_noturnas(request):
    atividades_noturnas = AtividadeNoturna.objects.all()
    return render(
        request,
        'atividades_noturnas_list.html',
        {
            'atividades_noturnas': atividades_noturnas
        }
    )

class InscricaoOficinaCreateView(CreateView):
    model = InscricaoOficina
    form_class = InscricaoOficinaForm
    template_name = 'inscricao_oficina_form.html'
    success_url = reverse_lazy('oficinas')

    def get_initial(self):
        oficina = Oficina.objects.get(id=self.kwargs['id'])
        initial = {
            'oficina': oficina,
            'usuario_inscricao': self.request.user
        }
        return initial

    def get_context_data(self, **kwargs):
        context = super(InscricaoOficinaCreateView, self).get_context_data(**kwargs)
        oficina = Oficina.objects.get(id=self.kwargs['id'])
        context.update(
            {
                'inscricao_oficina': self.kwargs['id'],
                'oficina': oficina,
                'usuario_inscricao': self.request.user
            }
        )
        return context

class InscricaoAtividadeExtraCreateView(CreateView):
    model = InscricaoAtividadeExtra
    form_class = InscricaoAtividadeExtraForm
    template_name = 'inscricao_atividade_extra_form.html'
    success_url = reverse_lazy('atividades_extras')

    def get_initial(self):
        atividade_extra = AtividadeExtra.objects.get(id=self.kwargs['id'])
        initial = {
            'atividade_extra': atividade_extra,
            'usuario_inscricao': self.request.user
        }
        return initial

    def get_context_data(self, **kwargs):
        context = super(InscricaoAtividadeExtraCreateView, self).get_context_data(**kwargs)
        atividade_extra = AtividadeExtra.objects.get(id=self.kwargs['id'])
        context.update(
            {
                'inscricao_atividade_extra': self.kwargs['id'],
                'atividade_extra': atividade_extra,
                'usuario_inscricao': self.request.user
            }
        )
        return context

class InscricaoAtividadeNoturnaCreateView(CreateView):
    model = InscricaoAtividadeNoturna
    form_class = InscricaoAtividadeNoturnaForm
    template_name = 'inscricao_atividade_noturna_form.html'
    success_url = reverse_lazy('atividades_noturnas')

    def get_initial(self):
        atividade_noturna = AtividadeNoturna.objects.get(id=self.kwargs['id'])
        initial = {
            'atividade_noturna': atividade_noturna,
            'usuario_inscricao': self.request.user
        }
        return initial

    def get_context_data(self, **kwargs):
        context = super(InscricaoAtividadeNoturnaCreateView, self).get_context_data(**kwargs)
        atividade_noturna = AtividadeNoturna.objects.get(id=self.kwargs['id'])
        context.update(
            {
                'inscricao_atividade_noturna': self.kwargs['id'],
                'atividade_noturna': atividade_noturna,
                'usuario_inscricao': self.request.user
            }
        )
        return context
