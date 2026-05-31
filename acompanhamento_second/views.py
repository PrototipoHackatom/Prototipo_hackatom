from django.shortcuts import render
from django.http import JsonResponse
from dashboard_second.models import AlunoConcluido, AlunoDesistencia

def grafico(request):
    # Renderiza a página HTML dos gráficos
    return render(request, 'graficos_second/graficos_second.html')

def conclusao_desistencia(request):
    # Conta a quantidade de registros em cada tabela
    qtd_concluidos = AlunoConcluido.objects.count()
    qtd_desistentes = AlunoDesistencia.objects.count()

    labels = ['Concluídos', 'Desistentes']
    valores = [qtd_concluidos, qtd_desistentes]

    dados = {
        'labels': labels,
        'valores': valores
    }
    return JsonResponse(dados)

def desistencia(request):
    pass

def sexo_conclusao(request):
    pass