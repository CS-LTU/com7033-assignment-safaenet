from flask_restful import abort
from sqlalchemy import text
from models.patientModel import db, PatientModel

class PatientDAL:
    @staticmethod
    def get_all_patients():
        result = db.session.execute(text("SELECT * FROM patient_model"))
        patients = result.fetchall()
        return patients

    @staticmethod
    def get_patient_by_id(patient_id):
        result = PatientModel.query.get(patient_id)
        if(result == None):
            abort(404, description="Patient not found")
        return result

    @staticmethod
    def search_patients_by_value(search_value):
        sql_query = text(f"""
            SELECT * FROM patient_model 
            WHERE id = :value OR 
                  age = :value OR 
                  avg_glucose_level = :value OR 
                  bmi = :value
        """)
        result = db.session.execute(sql_query, {'value': search_value})
        return result.fetchall()

    @staticmethod
    def add_patient(patient_data):
        new_patient = PatientModel(**patient_data)
        db.session.add(new_patient)
        db.session.commit()
        return new_patient

    @staticmethod
    def update_patient(patient, updated_data):
        for key, value in updated_data.items():
            setattr(patient, key, value)
        db.session.commit()

    @staticmethod
    def delete_patient(patient):
        db.session.delete(patient)
        db.session.commit()