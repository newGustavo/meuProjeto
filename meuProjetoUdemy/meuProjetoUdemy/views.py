from django.shortcuts import render

def projetoUdemy(request):
    return render(request, 'home.html')