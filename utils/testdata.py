from faker import Faker
import random

class TestData:
    def __init__(self):
        self.fake = Faker()

    def get_first_name(self):
        return self.fake.first_name()

    def get_last_name(self):
        return self.fake.last_name()

    def get_middle_name(self):
        return self.fake.middle_name()

    def get_email(self):
        return self.fake.email()

    def get_phone(self):
        self.fake = Faker("en_IN")
        return self.fake.phone_number()    
    
    def date_1(self):
        year = random.randint(1990, 2010)
        month = random.randint(1, 12)
        day = random.randint(1, 28)   
        return f"{year:04d}-{month:02d}-{day:02d}"  
        
    def date_2(self):
        year = random.randint(2011, 2025)
        month = random.randint(1, 12)
        day = random.randint(1, 28)   
        return f"{year:04d}-{month:02d}-{day:02d}"  
            