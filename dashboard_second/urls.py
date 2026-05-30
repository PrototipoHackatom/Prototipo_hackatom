from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_second, name='dashboard_second')
]
