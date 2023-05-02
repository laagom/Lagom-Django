from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Show user list'
    
    def handle(self, *args, **options):
        self.stdout.write('show user')