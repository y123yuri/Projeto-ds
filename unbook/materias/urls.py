from django.urls import path
from . import views
from app_cadastro import views as v
from django.urls import path, include

urlpatterns = [
    path('', views.home, name="home"),
    path('Quem_somos/', views.somos, name='somos'),
    path('pesquisa_prof/', views.pesquisa),
    path('pesquisa_materia/', views.pesquisa_materias),
    path("materia/<str:codigo>/<str:nome>", views.materia, name='materia'),
    path("professor/<str:nome>", views.professor, name="professor")
]