from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import Enquete, RespostaEnquete
from .forms import RespostaEnqueteForm

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

class RespostaEnqueteCreateView(CreateView):
    model = RespostaEnquete
    form_class = RespostaEnqueteForm
    template_name = 'resposta_enquete_form.html'
    success_url = 'enquetes/'

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
