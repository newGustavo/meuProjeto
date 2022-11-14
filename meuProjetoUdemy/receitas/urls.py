from django.urls import path
from receitas.views import home, contato, sobre


urlpatterns = [
    path('contato', contato),
    path('sobre', sobre),
]