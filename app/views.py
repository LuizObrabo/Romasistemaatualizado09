from django.shortcuts import render, redirect
from app.forms import NomesForm
from app.models import nomes
from django.db import models



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
    data['db'] = nomes.objects.all
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
