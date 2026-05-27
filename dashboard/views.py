from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno, TurnoEstuda, TurnoVaga,Aprendizagem, Escolaridade
from .models import Entidade, Curso, TipoFormacao
from autenticacao.models import Pessoa

def dashboard(request):

    pessoa_id = request.session.get('pessoa_id')

    usuario = Pessoa.objects.get(id=pessoa_id)

    #Pega as informções que estão sendo inseridas no formulário de cadastro do aluno
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


    # Salva as informações na tabela Aluno
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

    #Verifica se o cargo do usuário é professor
    eh_professor = usuario.cargo.filter(
        nome='Professor').exists()
    
    #Verifica se o usuário tem algum cargo de admin cadastrado
    eh_admin = usuario.cargo.filter(
        nome__in=[
        'Coordenador',
        'Diretor de centro de unidade de internação',
        'Diretor de unidade de acolhimento']).exists()
    
    #Se o usuário ter apenas cargo de professor verá apenas os seu alunos cadastrados
    if eh_professor and not eh_admin:

        alunos = Aluno.objects.filter(
        cadastrado_por=usuario)

    #Se o usuário ter caargo de admin verá todos os alunos cadastrados
    else:
        alunos = Aluno.objects.all()

    pessoas = []

    for pessoa in Pessoa.objects.all():

        cargos = pessoa.cargo.values_list(
            'nome',
            flat=True
        )

        # se tiver somente Professor -> não mostra
        if list(cargos) == ['Professor']:
            continue

        pessoas.append(pessoa)

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

        turno_estuda_id = request.POST.get('turno_estuda')
        turno_estuda = TurnoEstuda.objects.get(id=turno_estuda_id)
        aluno.turno_estuda = turno_estuda

        tuno_vaga_id = request.POST.get('turno_vaga')
        turno_vaga = TurnoVaga.objects.get(id=tuno_vaga_id)
        aluno.turno_vaga = turno_vaga

        aprendizagem_id = request.POST.get('aprendizagem')
        aprendizagem = Aprendizagem.objects.get(id=aprendizagem_id)
        aluno.aprendizagem = aprendizagem

        escolaridade_id = request.POST.get('escolaridade')
        escolaridade = Escolaridade.objects.get(id=escolaridade_id)
        aluno.escolaridade = escolaridade

        entidade_id = request.POST.get('entidade')
        entidade = Entidade.objects.get(id=entidade_id)
        aluno.entidade = entidade

        curso_id = request.POST.get('curso')
        curso = Curso.objects.get(id=curso_id)
        aluno.curso = curso

        tipo_formacao_id = request.POST.get('tipo_formacao')
        tipo_formacao = TipoFormacao.objects.get(id=tipo_formacao_id)
        aluno.tipo_formacao = tipo_formacao




        aluno.save()

    return redirect('dashboard')

def excluir_aluno(request, id):

    aluno = get_object_or_404(Aluno, id=id)

    aluno.delete()

    return redirect('dashboard')