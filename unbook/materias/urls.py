from django.urls import path
from . import views
from app_cadastro import views as v
from django.urls import path, include

urlpatterns = [
    path('', views.home, name="home"),
    path('Quem_somos/', views.somos, name='somos')
]