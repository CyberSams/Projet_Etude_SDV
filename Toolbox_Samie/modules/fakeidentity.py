from faker import Faker
import random
import datetime

def generate_age():
    return random.randint(18, 90)

def generate_birthdate(age):
    year = datetime.datetime.now().year - age
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.datetime(year, month, day).strftime("%Y-%m-%d")

def get_fake_instance(locale):
    return Faker(locale)

def generate_name(fake_instance):
    return fake_instance.name()

def generate_job(fake_instance):
    return fake_instance.job()

def generate_address(fake_instance):
    return fake_instance.address()

def generate_email(fake_instance):
    return fake_instance.email()

def generate_fake_identity(locale):
    fake_instance = get_fake_instance(locale)
    name = generate_name(fake_instance)
    age = generate_age()
    birthdate = generate_birthdate(age)
    address = generate_address(fake_instance)
    job = generate_job(fake_instance)
    email = generate_email(fake_instance)

    fake_identity = {
        'Name': name,
        'Age': age,
        'Birthdate': birthdate,
        'Address': address,
        'Job': job,
        'Email': email
    }

    fake_data = "\n\n===================\n"
    fake_data += "Fausse Identité\n"
    fake_data += "===================\n"

    for element, value in fake_identity.items():
        fake_data += f"{element}\t=>\t{value}\n"
    
    return fake_data