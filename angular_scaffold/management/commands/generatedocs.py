from django.core.management.base import BaseCommand
from django.conf import settings

from angular_scaffold.management.commands.helpers._generate_docs import generate_docs


class Command(BaseCommand):
    help = 'Adds a docs folder and some basic documentation'

    def handle(self, *args, **options):
        self.stdout.write('Generating documentation')
        if hasattr(settings, 'BASE_DIR'):
            path = settings.BASE_DIR
        else:
            path = '.'
        generate_docs(path)