from .models import Name
from faker import Faker
fake = Faker()


def seed_db(n):
    for i in range(0,n):
        Name.objects.create(
            name = fake.name()
        )
        

