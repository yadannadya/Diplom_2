from faker import Faker

faker = Faker()

def faker_user():
    return {
        "email": faker.email(),
        "password": faker.password(length = 10, special_chars=True, digits=True, upper_case=True, lower_case=True),
        "name": faker.first_name()
        }
