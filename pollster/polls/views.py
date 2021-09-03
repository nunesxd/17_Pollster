from django.shortcuts import render
from .models import Question, Choice

# Get Questions, e as mostra:


def index(request):
    # Obtemos a lista das cinco questões de nosso modelo na base, ordenando-as pela data de publicação, de fora descendente:
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # Criamos um objeto tipo JSON com essa lista e passamos para renderizar no site.
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
