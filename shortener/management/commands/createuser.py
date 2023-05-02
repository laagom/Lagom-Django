from django.core.management.base import BaseCommand

from shortener.models import User

class Command(BaseCommand):
    help = 'Create user data'

    def add_arguments(self, parser):
        # parser.add_argument('attrs', nargs='+', type=str)
        parser.add_argument('-n', '--name', required=True, type=str)
        parser.add_argument('-c', '--content', required=True, type=str)

    def handle(self, *args, **options):
        # attrs = options['attrs']
        attrs = [options['name'], options['content']]
        print(attrs)

        user = User.objects.create(name=attrs[0], content=attrs[1])
        self.stdout.write('Complete created user')