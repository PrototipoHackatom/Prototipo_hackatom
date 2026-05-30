from django.db import models
from autenticacao.models import Pessoa
from dashboard.models import TurnoEstuda, TurnoVaga, Aprendizagem,Escolaridade
from dashboard.models import Entidade, Curso, TipoFormacao, Sexo


class AlunoDesistencia(models.Model):
    nome = models.CharField(max_length=200)
    nome_social = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    nome_responsavel = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100, null=True)
    telefone_responsavel = models.CharField(max_length=100)
    data_nascimento = models.DateTimeField()
    profissional_ref = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING, null=True)
    sexo = models.ForeignKey(Sexo, on_delete=models.DO_NOTHING, null=True)
    turno_estuda = models.ForeignKey(TurnoEstuda, on_delete=models.DO_NOTHING, null=True)
    aprendizagem = models.ForeignKey(Aprendizagem, on_delete=models.DO_NOTHING, null=True)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.DO_NOTHING, null=True)
    entidade = models.ForeignKey(Entidade, on_delete=models.DO_NOTHING, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, null=True)
    turno_vaga = models.ForeignKey(TurnoVaga, on_delete=models.DO_NOTHING, null=True)
    tipo_formacao = models.ForeignKey(TipoFormacao, on_delete=models.DO_NOTHING, null=True)
    #cadastrado_por = models.ForeignKey(Pessoa,on_delete=models.DO_NOTHING,related_name='alunos_cadastrados', null=True)
    cep = models.CharField(max_length=9,null=True)
    rua = models.CharField(max_length=255,null=True)
    numero = models.CharField(max_length=20,null=True)
    bairro = models.CharField(max_length=100,null=True)
    cidade = models.CharField(max_length=100,null=True)
    estado = models.CharField(max_length=2,null=True)


    def __str__(self):
        return self.nome



class AlunoConcluido(models.Model):
    nome = models.CharField(max_length=200)
    nome_social = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    nome_responsavel = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100, null=True)
    telefone_responsavel = models.CharField(max_length=100)
    data_nascimento = models.DateTimeField()
    profissional_ref = models.ForeignKey(Pessoa, on_delete=models.DO_NOTHING, null=True)
    sexo = models.ForeignKey(Sexo, on_delete=models.DO_NOTHING, null=True)
    turno_estuda = models.ForeignKey(TurnoEstuda, on_delete=models.DO_NOTHING, null=True)
    aprendizagem = models.ForeignKey(Aprendizagem, on_delete=models.DO_NOTHING, null=True)
    escolaridade = models.ForeignKey(Escolaridade, on_delete=models.DO_NOTHING, null=True)
    entidade = models.ForeignKey(Entidade, on_delete=models.DO_NOTHING, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, null=True)
    turno_vaga = models.ForeignKey(TurnoVaga, on_delete=models.DO_NOTHING, null=True)
    tipo_formacao = models.ForeignKey(TipoFormacao, on_delete=models.DO_NOTHING, null=True)
    #cadastrado_por = models.ForeignKey(Pessoa,on_delete=models.DO_NOTHING,related_name='alunos_cadastrados', null=True)
    cep = models.CharField(max_length=9,null=True)
    rua = models.CharField(max_length=255,null=True)
    numero = models.CharField(max_length=20,null=True)
    bairro = models.CharField(max_length=100,null=True)
    cidade = models.CharField(max_length=100,null=True)
    estado = models.CharField(max_length=2,null=True)


    def __str__(self):
        return self.nome
