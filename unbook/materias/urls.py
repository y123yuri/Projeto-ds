from django.urls import path
from . import views
from app_cadastro import views as v
from django.urls import path, include

urlpatterns = [
    path('UnBook', views.home, name="home"),
    path('Quem_somos/', views.somos, name='somos'),
    path('pesquisa_prof/', views.pesquisa),
    path('pesquisa_materia/', views.pesquisa_materias),
]