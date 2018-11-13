from django.shortcuts import render
from .models import Livros
from django.utils import timezone

# Create your views here.
def tela_inicial(request):
	codigos = Livros.objects.order_by('codigo')
	return render(request, 'biblioteca/inicio.html', {'livrosCadastrados': codigos})