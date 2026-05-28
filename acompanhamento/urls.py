from django.urls import path
from . import views

urlpatterns = [
    path('graficos/', views.pagina_graficos, name='pagina_graficos'),
    path('api/grafico-alunos/', views.grafico_alunos, name='grafico_alunos'),
]