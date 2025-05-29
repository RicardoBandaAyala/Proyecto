from django.apps import AppConfig


class ReservasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservas'

    def ready(self):
        # Importar señales aquí para asegurarse de que se registren al iniciar la aplicación
        import reservas.signals
