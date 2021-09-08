from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice

# Obtem as questões e as mostra nos templates criados:


def index(request):
    # Obtemos a lista das cinco questões de nosso modelo na base, ordenando-as pela data de publicação, de fora descendente:
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # Criamos um objeto tipo JSON com essa lista e passamos para renderizar no site.
    context = {'latest_question_list': latest_question_list}
    # Definimos em 'settings' o nosso diretório de templates, abaixo ele irá reconhecer e auto-preencher a url para o index.html.
    return render(request, 'polls/index.html', context)

# Mostra os detalhes específicos de um questão e das opções:


def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/details.html', {'question': question})

# Identifica a questão e mostra seus resultados:


def results(request, question_id):
    # Abaixo utilizamos um 'django shortcut', que nos permite procurar um item na base de dados e caso não encontre, retorna um erro 404. Desta forma não precisamos usar um try / catch, por exemplo.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Registra o voto para aquela opção:


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # OBS 1 - O Djando ORM (Object Relational Mapper) gera um método para os modelos que utilizam da foreign key, atráves do 'RelatedManager'. O 'foo_set', que neste caso é 'choice_set', é criado de forma que podemos acessar as opções, questões, diretamente pelo nosso modelo de perguntas.
        # OBS 2 - O request.POST['choice'] se refere ao form criado no template 'details.html', lá o form possui um id único como 'choiceX'(X sendo o número daquela iteração), deste, quando rodamos o POST, podemos acessar o atributo 'value' e incrementá-lo
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error message': 'Please select a choice.'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Sempre devemos retornar um HttpResponseRedirect depois de lidarmos com sucesso com um POST data. Desta forma previnimos que seja feito duas vezes, se o usuário clicar no botão de back.
        # O 'reverse' é um método para construção de URL, pois podemos receber demais argumentos dentro dele.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
