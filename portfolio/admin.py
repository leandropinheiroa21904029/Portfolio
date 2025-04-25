from django.contrib import admin
from .models import Docente, Conceito, Tecnologia, Curiosidades, Disciplina, Projeto, Imagem

admin.site.register(Docente)
admin.site.register(Conceito)
admin.site.register(Tecnologia)
admin.site.register(Curiosidades)
admin.site.register(Disciplina)
admin.site.register(Projeto)
admin.site.register(Imagem)