from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import Aluno, Curso, Escolaridade
from datetime import date


def pagina_graficos(request):

    return render(
        request,
        'acompanhamento/graficos.html'
    )


def grafico_Turno_estuda(request):

    dados = {
        'labels': ['Manhã', 'Tarde', 'Noite'],
        'valores': [
            Aluno.objects.filter(turno_estuda__nome='Manhã').count(),
            Aluno.objects.filter(turno_estuda__nome='Tarde').count(),
            Aluno.objects.filter(turno_estuda__nome='Noite').count(),
        ]
    }

    return JsonResponse(dados)

def grafico_cursos(request):

    cursos = Curso.objects.all()

    labels = []
    valores = []

    for curso in cursos:

        labels.append(curso.nome)

        quantidade = Aluno.objects.filter(curso=curso).count()

        valores.append(quantidade)

    dados = {
        'labels': labels,
        'valores': valores
    }

    return JsonResponse(dados)

def calcular_idade(data_nascimento):
    hoje = date.today()

    idade = hoje.year - data_nascimento.year

    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1

    return idade


def grafico_idade(request):

    alunos = Aluno.objects.all()

    idades = {}

    for aluno in alunos:

        idade = calcular_idade(aluno.data_nascimento)

        if idade in idades:
            idades[idade] += 1

        else:
            idades[idade] = 1

    # ordenar as idades
    idades_ordenadas = dict(sorted(idades.items()))

    dados = {
        'labels': list(idades_ordenadas.keys()),
        'valores': list(idades_ordenadas.values())
    }

    return JsonResponse(dados)

def grafico_bairros(request):

    alunos = Aluno.objects.all()

    bairros = {}

    for aluno in alunos:

        bairro_cidade = f'{aluno.bairro} - {aluno.cidade}'

        if bairro_cidade in bairros:

            bairros[bairro_cidade] += 1

        else:

            bairros[bairro_cidade] = 1

    bairros_ordenados = dict(
        sorted(
            bairros.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )

    dados = {
        'labels': list(bairros_ordenados.keys()),
        'valores': list(bairros_ordenados.values())
    }

    return JsonResponse(dados)

def grafico_escolaridade(request):
    escolaridades = Escolaridade.objects.all()

    labels = []
    valores = []

    for escolaridade in escolaridades:
        labels.append(escolaridade.nome)

        quantidade = Aluno.objects.filter(escolaridade=escolaridade).count()
        valores.append(quantidade)

        dados = {
            'labels': labels,
            'valores': valores
        }
    return JsonResponse(dados)
