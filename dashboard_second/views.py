from django.shortcuts import render
from .models import AlunoConcluido

def dashboard(request):
    aluno_concluido = AlunoConcluido.objects.all
    return render(request, 'dashboard_second/dashboard_second.html', {'aluno_concluido': aluno_concluido})
