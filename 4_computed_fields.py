from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str 
    email: EmailStr
    linkedin_url: AnyUrl
    age: int

    weight: float = Field(gt = 0, lt = 120)
    height : float

    married: bool = False

    allergies: List[str]

    contact_details: Dict[str, str]

    @computed_field
    @property

    ## -> float will indicate that the output of this function will be in float.
    def bmi(self) -> float:
        bmi = round((self.weight / self.height ** 2), 2)
        return bmi
    

        

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)

    # Whatever name you gave to function that will be considered as your field value.
    print('BMI', patient.bmi)
    print(patient.contact_details)
    print("updated")

# if we give abc@gmail.com then it will throw an error and if we give abc@hdfc/icici.com then it will work becuase we applied field_validators
patient_info = {'name': 'naman', 'email': 'abc@google.com','linkedin_url': 'https://www.linkedin.com/naman', 'age': '61', 'weight': 78, 'height': 1.72, 'allergies': ['dust'], 'contact_details': { 'phone': '1234567890', 'emergency': '0987654321'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)