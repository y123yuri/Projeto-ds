from django.apps import AppConfig

class AppCadastroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_cadastro'
    def ready(self):
        import app_cadastro.signals