from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import (
    TurnoEstuda, Aprendizagem, Escolaridade, Entidade, Curso, 
    TurnoVaga, TipoFormacao, AlunoConcluido, AlunoDesistencia
)
from autenticacao.models import Pessoa
from dashboard.models import Aluno

# ... (Mantenha a sua view dashboard igual se ela gerencia apenas Alunos Ativos) ...

# =========================================================================================
# 2. VIEW: SEGUNDA DASHBOARD (CONCLUÍDOS / DESISTENTES) + SALVAR EDIÇÃO
# =========================================================================================
def dashboard_second(request):
    # 1. PROCESSAMENTO DE POST (EDIÇÃO)
    if request.method == 'POST':
        aluno_id = request.POST.get('aluno_id')
        tipo_aluno = request.POST.get('tipo_aluno') # 'concluido' ou 'desistente'
        
        if aluno_id:
            # Identifica em qual tabela salvar baseado em um input hidden que adicionamos no HTML
            if tipo_aluno == 'concluido':
                aluno = get_object_or_404(AlunoConcluido, id=aluno_id)
            else:
                aluno = get_object_or_404(AlunoDesistencia, id=aluno_id)
                
            aluno.nome = request.POST.get('nome')
            aluno.nome_social = request.POST.get('nome_social')
            aluno.email = request.POST.get('email')
            aluno.nome_responsavel = request.POST.get('nome_responsavel')
            aluno.telefone = request.POST.get('telefone')
            aluno.telefone_responsavel = request.POST.get('telefone_responsavel')
            aluno.data_nascimento = request.POST.get('data_nascimento') or None
            
            # Foreign Keys
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

    # 2. PROCESSAMENTO DE GET (FILTROS E RENDERIZAÇÃO)
    search_nome = request.GET.get('nome', '').strip()
    search_profissional = request.GET.get('profissional', '')
    search_cadastrado = request.GET.get('cadastrado_por', '')

    # Busca diretamente nos models específicos solicitados
    concluidos_list = AlunoConcluido.objects.all()
    desistentes_list = AlunoDesistencia.objects.all()

    # Aplicação dos filtros dinâmicos em ambas as listas
    if search_nome:
        concluidos_list = concluidos_list.filter(nome__icontains=search_nome)
        desistentes_list = desistentes_list.filter(nome__icontains=search_nome)
    if search_profissional:
        concluidos_list = concluidos_list.filter(profissional_ref_id=search_profissional)
        desistentes_list = desistentes_list.filter(profissional_ref_id=search_profissional)
    # Nota: Se o campo 'cadastrado_por' estiver comentado no model, o filtro abaixo pode quebrar. 
    # Caso descomente no model, pode descomentar aqui:
    # if search_cadastrado:
    #     concluidos_list = concluidos_list.filter(cadastrado_por_id=search_cadastrado)
    #     desistentes_list = desistentes_list.filter(cadastrado_por_id=search_cadastrado)

    # Contadores reais baseados nos models corretos
    concluidos_count = concluidos_list.count()
    desistentes_count = desistentes_list.count()

    # Paginação separada para cada tabela para não bagunçar a navegação do usuário
    page_concluidos = request.GET.get('page_concluidos')
    page_desistentes = request.GET.get('page_desistentes')

    paginator_c = Paginator(concluidos_list.order_by('nome'), 5)
    paginator_d = Paginator(desistentes_list.order_by('nome'), 5)

    context = {
        'alunos_concluidos': paginator_c.get_page(page_concluidos),
        'alunos_desistentes': paginator_d.get_page(page_desistentes),
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
# 3. VIEWS DE MOVIMENTAÇÃO (Migrando dados entre tabelas)
# =========================================================================================
def mover_para_conclusao(request, aluno_id):
    aluno_ativo = get_object_or_404(Aluno, id=aluno_id)
    
    # Cria o registro na tabela de Concluídos copiando os dados
    AlunoConcluido.objects.create(
        nome=aluno_ativo.nome,
        nome_social=aluno_ativo.nome_social,
        email=aluno_ativo.email,
        nome_responsavel=aluno_ativo.nome_responsavel,
        telefone=aluno_ativo.telefone,
        telefone_responsavel=aluno_ativo.telefone_responsavel,
        data_nascimento=aluno_ativo.data_nascimento,
        profissional_ref=aluno_ativo.profissional_ref,
        turno_estuda=aluno_ativo.turno_estuda,
        aprendizagem=aluno_ativo.aprendizagem,
        escolaridade=aluno_ativo.escolaridade,
        entidade=aluno_ativo.entidade,
        curso=aluno_ativo.curso,
        turno_vaga=aluno_ativo.turno_vaga,
        tipo_formacao=aluno_ativo.tipo_formacao,
        cep=aluno_ativo.cep,
        rua=aluno_ativo.rua,
        numero=aluno_ativo.numero,
        bairro=aluno_ativo.bairro,
        cidade=aluno_ativo.cidade,
        estado=aluno_ativo.estado
    )
    
    # Opcional: Deleta ou altera o status do aluno ativo para não duplicar no painel principal
    aluno_ativo.delete() 
    return redirect('dashboard')


def mover_para_desistencia(request, aluno_id):
    aluno_ativo = get_object_or_404(Aluno, id=aluno_id)
    
    # Cria o registro na tabela de Desistentes copiando os dados
    AlunoDesistencia.objects.create(
        nome=aluno_ativo.nome,
        nome_social=aluno_ativo.nome_social,
        email=aluno_ativo.email,
        nome_responsavel=aluno_ativo.nome_responsavel,
        telefone=aluno_ativo.telefone,
        telefone_responsavel=aluno_ativo.telefone_responsavel,
        data_nascimento=aluno_ativo.data_nascimento,
        profissional_ref=aluno_ativo.profissional_ref,
        turno_estuda=aluno_ativo.turno_estuda,
        aprendizagem=aluno_ativo.aprendizagem,
        escolaridade=aluno_ativo.escolaridade,
        entidade=aluno_ativo.entidade,
        curso=aluno_ativo.curso,
        turno_vaga=aluno_ativo.turno_vaga,
        tipo_formacao=aluno_ativo.tipo_formacao,
        cep=aluno_ativo.cep,
        rua=aluno_ativo.rua,
        numero=aluno_ativo.numero,
        bairro=aluno_ativo.bairro,
        cidade=aluno_ativo.cidade,
        estado=aluno_ativo.estado
    )
    
    # Opcional: Deleta ou altera o status do aluno ativo
    aluno_ativo.delete()
    return redirect('dashboard')