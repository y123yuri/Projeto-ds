from django.urls import path
from . import views
from app_cadastro import views as v


urlpatterns = [
    # path('', views.cadastro, name="cadastro"),
    path('sucesso/', views.sucesso, name="sucesso"),
]
