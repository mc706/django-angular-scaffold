import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from _generate_controller import generate_controller

class Command(BaseCommand):
    args = '<controller_name>'
    help = 'Creates a new controller'

    def handle(self, *args, **options):
        if hasattr(settings, 'BASE_DIR'):
            dir = settings.BASE_DIR
        else:
            dir = '.'
        if not args:
            controller_name = raw_input("Name of the controller: ")
            generate_controller(dir, controller_name)
            self.stdout.write('Successfully initialized controller "%s"' % controller_name)
        else:
            for controller_name in args:
                generate_controller(dir, controller_name)
                self.stdout.write('Successfully initialized controller "%s"' % controller_name)
