# Patient service is the bridge between App and the Data Layer Access layer.
# This layer takes commands from the App, validates the data and manipulates it's data if needed and forwards the command to DAL.

from dal.patientsDAL import PatientDAL

# This method validates the data from submitted for to check the data types and also value ranges be correct
def validate_patient_data(p):
    try:
        val = int(p['gender'])
        if(val < 0 and val > 2):
            return False
        val = int(p['age'])
        if(val <= 0):
            return False
        val = int(p['hypertension'])
        if(val < 0 and val > 1):
            return False
        val = int(p['heart_disease'])
        if(val < 0 and val > 1):
            return False
        val = int(p['ever_married'])
        if(val < 0 and val > 1):
            return False
        val = int(p['work_type'])
        if(val < 0 and val > 4):
            return False
        val = int(p['residence_type'])
        if(val < 0 and val > 1):
            return False
        val = float(p['avg_glucose_level'])
        if(p['bmi'] != None):
            float(p['bmi'])
        val = int(p['smoking_status'])
        if(val < 0 and val > 3):
            return False
        val = int(p['stroke'])
        if(val < 0 and val > 1):
            return False
        
    except ValueError:
        return False

# Do a simple encryption on numerical fields(Glucose level and BMI) befor storing in DB
def encryptValue(val):
    fval = float(val)
    return ((fval * 2) + 666)

# Decrypt numerical fields(Glucose level and BMI) after retrieving from DB
def decryptValue(val):
    fval = float(val)
    return ((fval - 666) / 2)

# When user wants to list all patients, this command is called and it just forwards it to DAL
def get_all_patients():
    patients = PatientDAL.get_all_patients()
    return patients

# Takes Id as an argument and calls appropriate DAL method. If DAL couldn't find the patient, simply returns a code 404
def get_patient_by_id(patient_id):
    try: # Validation check. If argument was not integer, return a Bad request code
        int(patient_id)
    except TypeError:
        return 500
    patient = PatientDAL.get_patient_by_id(patient_id)
    if(patient != 404):
        patient.avg_glucose_level = decryptValue(patient.avg_glucose_level)
        if(patient.bmi != None):
            patient.bmi = decryptValue(patient.bmi)
    return patient

# Forwards Add patient call to DAL
def add_patient(patient_data):
    if(patient_data['bmi'] == ''): # bmi field is Nullable, thats why when inserting/updating to the db, we set it to None if the field is empty
        patient_data['bmi'] = None
    if(validate_patient_data(patient_data) == False): # Validate inputs before sending to DAL
        return 500
    patient_data['avg_glucose_level'] = encryptValue(patient_data['avg_glucose_level'])
    if(patient_data['bmi'] != None):
        patient_data['bmi'] = encryptValue(patient_data['bmi'])
    return PatientDAL.add_patient(patient_data)

# Takes patient ID and updated data as parameters, Gets the patient from DB and then sends the original and updated data to DAL
def update_patient(patient_id, updated_data):
    if(updated_data['bmi'] == ''): # bmi field is Nullable, thats why when inserting/updating to the db, we set it to None if the field is empty
        updated_data['bmi'] = None
    if(validate_patient_data(updated_data) == False): # Validate inputs before sending to DAL
        return 500
    patient = PatientDAL.get_patient_by_id(patient_id)
    if not patient:
        return 404
    updated_data['avg_glucose_level'] = encryptValue(updated_data['avg_glucose_level'])
    if(updated_data['bmi'] != None):
        updated_data['bmi'] = encryptValue(updated_data['bmi'])
    PatientDAL.update_patient(patient, updated_data)
    return 200

# To delete a patient it first searchs for the patient in the DB and if it exists calls the DAL method to delete the patient
def delete_patient(patient_id):
    patient = PatientDAL.get_patient_by_id(patient_id)
    if not patient:
        return 404
    PatientDAL.delete_patient(patient)
    return 200