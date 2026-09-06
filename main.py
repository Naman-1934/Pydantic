from pydantic import BaseModel

class Patient(BaseModel):

    name: str
    age: int

# Now, we got the patient1 object with the data from the patient_info dictionary and we can use that object to insert the data into the database.
def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print("inserted")

patient_info = {'name': 'naman', 'age': 24}

# patient_info is a dictionary so, we need to unpack that dictionary using ** operator.

# 1) on the patient_info data apply that Patient rule like name:str, age:int and everything is fine and 
# applied and we get the object patient1. 
patient1 = Patient(**patient_info)

insert_patient_data(patient1)