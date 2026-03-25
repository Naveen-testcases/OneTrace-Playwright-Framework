from faker import Faker

fake = Faker()


def generate_test_data():
    serial = f"SN-{fake.random_number(digits=6)}"
    po = f"PON-{fake.random_number(digits=6)}"
    description = fake.word()
    comments = f"AutoTest-{fake.random_number(digits=5)}"

    return serial, po, description, comments