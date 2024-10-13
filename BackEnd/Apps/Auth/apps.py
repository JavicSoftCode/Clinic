from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BackEnd.Apps.Auth'

    def ready(self):
        # Importar el archivo de señales para que se registren
        import BackEnd.Apps.Auth.signals
