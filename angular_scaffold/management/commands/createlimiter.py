from django.core.management.base import BaseCommand
from django.conf import settings

from angular_scaffold.management.commands.helpers._generate_limiter import generate_limiter


class Command(BaseCommand):
    help = 'Adds the rootScope Rate limiter for your services'

    def handle(self, *args, **options):
        self.stdout.write('Generating rate limiter run file')
        if hasattr(settings, 'BASE_DIR'):
            path = settings.BASE_DIR
        else:
            path = '.'
        generate_limiter(path)