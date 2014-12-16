import os

from django.core.management.base import BaseCommand
from django.conf import settings

from angular_scaffold.management.commands.helpers._generate_view import generate_view


class Command(BaseCommand):
    args = '<view_name view_name ...>'
    help = 'Creates a new view, adds the styles, and imports it'

    def handle(self, *args, **options):
        if hasattr(settings, 'BASE_DIR'):
            dir = settings.BASE_DIR
        else:
            dir = '.'
        if not args:
            view_name = raw_input("View Name: ")
            generate_view(os.path.join(dir, 'assets'), view_name)
            self.stdout.write('Successfully initialized view "%s"' % view_name)
        else:
            for view_name in args:
                generate_view(os.path.join(dir, 'assets'), view_name)
                self.stdout.write('Successfully initialized view "%s"' % view_name)
