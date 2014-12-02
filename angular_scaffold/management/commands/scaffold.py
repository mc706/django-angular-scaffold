from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from _generate_assets import generate_assets

class Command(BaseCommand):
    help = 'Adds basic structure to basic application'

    def handle(self, *args, **options):
        self.stdout.write('Generating assets directory')
        if hasattr(settings, 'BASE_DIR'):
            dir = settings.BASE_DIR
        else:
            dir = '.'
        generate_assets(dir)
