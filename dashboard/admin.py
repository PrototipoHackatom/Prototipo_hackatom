from django.contrib import admin
from .models import Aluno,Aprendizagem,Escolaridade, Entidade, Curso
from .models import TipoFormacao, TurnoEstuda, TurnoVaga, Sexo

admin.site.register(Aluno)
admin.site.register(Aprendizagem)
admin.site.register(Escolaridade)
admin.site.register(Entidade)
admin.site.register(Curso)
admin.site.register(TipoFormacao)
admin.site.register(TurnoEstuda)
admin.site.register(TurnoVaga)
admin.site.register(Sexo)
