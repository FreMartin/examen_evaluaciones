from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def examen(request):
    data = {}
    return render(request, 'examen/examen.html', data)