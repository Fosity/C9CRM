from django.apps import AppConfig


class CarryConfig(AppConfig):
    name = 'carry'

    def ready(self):
        super(CarryConfig, self).ready()

        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('carry')
