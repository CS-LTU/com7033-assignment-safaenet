from dal import PatientDAL

class PatientService:
    @staticmethod
    def get_all_patients():
        return PatientDAL.get_all_patients()

    @staticmethod
    def get_patient_by_id(patient_id):
        patient = PatientDAL.get_patient_by_id(patient_id)
        if not patient:
            return {"message": "Patient not found"}, 404
        return patient

    @staticmethod
    def search_patients_by_value(search_value):
        patients = PatientDAL.search_patients_by_value(search_value)
        if not patients:
            return {"message": "No matching patients found"}, 404
        return patients

    @staticmethod
    def add_patient(patient_data):
        return PatientDAL.add_patient(patient_data)

    @staticmethod
    def update_patient(patient_id, updated_data):
        patient = PatientDAL.get_patient_by_id(patient_id)
        if not patient:
            return {"message": "Patient not found"}, 404
        PatientDAL.update_patient(patient, updated_data)
        return {"message": "Patient updated successfully"}, 200

    @staticmethod
    def delete_patient(patient_id):
        patient = PatientDAL.get_patient_by_id(patient_id)
        if not patient:
            return {"message": "Patient not found"}, 404
        PatientDAL.delete_patient(patient)
        return {"message": "Patient deleted successfully"}, 200