import sys
from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'
    verbose_name = 'Cars Application'

    def ready(self):
        print('cars ready...')
        import cars.signals
