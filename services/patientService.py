# Patient service is the bridge between App and the Data Layer Access layer.
# This layer takes commands from the App, manipulates it's data if needed and forwards the command to DAL.

from dal.patientsDAL import PatientDAL

# When user wants to list all patients, this command is called and it just forwards it to DAL
def get_all_patients():
    return PatientDAL.get_all_patients()

# Takes Id as an argument and calls appropriate DAL method. If DAL couldn't find the patient, simply returns a code 404
def get_patient_by_id(patient_id):
    patient = PatientDAL.get_patient_by_id(patient_id)
    if not patient:
        return 404
    return patient

# Search for patient by it's ID
def search_patients_by_value(search_value):
    patients = PatientDAL.search_patients_by_value(search_value)
    if not patients:
        return {"message": "No matching patients found"}, 404
    return patients

# Forwards Add patient call to DAL
def add_patient(patient_data):
    return PatientDAL.add_patient(patient_data)

# Takes patient ID and updated data as parameters, Gets the patient from DB and then sends the original and updated data to DAL
def update_patient(patient_id, updated_data):
    patient = PatientDAL.get_patient_by_id(patient_id)
    if not patient:
        return 404
    PatientDAL.update_patient(patient, updated_data)
    return 200

# To delete a patient it first searchs for the patient in the DB and if it exists calls the DAL method to delete the patient
def delete_patient(patient_id):
    patient = PatientDAL.get_patient_by_id(patient_id)
    if not patient:
        return 404
    PatientDAL.delete_patient(patient)
    return 200