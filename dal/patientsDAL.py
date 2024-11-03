from flask_restful import abort
from sqlalchemy import text
from models.patientModel import db, PatientModel

class PatientDAL:
    # Load all patients from the sqlite DB
    @staticmethod
    def get_all_patients():
        result = db.session.execute(text("SELECT * FROM patient_model"))
        patients = result.fetchall()
        return patients

    # Search for a patient with a patient ID and return it. Otherwise, return code 404 (Not found)
    @staticmethod
    def get_patient_by_id(patient_id):
        result = PatientModel.query.get(patient_id)
        if(result == None):
            abort(404, description="Patient not found")
        return result

    # Add a patient to DB. It takes patient data as object and converts it first to Patient Model. Then saves it in to DB
    @staticmethod
    def add_patient(patient_data):
        new_patient = PatientModel(**patient_data)
        db.session.add(new_patient)
        db.session.commit()
        return new_patient

    # This method takes patient original data and updated data as parameters, then updates all fields to the updated data
    @staticmethod
    def update_patient(patient, updated_data):
        for key, value in updated_data.items():
            setattr(patient, key, value)
        db.session.commit()

    # Simple method to delete a patient from the DB by it's patient ID
    @staticmethod
    def delete_patient(patient):
        db.session.delete(patient)
        db.session.commit()