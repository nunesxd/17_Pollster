from django.urls import path
from . import views

# Criação das rotas de nosso site. O arquivo 'urls' que está na pasta principal 'pollster', está criando as rotas padrões do site (tipo o 'app.use()' do JS):

app_name = 'polls'
urlpatterns = [
    # Se deixarmos como '', ele usará a rota configurada no 'urls.py' da pasta principal 'pollster'.
    path('', views.index, name='index')
]
