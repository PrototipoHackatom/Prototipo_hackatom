from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('editar_aluno/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('excluir_aluno/<int:id>/', views.excluir_aluno, name='excluir_aluno'),
]
