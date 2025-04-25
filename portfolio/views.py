from django.shortcuts import render
from .models import Projeto, Tecnologia

def index_view(request):
    return render(request, "portfolio/index.html")

def sobre_view(request):
    return render(request, "portfolio/sobre.html")

def interesses_view(request):
    return render(request, "portfolio/interesses.html")

def projetos_view(request):
    context = {
        'projetos': Projeto.objects.all().order_by('nome')
    }
    return render(request, "portfolio/projetos.html", context)

def projeto_view(request, projeto_id):
    context = {
        'projeto': Projeto.objects.get(id=projeto_id)
    }
    return render(request, "portfolio/projeto.html", context)

def tecnologias_view(request):
    context = {
        'tecnologias': Tecnologia.objects.all().order_by('nome')
    }
    return render(request, "portfolio/tecnologias.html", context)

def tecnologia_view(request, tecnologia_id):
    context = {
        'tecnologia': Tecnologia.objects.get(id=tecnologia_id)
    }
    return render(request, "portfolio/tecnologia.html", context)

def cv_view(request):
    return render(request, "portfolio/cv.html")
