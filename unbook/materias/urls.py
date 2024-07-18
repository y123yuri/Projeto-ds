from django.urls import path
from . import views
from app_cadastro import views as v
from django.urls import path, include

urlpatterns = [
    path('', views.home, name="home"),
    path('Quem_somos/', views.somos, name='somos'),
    path('pesquisa_prof/', views.pesquisa),
    path('pesquisa_materia/', views.pesquisa_materias),
    path('perfil/', views.perfil, name="perfil"),
    path("professor/<str:nome>", views.professor, name="professor"),
    path('pesquisa_turma/', views.pesquisa_turma),
    path("materia/<str:codigo>/<str:nome>", views.materia, name='materia'),
    path("materia/<str:codigo>/<str:nome>/videos", views.videos, name='videos'),
    path("materia/<str:codigo>/<str:nome>/resumos", views.resumos, name='resumos'),
    path("materia/<str:codigo>/<str:nome>/atividades", views.atividades, name='atividades'),
    path("avaliacao/", views.avaliacao, name="avaliacao"),
    path("denuncia/", views.denuncia, name="denuncia"),
    path("comentario/", views.comentarios, name='comentarios'),
    path("Tutorial", views.tutorial, name='tutorial'),
    path("like/", views.like, name="like"),
    path("video/", views.add_video, name="video"),
    path("atividade/", views.add_atividade, name="atividade"),
    path("resumo/", views.add_resumo, name="resumo"),
    path('deletar/<int:comentario_id>/', views.deletar_comentario, name='deletar_comentario'),
    path('curtir_video/', views.like_video , name='curtir_video'),
    path('curtir_resumo/', views.like_resumo , name='curtir_resumo'),
    path('editar-comentario/<int:comentario_id>/', views.editar_comentario, name='editar_comentario'),
    

]