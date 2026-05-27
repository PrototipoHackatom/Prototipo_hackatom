from django.contrib import admin
from .models import Pessoa, Cargo, Local, Turno, Unidade

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'local','turno')
    search_fields = ('nome', 'email',)
    list_filter = ('cargo','local')
admin.site.register(Cargo)
admin.site.register(Local)
admin.site.register(Turno)
admin.site.register(Unidade)
