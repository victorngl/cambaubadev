from django.apps import AppConfig


class EscolasConfig(AppConfig):
    name = 'escolas'

    def ready(self):
        import escolas.signals  # noqa
