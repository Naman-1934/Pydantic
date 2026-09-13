from pydantic import BaseModel


##### Benefits #####

# Better oraganization of related data (e.g., vitals, address, insurance)
# Reusability: Use visuals in multiple models (e.g. Patient, MedicalRecord)
# Readability: Easier for developers and API consumers to understand
# Validation: Nested models are validated automatically no extra work nedded.

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

# Dictionary of address
address_dict = {'city': 'Vadodara', 'state': 'Gujarat', 'pin': '390009'}

# Object of this address
address1 = Address(**address_dict)

# Dictionary for patient
patient_dict = {'name': 'Naman', 'gender': 'male', 'age': 20, 'address': address1}

# Object of patient 
patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.city)
print(patient1.address.pin)
