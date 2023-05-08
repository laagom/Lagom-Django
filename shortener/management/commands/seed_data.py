import random
from faker import Faker
from django_seed import Seed
from django.db import DatabaseError, transaction
from django.core.management.base import BaseCommand

from shortener.models import PayPlan, Users

class Command(BaseCommand):
    help = 'Create data of user and pay plan'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--number', required=True, type=int)

    def handle(self, *args, **options):
        number = options['number']
        price = lambda x: random.randint(000000, 999999)
        faker = Faker()
        
        with transaction.atomic():
            payplan_seeder = Seed.seeder()
            payplan_seeder.add_entity(PayPlan, number, {
                'price': price,
            })
            payplan_seeder.execute()

            payplan = PayPlan.objects.all()
            user_seeder = Seed.seeder()
            user_seeder.add_entity(Users, number, {
                'pay_plan': lambda x: random.choice(payplan),
                'password': lambda x: faker.password(),
            })
            user_seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))



