from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str 
    email: EmailStr
    linkedin_url: AnyUrl
    age: int

    weight: float = Field(gt = 0, lt = 120)

    married: bool = False

    allergies: List[str]

    contact_details: Dict[str, str]


# field_validator is a class method which is used to validate the field values and after this you need to compulsory define the @classmethod.
    @field_validator('email')
    @classmethod

    # We give cls as a parameter because if we have multple classed then we can access inside this function.
    # value is nothing but a email address.
    def email_validator(cls, value):

        valid_domain = ['google.com', 'youtube.com', 'linkedin.com']

        # Split the email address from the '@' symbol to get the domain part
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid email domain.')

        return value  

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()  

# mode = before will considered the age value before the type conversion which means if you give age as a string then it will throw an error becuase in the condition 0 < value < 100 value considered the before type conversion value that is why it will not compare integer with a string.

# mode = after will considered the age value after the type conversion which means if you give age as a string then it will work.
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted")

# if we give abc@gmail.com then it will throw an error and if we give abc@hdfc/icici.com then it will work becuase we applied field_validators
patient_info = {'name': 'naman', 'email': 'abc@google.com','linkedin_url': 'https://www.linkedin.com/naman', 'age': '24', 'weight': 78, 'allergies': ['dust'], 'contact_details': { 'phone': '1234567890'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)