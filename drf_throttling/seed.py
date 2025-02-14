from faker import Faker
faker = Faker()
from jwt_auth.models import Student

def seed(n = 100):
    for _ in range(n):
        Student.objects.create(
            name = faker.name(),
            age = faker.random_int(min=18, max=25),
            roll = faker.random_int(min=1, max=500),
            city = faker.city()
        )