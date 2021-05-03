from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Endereco
from .models import Estado
from .models import Cidade


def buscar_cep(request):
    if request.method == 'POST':
        cep = request.POST.get('cep', "")

        endereco = Endereco.objects.buscar_cep(cep)

        return JsonResponse(endereco)


def on_change_pais(request):
    if request.method == 'POST':
        pais = request.POST.get('pais', 0)

        estados = Estado.objects.filter(pais=pais)

        estados_serializados = serializers.serialize('json', estados)
        return JsonResponse(estados_serializados, safe=False)


def on_change_estado(request):
    if request.method == 'POST':
        estado = request.POST.get('estado', 0)

        cidades = Cidade.objects.filter(estado=estado)

        cidades_serializadas = serializers.serialize('json', cidades)
        return JsonResponse(cidades_serializadas, safe=False)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def resetar_senha(request):
    return render(request, 'resetar_senha.html', {})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('senha_resetada')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


@login_required
def senha_resetada(request):
    return render(request, 'senha_resetada.html', {})