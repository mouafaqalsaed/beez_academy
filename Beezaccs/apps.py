from django.apps import AppConfig


class BeezaccsConfig(AppConfig):
    name = 'Beezaccs'

    def ready(self):
        import Beezaccs.signals