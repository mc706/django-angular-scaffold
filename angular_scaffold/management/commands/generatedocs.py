from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from _generate_docs import generate_docs

class Command(BaseCommand):
    help = 'Adds a docs folder and some basic documentation'

    def handle(self, *args, **options):
        self.stdout.write('Generating documentation')
        if hasattr(settings, 'BASE_DIR'):
            dir = settings.BASE_DIR
        else:
            dir = '.'
        generate_docs(dir)