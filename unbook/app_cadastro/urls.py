from django.urls import path
from . import views
from app_cadastro import views as v
from django.contrib.auth import views as v_senha


urlpatterns = [
    path('', views.cadastro, name="cadastro"),
    path('sucesso/', views.sucesso, name="sucesso"),
    path('login/', views.login_func, name="login_func"),
    path('verificar/<uidb64>/<token>/', views.verificar, name="verificar"),
    path('verificar/ativado/', views.ativado, name="ativado"),
    path('login/esqueceu/', views.esqueceu, name="esqueceu"),
    path('login/esqueceu/nova-senha/<str:token>/', views.novaSenha, name="novaSenha"),#nopva senha
    path('login/logado/', views.logado, name='logado'),
    path('login/logout/', views.logout, name='logout'),
    path('login/esqueceu/email_recupera', views.email_recupera, name='email_recupera'),#nova senha confirma
    path('login/usuario/', views.usuario, name='usuario'),
    path('usuario/', views.usuario, name='usuario'),
    path('trocar_senha/', views.trocar_senha, name='trocar_senha'),
    path('login/username/', views.username, name='username'),
    path('sucesso/nao-recebi', views.nao_recebi, name="nao_recebi"),
    path('sucesso/nao-recebi/envio/', views.envio_novo, name="envio_novo"),
    
]
