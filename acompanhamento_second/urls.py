from django.urls import path
from . import views

urlpatterns = [
    # Mudei de '' para 'acompanhamento/'
    path('graficos_second/', views.grafico, name='graficos_second'),
    path('api/grafico-conclusao_desistencia/', views.conclusao_desistencia, name='conclusao_desistencia'),
    path('api/grafico-desistencia/', views.desistencia, name='desistencia'),
    path('api/grafico-sexo_conclusao/', views.sexo_conclusao, name='sexo_conclusao')
]