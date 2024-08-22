from django.contrib import admin

from examen.models import Pregunta, Respuesta

admin.site.register([Pregunta, Respuesta])