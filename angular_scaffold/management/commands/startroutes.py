from django.core.management.base import BaseCommand
from django.conf import settings

from angular_scaffold.management.commands.helpers._generate_routes import generate_routes


class Command(BaseCommand):
    help = 'Starts angular routes and adds ngRoutes to the dependenices'

    def handle(self, *args, **options):
        self.stdout.write('Generating routes config file')
        if hasattr(settings, 'BASE_DIR'):
            path = settings.BASE_DIR
        else:
            path = '.'
        generate_routes(path)