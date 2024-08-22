from django.urls import path
from .views import home, registro, login

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
]
