from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from _generate_assets import generate_assets

class Command(BaseCommand):
    help = 'Adds basic structure to basic application'

    def handle(self, *args, **options):
        self.stdout.write('Generating assets directory')
        generate_assets('.')
