from django.core.management.base import BaseCommand
from django.conf import settings

from angular_scaffold.management.commands.helpers._generate_assets import generate_assets


class Command(BaseCommand):
    help = 'Adds basic structure to basic application'

    def handle(self, *args, **options):
        self.stdout.write('Generating assets directory')
        if hasattr(settings, 'BASE_DIR'):
            directory = settings.BASE_DIR
        else:
            directory = '.'
        generate_assets(directory)
        if not settings.STATICFILES_DIRS:
            settings_module = settings.SETTINGS_MODULE
            settings_file = settings_module.replace('.', '/') + '.py'
            with open(directory + '/' + settings_file, 'a') as conf:
                if not settings.BASE_DIR:
                    conf.write("BASE_DIR = os.path.dirname(os.path.dirname(__file__))\n")
                conf.write('STATICFILES_DIRS = (BASE_DIR + "/assets",)')


