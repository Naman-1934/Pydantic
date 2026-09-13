from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str 
    email: EmailStr
    linkedin_url: AnyUrl
    age: int

    weight: float = Field(gt = 0, lt = 120)

    married: bool = False

    allergies: List[str]

    contact_details: Dict[str, str]

# Model Validor will give you a authority to combine multiple field and do the data validation.
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patient is older than 60 must have an emergency contact")
        else:
            return model
        

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("updated")

# if we give abc@gmail.com then it will throw an error and if we give abc@hdfc/icici.com then it will work becuase we applied field_validators
patient_info = {'name': 'naman', 'email': 'abc@google.com','linkedin_url': 'https://www.linkedin.com/naman', 'age': '61', 'weight': 78, 'allergies': ['dust'], 'contact_details': { 'phone': '1234567890', 'emergency': '0987654321'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)