from django.core.management.base import BaseCommand
from django.conf import settings

from angular_scaffold.management.commands.helpers._generate_debugger import generate_debugger


class Command(BaseCommand):
    args = '<password>'
    help = 'Adds a debugger config that overrides console log with angular.$log'

    def handle(self, *args, **options):
        self.stdout.write('Generating debugger')
        if hasattr(settings, 'BASE_DIR'):
            path = settings.BASE_DIR
        else:
            path = '.'
        if not args:
            password = raw_input("Password: ")
            generate_debugger(path, password)
        else:
            for password in args:
                generate_debugger(path, password)