from django.core.management.base import BaseCommand
from django.conf import settings

from angular_scaffold.management.commands.helpers._generate_service import generate_service


class Command(BaseCommand):
    args = '<service_name>'
    help = 'Creates a new service, adds endpoints for list, get, post, put, and delete'

    def handle(self, *args, **options):
        if hasattr(settings, 'BASE_DIR'):
            directory = settings.BASE_DIR
        else:
            directory = '.'
        if not args:
            generate_service(directory)
            print 'Successfully initialized service'
        else:
            for service_name in args:
                generate_service(directory, service_name)
                print 'Successfully initialized service "%s"' % service_name
