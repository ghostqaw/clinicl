from django.apps import AppConfig


class ClinicappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clinicApp'

    def ready(self):
        import clinicApp.signals


