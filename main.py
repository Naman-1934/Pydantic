from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float

    # We can also set a default value from here and if we don't give any value in the object then it will considered this value as a default.
    married: bool = False

    # we don't use list becuase we don't only validate the list but we validate the list and the entered values in the list are also string
    # and that's why we use List[str].
    # Now allergies will be optional because we use Optional[List[str]] and we have to give a default value which is None.
    allergies: Optional[List[str]] = None

    # we don't use list becuase we don't only validate the dictionary but we validate the dictionary and the entered keys and values both should be string and that's why we use Dict[str, str].
    contact_details: Dict[str, str]

# Now, we got the patient1 object with the data from the patient_info dictionary and we can use that object to insert the data into the database.
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted")

patient_info = {'name': 'naman', 'email': 'abc@gmail.com','linkedin_url': 'https://www.linkedin.com/naman', 'age': 24, 'weight': 78, 'contact_details': { 'phone': '1234567890'}}

# patient_info is a dictionary so, we need to unpack that dictionary using ** operator.

# 1) on the patient_info data apply that Patient rule like name:str, age:int and everything is fine and 
# applied and we get the object patient1. 
patient1 = Patient(**patient_info)

insert_patient_data(patient1)