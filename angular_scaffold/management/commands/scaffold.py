from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Adds basic structure to basic application'

    def handle(self, *args, **options):
        self.stdout.write('Hello World')