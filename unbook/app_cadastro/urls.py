from django.urls import path
from . import views
from app_cadastro import views as v


urlpatterns = [
    path('', views.cadastro, name="cadastro"),
    path('sucesso/', views.sucesso, name="sucesso"),
    path('login/', views.login, name="login"),
    path('login/esqueceu/', views.esqueceu, name="esqueceu"),
    path('login/esqueceu/nova-senha/', views.novaSenha, name="novaSenha"),
    path('login/logado/', views.logado, name='logado')
]
