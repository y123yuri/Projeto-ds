from django.urls import path
from . import views
from app_cadastro import views as v


urlpatterns = [
    path('', views.home, name="home"),
]