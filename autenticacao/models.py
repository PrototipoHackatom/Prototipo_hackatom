from django.db import models

# Funcionário
class Cargo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Local(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Turno(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Unidade(models.Model):
    nome= models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email  = models.EmailField()
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    cargo = models.ManyToManyField(Cargo)
    local = models.ForeignKey(Local, on_delete=models.DO_NOTHING)
    turno = models.ForeignKey(Turno, on_delete=models.DO_NOTHING, null=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.nome
    
