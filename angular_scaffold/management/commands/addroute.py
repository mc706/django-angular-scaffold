from django.core.management.base import BaseCommand
from django.conf import settings

from _add_route import add_route


class Command(BaseCommand):
    help = 'Adds a route'

    def handle(self, *args, **options):
        self.stdout.write('Generating assets directory')
        if hasattr(settings, 'BASE_DIR'):
            directory = settings.BASE_DIR
        else:
            directory = '.'
        add_route(directory)


