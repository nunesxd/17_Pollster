from django.shortcuts import render

# Esta página será uma landing page, caso alguém acesse o site pela url basica, sem ser pelo polls.


def index(request):
    return render(request, 'pages/index.html')
