from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import Aluno


def pagina_graficos(request):

    return render(
        request,
        'acompanhamento/graficos.html'
    )


def grafico_alunos(request):

    dados = {
        'labels': ['Manhã', 'Tarde', 'Noite'],
        'valores': [
            Aluno.objects.filter(turno_estuda__nome='Manhã').count(),
            Aluno.objects.filter(turno_estuda__nome='Tarde').count(),
            Aluno.objects.filter(turno_estuda__nome='Noite').count(),
        ]
    }

    return JsonResponse(dados)