import random
from django.http import HttpResponse
from django.shortcuts import render

from examen.models import Pregunta, Respuesta


def examen(request):

    preguntas = Pregunta.objects.all()
    respuestas = Respuesta.objects.all()
   

    data = {
        'preguntas': preguntas,
        'respuestas': respuestas
    }

    return render(request, 'examen/examen.html', data)