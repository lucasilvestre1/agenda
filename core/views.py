from django.shortcuts import render, HttpResponse
from core.models import Evento
# Create your views here.


def local_evento(requests, titulo=None):
    evento = Evento.objects.get(titulo=titulo)
    return HttpResponse('%s foi definido como local para o Evento %s.' % (evento.local, titulo))

