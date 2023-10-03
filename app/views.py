from django.shortcuts import render, redirect
from app.forms import NomesForm, ConsignadoForm, EmprestimoForm
from app.models import nomes, consignado, emprestimo
from django.db import models
import logging
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = nomes.objects.filter(Nome_completo__icontains=search)
    else:
        data['db'] = nomes.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = NomesForm()
    return render(request, 'form.html', data)

def create(request):
    if request.method == 'POST':
        form = NomesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NomesForm()
    return render(request, 'form.html', {'form': form})

def view(request, pk):
    data = {}
    data['db'] = nomes.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = nomes.objects.get(pk=pk)
    if request.method == 'POST':
        form = NomesForm(request.POST, request.FILES, instance=data['db'])
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NomesForm(instance=data['db'])
    return render(request, 'form.html', {'form': form})

def update(request, pk):
    data = {}
    data['db'] = nomes.objects.get(pk=pk)
    form = NomesForm(request.POST, request.FILES, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = nomes.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def create_consignado(request):
    if request.method == 'POST':
        form = ConsignadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ConsignadoForm()
    return render(request, 'consignado_form.html', {'form': form})

def create_user(request):
    return render(request,'create_user.html')

def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'create_user.html',data)

def create_emprestimo(request,pk):
    if request.method == 'POST':
        form = emprestimo(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            logging.info('Formulário de Empréstimo salvo com sucesso!')
            return redirect('index.html')
        else:

            logging.error('O formulário de Empréstimo não é válido.')
    else:
        form = EmprestimoForm()
    return render(request, 'emprestimo_form.html', {'form': form})

#Formulário do painel de login
def painel(request):
    return render(request,'painel.html')

#Processa o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request,'painel.html',data)

#Página inicial do dashboard
def dashboard(request):
    return render(request,'dashboard/home.html')