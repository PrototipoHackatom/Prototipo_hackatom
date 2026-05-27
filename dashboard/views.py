from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno, TurnoEstuda, TurnoVaga,Aprendizagem, Escolaridade
from .models import Entidade, Curso, TipoFormacao
from autenticacao.models import Pessoa

def dashboard(request):

    pessoa_id = request.session.get('pessoa_id')

    usuario = Pessoa.objects.get(id=pessoa_id)

    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        nome_responsavel = request.POST.get('nome_responsavel')
        tel_responsavel = request.POST.get('tel_responsavel')
        
        profissional_id = request.POST.get('profissional_ref')
        profissional = Pessoa.objects.get(id=profissional_id)
        
        turno_estuda_id = request.POST.get('turno_estuda')
        turno_estuda = TurnoEstuda.objects.get(id=turno_estuda_id)

        tuno_vaga_id = request.POST.get('turno_vaga')
        turno_vaga = TurnoVaga.objects.get(id=tuno_vaga_id)

        aprendizagem_id = request.POST.get('aprendizagem')
        aprendizagem = Aprendizagem.objects.get(id=aprendizagem_id)

        escolaridade_id = request.POST.get('escolaridade')
        escolaridade = Escolaridade.objects.get(id=escolaridade_id)

        entidade_id = request.POST.get('entidade')
        entidade = Entidade.objects.get(id=entidade_id)

        curso_id = request.POST.get('curso')
        curso = Curso.objects.get(id=curso_id)

        tipo_formacao_id = request.POST.get('tipo_formacao')
        tipo_formacao = TipoFormacao.objects.get(id=tipo_formacao_id)



        aluno = Aluno(
            nome=nome,
            email=email,
            telefone=telefone,
            data_nascimento=data_nascimento,
            nome_responsavel=nome_responsavel,
            telefone_responsavel=tel_responsavel,
            profissional_ref=profissional,
            cadastrado_por=usuario,
            turno_estuda = turno_estuda,
            turno_vaga = turno_vaga,
            aprendizagem = aprendizagem,
            escolaridade = escolaridade,
            entidade = entidade,
            curso = curso,
            tipo_formacao = tipo_formacao
        )

        aluno.save()

        return redirect('dashboard')

    cargo_professor = usuario.cargo.filter(
        nome='Professor'
    ).exists()

    if cargo_professor:

        alunos = Aluno.objects.filter(
            cadastrado_por=usuario
        )

    else:

        alunos = Aluno.objects.all()

    pessoas = Pessoa.objects.all()
    turnos_estuda = TurnoEstuda.objects.all()
    turno_vaga = TurnoVaga.objects.all()
    aprendizagem = Aprendizagem.objects.all()
    escolaridade = Escolaridade.objects.all()
    entidade = Entidade.objects.all()
    curso = Curso.objects.all()
    tipo_formacao = TipoFormacao.objects.all()

    return render(
        request,
        'dashboard/dashboard.html',
        {
            'pessoas': pessoas,
            'alunos': alunos,
            'turnos_estuda': turnos_estuda,
            'turno_vaga': turno_vaga,
            'aprendizagem': aprendizagem,
            'escolaridade': escolaridade,
            'entidade': entidade,
            'curso': curso,
            'tipo_formacao': tipo_formacao
        }
    )

def editar_aluno(request, id):

    aluno = get_object_or_404(Aluno, id=id)

    if request.method == 'POST':

        aluno.nome = request.POST.get('nome')
        aluno.email = request.POST.get('email')
        aluno.telefone_responsavel = request.POST.get('telefone_responsavel')
        aluno.nome_responsavel = request.POST.get('nome_responsavel')
        aluno.data_nascimento = request.POST.get('data_nascimento')

        profissional_id = request.POST.get('profissional_ref')

        profissional = Pessoa.objects.get(id=profissional_id)

        aluno.profissional_ref = profissional

        aluno.save()

    return redirect('dashboard')

def excluir_aluno(request, id):

    aluno = get_object_or_404(Aluno, id=id)

    aluno.delete()

    return redirect('dashboard')