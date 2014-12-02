from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from _generate_debugger import generate_debugger


class Command(BaseCommand):
    args = '<password>'
    help = 'Adds a debugger config that overrides console log with angular.$log'

    def handle(self, *args, **options):
        if not args:
            raise CommandError('Need to add a password argument')
        for password in args:
            self.stdout.write('Generating debugger')
            if hasattr(settings, 'BASE_DIR'):
                path = settings.BASE_DIR
            else:
                path = '.'
            generate_debugger(path, password)