from django.core.management.base import BaseCommand
from django.conf import settings

from angular_scaffold.management.commands.helpers._generate_csrf import generate_csrf


class Command(BaseCommand):
    help = 'Adds the CSRF Token to the headers for your services'

    def handle(self, *args, **options):
        self.stdout.write('Generating run config file')
        if hasattr(settings, 'BASE_DIR'):
            path = settings.BASE_DIR
        else:
            path = '.'
        generate_csrf(path)