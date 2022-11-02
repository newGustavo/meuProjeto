from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(request, 'receitas/index.html')

def contato(request):
    return HttpResponse('Contato: (XX)XXXXX-XXXX')