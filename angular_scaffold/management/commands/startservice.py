import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from _generate_service import generate_service

class Command(BaseCommand):
    args = '<service_name>'
    help = 'Creates a new service, adds endpoints for list, get, post, put, and delete'

    def handle(self, *args, **options):
        if hasattr(settings, 'BASE_DIR'):
            dir = settings.BASE_DIR
        else:
            dir = '.'
        if not args:
            raise CommandError('Need a service name as an argument')
        for service_name in args:
            generate_service(dir, service_name)
            self.stdout.write('Successfully initialized service "%s"' % service_name)
