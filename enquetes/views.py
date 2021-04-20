from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView
from django.http import HttpResponseForbidden
from .models import Enquete, RespostaEnquete, Opcao
from .forms import RespostaEnqueteForm
from crum import get_current_user
from datetime import date

@login_required
def enquetes(request):
    enquetes = Enquete.objects.all()
    return render(
        request,
        'enquetes_list.html',
        {
            'enquetes': enquetes
        }
    )

class EnqueteDetailView(DetailView):
    model = Enquete

class RespostaEnqueteCreateView(CreateView):
    model = RespostaEnquete
    form_class = RespostaEnqueteForm
    template_name = 'resposta_enquete_form.html'
    
    def get_initial(self):
        initial = {
            'enquete': self.kwargs['id']
        }
        return initial

    def get_context_data(self, **kwargs):
        context = super(RespostaEnqueteCreateView, self).get_context_data(**kwargs)
        enquete = get_object_or_404(Enquete, pk=self.kwargs['id'])
        context.update(
            {
                'enquete': enquete
            }
        )
        return context
    
    def dispatch(self, request, *args, **kwargs):
        user = get_current_user()
        enquete = Enquete.objects.get(id=self.kwargs['id'])
        enquetes_respondidas = RespostaEnquete.objects.filter(usuario_votante=user, enquete=self.kwargs['id'])
        if enquete.voto_unico and enquetes_respondidas.count() < 1 and enquete.data_expiracao >= date.today():
            return super(RespostaEnqueteCreateView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def get_success_url(self): 
        enquete = Enquete.objects.get(id=self.kwargs['id'])

        if  enquete.mostrar_resultado:
            return reverse_lazy('enquete_resultados_detail', kwargs = {'pk': self.kwargs['id']})
        else:
            return reverse_lazy('enquetes')
