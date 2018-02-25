from django.core.management.base import BaseCommand
from django.conf import settings

from angular_scaffold.management.commands.helpers._generate_controller import generate_controller
import sys


class Command(BaseCommand):
    args = '<controller_name>'
    help = 'Creates a new controller'

    def handle(self, *args, **options):
        if hasattr(settings, 'BASE_DIR'):
            directory = settings.BASE_DIR
        else:
            directory = '.'
        if not args:
            if (sys.version_info > (3, 0)):
                controller_name = input("Name of the controller: ")
            else:
                controller_name = raw_input("Name of the controller: ")
            generate_controller(directory, controller_name)
            self.stdout.write('Successfully initialized controller "%s"' % controller_name)
        else:
            for controller_name in args:
                generate_controller(directory, controller_name)
                self.stdout.write('Successfully initialized controller "%s"' % controller_name)
