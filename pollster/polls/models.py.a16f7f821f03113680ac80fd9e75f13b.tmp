'''
- Módulo responsável pela criação dos modelos que serão usados no site, segundo o padrão MVC.

OBS: O Django já cria uma primary key automaticamente para cada modelo em nossa base de dados, que por padrão é o sqlite3.

OBS 2: Logo após criarmos os modelos, devemos rodar:
1) 'python manage.py makemigrations polls' - Que cria o arquivo contendo o código responsável pela criação das tabelas na base de dados;
2) 'python manage.py migrate' - Que cria as respectivas tabelas dos modelos na base de dados, segundo o arquivo criado na primeira etapa.

OBS 3: Podemos relizar queries diretamente do terminal, rodando: 'python manage.py shell', sendo que podemos rodar, exemplo:
>>> from polls.models import Question, Choice
>>> from django.utils import timezone                                          
>>> q = Question(question_text='What is your favorite Python framework ?',pub_date=timezone.now()) 
>>> q.save()
>>> q.id
1
>>> q.question_text
'What is your favorite Python framework ?'
>>> Question.objects.all()
<QuerySet [<Question: What is your favorite Python framework ?>]>
>>> Question.objects.filter(id=1) 
<QuerySet [<Question: What is your favorite Python framework ?>]>
>>> Question.objects.get(pk=1) 
<Question: What is your favorite Python framework ?>
>>> q2 = Question.objects.get(pk=1) 
>>> q2.choice_set.all()
<QuerySet []>
>>> q2.choice_set.create(choice_text="Django",votes=0) 
<Choice: Django>
>>> q2.choice_set.create(choice_text="Flask",votes=0)  
<Choice: Flask>
>>> q2.choice_set.create(choice_text="Web2py",votes=0) 
<Choice: Web2py>
>>> q2.choise_set.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Question' object has no attribute 'choise_set'
>>> q2.choice_set.all() 
<QuerySet [<Choice: Django>, <Choice: Flask>, <Choice: Web2py>]>
'''

from django.db import models


class Question(models.Model):
    # Abaixo definimos os campos que teremos na classe Question, no caso o campo será de caracteres:
    question_text = models.CharField(max_length=200)
    # O texto será disponibilizado quando o campo for acionado:
    pub_date = models.DateTimeField('date published')

    # Quando formos nos referir a classe dentro no módulo 'admin', por padrão ele aparecerá como 'Question.object', sendo que queremos que apareça o conteúdo do texto, assim como nos 'Choices':
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # Abaixo criamos uma relação entre os modelos, tabelas:
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
