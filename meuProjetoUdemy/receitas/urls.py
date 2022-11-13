from django.urls import path
from receitas.views import hello, contato, sobre


urlpatterns = [
    path('', hello),
    path('contato', contato),
    path('sobre', sobre),
]