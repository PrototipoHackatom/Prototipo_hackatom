from django.urls import path
from . import views

urlpatterns = [
    path('graficos/', views.pagina_graficos, name='pagina_graficos'),
    path('api/grafico-turno_estuda/', views.grafico_Turno_estuda, name='grafico_Turno_estuda'),
    path('api/grafico-cursos/', views.grafico_cursos, name='grafico_cursos'),
    path('api/grafico-idades/', views.grafico_idade, name='grafico_idade'),
    path('api/grafico-bairros/', views.grafico_bairros, name='grafico_bairros'),
    path('api/grafico-escolaridade/', views.grafico_escolaridade, name='grafico_escolaridade'),
    path('api/grafico-aprendizagem/', views.grafico_aprendizagem, name='grafico_aprendizagem'),
    path('api/grafico-entidade/', views.entidade, name='entidade')
]