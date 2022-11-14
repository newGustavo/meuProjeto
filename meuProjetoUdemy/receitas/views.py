from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html', context={
        'nome': 'Gustavo Nascimento'
    })

def contato(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')