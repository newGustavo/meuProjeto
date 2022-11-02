from django.shortcuts import *
from django.http import *

def hello(request):
    return HttpResponse("Salve!")