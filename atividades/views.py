from datetime import datetime
from escolas.models.aluno import Aluno
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import permission_required
from django.views.generic import CreateView, ListView, DetailView
from atividades.models import Oficina, AtividadeExtra, AtividadeNoturna, InscricaoOficina, InscricaoAtividadeExtra, InscricaoAtividadeNoturna
from .forms import InscricaoOficinaForm, InscricaoAtividadeExtraForm, InscricaoAtividadeNoturnaForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden

@permission_required("core.pode_acessar_atividades")
def oficinas(request):
	oficinas = Oficina.objects.all()
	return render(
		request,
		'oficinas_list.html',
		{
			'oficinas': oficinas
		}
	)

@permission_required("core.pode_acessar_atividades")
def atividades_extras(request):
	perfil = request.user.profile.perfil
	atividades_extras_filtro = []
	atividades_extras = []
	if perfil == "Aluno":
		aluno = Aluno.objects.get(usuario=request.user)
		atividades_extras = AtividadeExtra.objects.get(turmas=aluno.turma)
	elif perfil == 'Responsável' or perfil == 'Professor/Responsavel':
		alunos=Aluno.objects.filter(
                Q(responsavel1=request.user) | 
                Q(responsavel2=request.user) | 
                Q(responsavel3=request.user) | 
                Q(responsavel4=request.user) | 
                Q(responsavel5=request.user)
                ) 
		atividades_extras_completo = AtividadeExtra.objects.all() 
		for aluno in alunos:
			atividades_extras_filtro.append(AtividadeExtra.objects.filter(turmas=aluno.turma))
		for i in range(atividades_extras_filtro.__len__()):
			for atividade_extra in atividades_extras_completo:
				for atividade_filtro in atividades_extras_filtro[i]:
					if(atividade_filtro == atividade_extra):
						atividades_extras.append(atividade_filtro)
		atividades_extras = list(set(atividades_extras))
	return render(
		request,
		'atividades_extras_list.html',
		{
			'atividades_extras': atividades_extras
		}
	)

@permission_required("core.pode_acessar_atividades")
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
		context['form'].fields['aluno'].queryset = context['form'].fields['aluno'].queryset.filter(
			Q(responsavel1=self.request.user) | 
			Q(responsavel2=self.request.user) | 
			Q(responsavel3=self.request.user) | 
			Q(responsavel4=self.request.user) | 
			Q(responsavel5=self.request.user)
		)
		context.update(
			{
				'inscricao_oficina': self.kwargs['id'],
				'oficina': oficina,
				'usuario_inscricao': self.request.user
			}
		)
		return context
	
	def dispatch(self, request, *args, **kwargs):
		if request.user.has_perm('core.pode_acessar_atividades'):
			return super(InscricaoOficinaCreateView, self).dispatch(request, *args, **kwargs)
		else:
			return HttpResponseForbidden()
	

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
		context['form'].fields['aluno'].queryset = context['form'].fields['aluno'].queryset.filter(
			Q(responsavel1=self.request.user) | 
			Q(responsavel2=self.request.user) | 
			Q(responsavel3=self.request.user) | 
			Q(responsavel4=self.request.user) | 
			Q(responsavel5=self.request.user)
		)
		context.update(
			{
				'inscricao_atividade_extra': self.kwargs['id'],
				'atividade_extra': atividade_extra,
				'usuario_inscricao': self.request.user
			}
		)
		return context
	

	def dispatch(self, request, *args, **kwargs):
		atividade_extra = AtividadeExtra.objects.get(id=self.kwargs['id'])
		if request.user.has_perm('core.pode_acessar_atividades') and atividade_extra.inscricoes_abertas:
			return super(InscricaoAtividadeExtraCreateView, self).dispatch(request, *args, **kwargs)
		else:
			return HttpResponseForbidden()

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
		context['form'].fields['aluno'].queryset = context['form'].fields['aluno'].queryset.filter(
			Q(responsavel1=self.request.user) | 
			Q(responsavel2=self.request.user) | 
			Q(responsavel3=self.request.user) | 
			Q(responsavel4=self.request.user) | 
			Q(responsavel5=self.request.user)
		)
		context.update(
			{
				'inscricao_atividade_noturna': self.kwargs['id'],
				'atividade_noturna': atividade_noturna,
				'usuario_inscricao': self.request.user
			}
		)
		return context
	
	def dispatch(self, request, *args, **kwargs):
		if request.user.has_perm('core.pode_acessar_atividades'):
			return super(InscricaoAtividadeNoturnaCreateView, self).dispatch(request, *args, **kwargs)
		else:
			return HttpResponseForbidden()

class OficinaDetailView(DetailView):
	model = Oficina
	
	def dispatch(self, request, *args, **kwargs):
		if request.user.has_perm('core.pode_acessar_atividades'):
			return super(OficinaDetailView, self).dispatch(request, *args, **kwargs)
		else:
			return HttpResponseForbidden()

class AtividadeNoturnaDetailView(DetailView):
	model = AtividadeNoturna
	
	def dispatch(self, request, *args, **kwargs):
		if request.user.has_perm('core.pode_acessar_atividades'):
			return super(AtividadeNoturnaDetailView, self).dispatch(request, *args, **kwargs)
		else:
			return HttpResponseForbidden()

class AtividadeExtraDetailView(DetailView):
	model = AtividadeExtra
	
	def dispatch(self, request, *args, **kwargs):
		if request.user.has_perm('core.pode_acessar_atividades'):
			return super(AtividadeExtraDetailView, self).dispatch(request, *args, **kwargs)
		else:
			return HttpResponseForbidden()