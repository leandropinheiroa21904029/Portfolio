from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Olá n00b, esta é a página web mais básica do mundo!")

def cmbyn_view(request):
    return HttpResponse("Is it better to speak or to die?")

def achilles_view(request):
    return HttpResponse("he's half of my soul as the poets say")

def rwrb_view(request):
    return HttpResponse("History huh? Bet we could make some")
