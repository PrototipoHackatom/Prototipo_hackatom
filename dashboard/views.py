from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno, TurnoEstuda, TurnoVaga,Aprendizagem, Escolaridade
from .models import Entidade, Curso, TipoFormacao
from autenticacao.models import Pessoa
from dashboard_second.models import Desistencia
from django.core.paginator import Paginator

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
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        numero= request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        nome_social = request.POST.get('nome_social')
        
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
            nome_social=nome_social,
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
            tipo_formacao = tipo_formacao,
            cep=cep,
            rua=rua,
            numero=numero,
            bairro=bairro,
            cidade=cidade,
            estado=estado

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
    
    if eh_professor and not eh_admin:

        lista_alunos = Aluno.objects.filter(
            cadastrado_por=usuario
        ).order_by('-id')

    else:

        lista_alunos = Aluno.objects.all().order_by('-id')

    nome = request.GET.get('nome')
    profissional = request.GET.get('profissional')
    cadastrado_por = request.GET.get('cadastrado_por')


# filtrar por nome
    if nome:

            lista_alunos = lista_alunos.filter(
                nome__icontains=nome
        )


# filtrar por profissional responsável
    if profissional:

        lista_alunos = lista_alunos.filter(
        profissional_ref__id=profissional
    )


# somente admin pode filtrar por quem cadastrou
    if eh_admin and cadastrado_por:

        lista_alunos = lista_alunos.filter(
            cadastrado_por__id=cadastrado_por
        )

    # paginação
    paginator = Paginator(lista_alunos, 6)

    page = request.GET.get('page')

    alunos = paginator.get_page(page)

    pessoas = []

    for pessoa in Pessoa.objects.all():

        cargos = list(
            pessoa.cargo.values_list(
                'nome',
                flat=True
            )
        )

        if cargos == ['Professor']:
            continue

        pessoas.append(pessoa)


# =========================
# LISTA PARA FILTRO ADMIN
# MOSTRA TODOS
# =========================

    todas_pessoas = Pessoa.objects.all()

    turnos_estuda = TurnoEstuda.objects.all()
    turno_vaga = TurnoVaga.objects.all()
    aprendizagem = Aprendizagem.objects.all()
    escolaridade = Escolaridade.objects.all()
    entidade = Entidade.objects.all()
    curso = Curso.objects.all()
    tipo_formacao = TipoFormacao.objects.all()
    desistencia = Desistencia.objects.all()

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
            'tipo_formacao': tipo_formacao,
            'eh_admin': eh_admin,
            'todas_pessoas': todas_pessoas,
            'desistencia': desistencia
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
        aluno.cep = request.POST.get('cep')
        aluno.rua = request.POST.get('rua')
        aluno.numero= request.POST.get('numero')
        aluno.bairro = request.POST.get('bairro')
        aluno.cidade = request.POST.get('cidade')
        aluno.estado = request.POST.get('estado')
        aluno.nome_social = request.POST.get('nome_social')

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