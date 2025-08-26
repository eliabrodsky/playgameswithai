from faker import Faker
from sqlmodel import Session
from .database import engine
from .models import Patient
from datetime import datetime

fake = Faker()

patients = []
for _ in range(5):
    patients.append(
        Patient(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            dob=fake.date_of_birth(minimum_age=18, maximum_age=90),
            last4_ssn=fake.ssn()[-4:],
            address=fake.address(),
            phone=fake.phone_number(),
            email=fake.email(),
            consent_contact=True,
        )
    )

with Session(engine) as session:
    for p in patients:
        session.add(p)
    session.commit()
