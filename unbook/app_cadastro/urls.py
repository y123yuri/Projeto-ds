from django.urls import path
from . import views
from app_cadastro import views as v


urlpatterns = [
<<<<<<< HEAD
    path('', views.cadastro, name="cadastro"),
=======
    # path('', views.cadastro, name="cadastro"),
>>>>>>> 098859d47ef34f5d02a0d1fbb6c0a66ccd05f8c4
    path('sucesso/', views.sucesso, name="sucesso"),
]
