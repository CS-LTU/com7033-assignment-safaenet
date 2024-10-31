from dal.patientsDAL import PatientDAL

def get_all_patients():
    return PatientDAL.get_all_patients()

def get_patient_by_id(patient_id):
    patient = PatientDAL.get_patient_by_id(patient_id)
    if not patient:
        return 404
    return patient

def search_patients_by_value(search_value):
    patients = PatientDAL.search_patients_by_value(search_value)
    if not patients:
        return {"message": "No matching patients found"}, 404
    return patients

def add_patient(patient_data):
    return PatientDAL.add_patient(patient_data)

def update_patient(patient_id, updated_data):
    patient = PatientDAL.get_patient_by_id(patient_id)
    if not patient:
        return 404
    PatientDAL.update_patient(patient, updated_data)
    return 200

def delete_patient(patient_id):
    patient = PatientDAL.get_patient_by_id(patient_id)
    if not patient:
        return 404
    PatientDAL.delete_patient(patient)
    return 200