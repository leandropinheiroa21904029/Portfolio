from django.db import models

class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome

class Tecnologia(models.Model):
    nome = models.CharField(max_length=200)
    logo = models.ImageField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Curiosidades(models.Model):
    desafios = models.TextField(null=True, blank=True)
    interesses = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.desafios} - {self.interesses}"

class Disciplina(models.Model):

    ANO_1 = 1
    ANO_2 = 2
    ANO_3 = 3
    ANO_CHOICES = [
        (ANO_1, "1º Ano"),
        (ANO_2, "2º Ano"),
        (ANO_3, "3º Ano"),
    ]

    SEMESTRE_1 = 1
    SEMESTRE_2 = 2
    SEMESTRE_CHOICES = [
        (SEMESTRE_1, "1º Semestre"),
        (SEMESTRE_2, "2º Semestre"),
    ]

    nome = models.CharField(max_length=200)
    ano = models.IntegerField(choices=ANO_CHOICES, default=ANO_1)
    semestre = models.IntegerField(choices=SEMESTRE_CHOICES, default=SEMESTRE_1)
    docentes = models.ManyToManyField(Docente, related_name='docentes')
    moodle =  models.URLField(null=True, blank=True)
    ulusofona =  models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.ano}º Ano/{self.semestre}º Semestre"


class Conceito(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    link_git = models.URLField(null=True, blank=True)
    link_video = models.URLField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='disciplina')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='tecnologias')
    curiosidades = models.OneToOneField(Curiosidades, on_delete=models.CASCADE, related_name='curiosidades')
    conceitos = models.ManyToManyField(Conceito, related_name='conceitos')

    def __str__(self):
        return f"{self.nome} - {self.disciplina}"

class Imagem(models.Model):
    imagem = models.ImageField(null=True, blank=True)
    descricao = models.CharField(max_length=200)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='imagens')

    def __str__(self):
        return self.descricao

