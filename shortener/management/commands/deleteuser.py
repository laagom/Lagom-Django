from django.core.management.base import BaseCommand

from shortener.models import User

class Command(BaseCommand):
    help = 'Delete user data'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=str)

    def handle(self, *args, **options):
        users = options['user_id']
        print(users)

        for user_id in users:
            user = User.objects.filter(id=str(user_id)).last()
            user.delete()
            self.stdout.write(f'delete user {user_id}')
