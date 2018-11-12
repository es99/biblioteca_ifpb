from django.urls import path
from . import views

urlpatterns = [
	path('', views.tela_inicial, name = 'inicio')
]