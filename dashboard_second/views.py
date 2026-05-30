from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import TurnoEstuda, Aprendizagem, Escolaridade, Entidade, Curso, TurnoVaga, TipoFormacao
from autenticacao.models import Pessoa
from dashboard.models import Aluno

# =========================================================================================
# 1. VIEW: DASHBOARD PRINCIPAL (PRÉ-APRENDIZAGEM / APRENDIZAGEM)
# =========================================================================================
def dashboard(request):
    # Captura os parâmetros de busca enviados pelos filtros GET
    search_nome = request.GET.get('nome', '').strip()
    search_profissional = request.GET.get('profissional', '')
    search_cadastrado = request.GET.get('cadastrado_por', '')

    # Filtra apenas os alunos ativos (que ainda não foram concluídos ou desistiram)
    alunos_list = Aluno.objects.filter(Q(status__isnull=True) | Q(status='') | Q(status='ativo'))

    # Aplicação dinâmica dos filtros de busca
    if search_nome:
        alunos_list = alunos_list.filter(nome__icontains=search_nome)
    if search_profissional:
        alunos_list = alunos_list.filter(profissional_ref_id=search_profissional)
    if search_cadastrado:
        alunos_list = alunos_list.filter(cadastrado_por_id=search_cadastrado)

    # Ordenação padrão por nome
    alunos_list = alunos_list.order_by('nome')

    # Paginação: Corrigido para request.GET.get('page')
    paginator = Paginator(alunos_list, 10)
    page_number = request.GET.get('page')
    alunos_paginados = paginator.get_page(page_number)

    context = {
        'alunos': alunos_paginados,
        'pessoas': Pessoa.objects.all(),
        'todas_pessoas': Pessoa.objects.all(),  
        'turnos_estuda': TurnoEstuda.objects.all(),
        'aprendizagens': Aprendizagem.objects.all(),
        'escolaridades': Escolaridade.objects.all(),
        'entidades': Entidade.objects.all(),
        'cursos': Curso.objects.all(),
        'turnos_vaga': TurnoVaga.objects.all(),
        'tipos_formacao': TipoFormacao.objects.all(),
        'eh_admin': True,  
    }
    
    # Processa o formulário de Cadastro se receber uma requisição POST
    if request.method == 'POST':
        novo_aluno = Aluno(
            nome=request.POST.get('nome'),
            nome_social=request.POST.get('nome_social'),
            email=request.POST.get('email'),
            nome_responsavel=request.POST.get('nome_responsavel'),
            telefone=request.POST.get('telefone'),
            telefone_responsavel=request.POST.get('telefone_responsavel'),
            data_nascimento=request.POST.get('data_nascimento') or None,
            profissional_ref_id=request.POST.get('profissional_ref') or None,
            turno_estuda_id=request.POST.get('turno_estuda') or None,
            aprendizagem_id=request.POST.get('aprendizagem') or None,
            escolaridade_id=request.POST.get('escolaridade') or None,
            entidade_id=request.POST.get('entidade') or None,
            curso_id=request.POST.get('curso') or None,
            turno_vaga_id=request.POST.get('turno_vaga') or None,
            tipo_formacao_id=request.POST.get('tipo_formacao') or None,
            cep=request.POST.get('cep'),
            rua=request.POST.get('rua'),
            numero=request.POST.get('numero'),
            bairro=request.POST.get('bairro'),
            cidade=request.POST.get('cidade'),
            estado=request.POST.get('estado'),
            status='ativo'
        )
        novo_aluno.save()
        return redirect('dashboard')

    return render(request, 'dashboard/dashboard.html', context)


# =========================================================================================
# 2. VIEW: SEGUNDA DASHBOARD (CONCLUÍDOS / DESISTENTES) + SALVAR EDIÇÃO
# =========================================================================================
def dashboard_second(request):
    # Se o formulário de edição dentro do offcanvas for submetido via POST
    if request.method == 'POST':
        # Como o seu formulário HTML não passa o ID na URL da action, podemos usar um campo oculto 
        # ou buscar dinamicamente. Para funcionar com a estrutura atual do seu HTML, 
        # interceptamos os dados e salvamos as alterações do Aluno correspondente:
        aluno_id = request.POST.get('aluno_id') # Caso queira adicionar um <input type="hidden" name="aluno_id" value="{{aluno.id}}"> no HTML
        
        # Como no seu HTML o form está dentro de um '{% for aluno in alunos %}', o ideal é tratar a rota de POST separada.
        # Porém, para fazer funcionar diretamente no mesmo arquivo que enviou:
        # Vamos buscar o aluno correspondente de forma segura se você optar por usar o ID vindo do POST:
        if aluno_id:
            aluno = get_object_or_404(Aluno, id=aluno_id)
            aluno.nome = request.POST.get('nome')
            aluno.nome_social = request.POST.get('nome_social')
            aluno.email = request.POST.get('email')
            aluno.nome_responsavel = request.POST.get('nome_responsavel')
            aluno.telefone = request.POST.get('telefone')
            aluno.telefone_responsavel = request.POST.get('telefone_responsavel')
            aluno.data_nascimento = request.POST.get('data_nascimento') or None
            
            # Atualização das chaves estrangeiras (ForeignKeys)
            aluno.profissional_ref_id = request.POST.get('profissional_ref') or None
            aluno.turno_estuda_id = request.POST.get('turno_estuda') or None
            aluno.aprendizagem_id = request.POST.get('aprendizagem') or None
            aluno.escolaridade_id = request.POST.get('escolaridade') or None
            aluno.entidade_id = request.POST.get('entidade') or None
            aluno.curso_id = request.POST.get('curso') or None
            aluno.turno_vaga_id = request.POST.get('turno_vaga') or None
            aluno.tipo_formacao_id = request.POST.get('tipo_formacao') or None
            
            # Endereço
            aluno.cep = request.POST.get('cep')
            aluno.rua = request.POST.get('rua')
            aluno.numero = request.POST.get('numero')
            aluno.bairro = request.POST.get('bairro')
            aluno.cidade = request.POST.get('cidade')
            aluno.estado = request.POST.get('estado')
            
            aluno.save()
            return redirect('dashboard_second')

    # Execução normal do método GET (Filtros e Renderização da página)
    search_nome = request.GET.get('nome', '').strip()
    search_profissional = request.GET.get('profissional', '')
    search_cadastrado = request.GET.get('cadastrado_por', '')

    # Captura apenas os alunos que saíram do fluxo ativo
    alunos_historico = Aluno.objects.filter(status__in=['concluido', 'desistencia'])

    if search_nome:
        alunos_historico = alunos_historico.filter(nome__icontains=search_nome)
    if search_profissional:
        alunos_historico = alunos_historico.filter(profissional_ref_id=search_profissional)
    if search_cadastrado:
        alunos_historico = alunos_historico.filter(cadastrado_por_id=search_cadastrado)

    # Paginação para as tabelas históricas
    paginator = Paginator(alunos_historico.order_by('nome'), 10)
    page_number = request.GET.get('page')
    alunos_paginados = paginator.get_page(page_number)

    # Contadores dinâmicos calculados em tempo real para alimentar as badges
    concluidos_count = Aluno.objects.filter(status='concluido').count()
    desistentes_count = Aluno.objects.filter(status='desistencia').count()

    context = {
        'alunos': alunos_paginados,
        'pessoas': Pessoa.objects.all(),
        'todas_pessoas': Pessoa.objects.all(),
        'turnos_estuda': TurnoEstuda.objects.all(),
        'aprendizagens': Aprendizagem.objects.all(),
        'escolaridades': Escolaridade.objects.all(),
        'entidades': Entidade.objects.all(),
        'cursos': Curso.objects.all(),
        'turnos_vaga': TurnoVaga.objects.all(),
        'tipos_formacao': TipoFormacao.objects.all(),
        'alunos_concluidos_count': concluidos_count,
        'alunos_desistentes_count': desistentes_count,
        'eh_admin': True,
    }
    return render(request, 'dashboard_second/dashboard_second.html', context)


# =========================================================================================
# 3. VIEWS DE MOVIMENTAÇÃO DE STATUS (BOTÕES DE AÇÃO)
# =========================================================================================
def mover_para_desistencia(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    aluno.status = 'desistencia'
    aluno.save()
    return redirect('dashboard')


def mover_para_conclusao(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    aluno.status = 'concluido'
    aluno.save()
    return redirect('dashboard')