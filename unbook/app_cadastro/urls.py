from django.urls import path
from . import views
from app_cadastro import views as v
from django.contrib.auth import views as v_senha


urlpatterns = [
    path('', views.cadastro, name="cadastro"),
    path('sucesso/', views.sucesso, name="sucesso"),
    path('login/', views.login_func, name="login_func"),
    path('login/esqueceu/', views.esqueceu, name="esqueceu"),
    path('login/esqueceu/email_recupera', views.email_recupera, name='email_recupera'),#nova senha confirma
    path('login/esqueceu/nova-senha/<str:token>/', views.novaSenha, name="novaSenha"),#nopva senha
    path('login/logado/', views.logado, name='logado'),
    path('login/logout/', views.logout, name='logout'),
    
    # path('login/esqueceu/nova_senha_trocada',views.nova_senha_trocada, name='nova_senha_trocada'),
    
]
