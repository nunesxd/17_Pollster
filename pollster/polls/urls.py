from django.urls import path
from . import views

# Criação das rotas de nosso site. O arquivo 'urls' que está na pasta principal 'pollster', está criando as rotas padrões do site (tipo o 'app.use()' do JS):

app_name = 'polls'
urlpatterns = [
    # Se deixarmos como '', ele usará a rota configurada no 'urls.py' da pasta principal 'pollster'.
    path('', views.index, name='index'),
    # Estamos definindo que um parâmetro deverá ser passado nesta rota, no caso um inteiro chamado 'question_id'.
    path('<int:question_id>/', views.details, name='details'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
