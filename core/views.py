from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
# Create your views here.


def index(requests):
    return redirect('/agenda/')


def local_evento(requests, titulo=None):
    evento = Evento.objects.get(titulo=titulo)
    return HttpResponse('%s foi definido como local para o Evento %s.' % (evento.local, titulo))


def lista_eventos(request):
    user = request.user
    eventos = Evento.objects.filter(user=user)
    response = {
        'user': eventos[0].user,
        'eventos': eventos,
    }
    return render(request, 'agenda.html', response)
