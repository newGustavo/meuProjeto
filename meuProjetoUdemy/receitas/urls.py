from django.urls import path
from receitas.views import hello, contato


urlpatterns = [
    path('', hello),
    path('contato', contato),
]