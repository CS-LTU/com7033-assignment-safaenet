from flask import Flask, flash, jsonify, redirect, render_template, request, url_for
import requests
from models import NewPatient, Patient

RUNNING_PORT = 5001
RUN_IN_DEBUG_MODE = True
BASE_URL = "http://127.0.0.1:5000/"
NEW_PATIENT_URL = BASE_URL + "AddPatient"

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/add_new_patient_clicked', methods = ['POST'])
def add_new_patient_clicked():
    new_Patient = NewPatient(
        gender = request.form.get('genderOptions'),
        age = request.form.get('age'),
        hypertension = request.form.get('hypertensionOptions'),
        heart_disease = request.form.get('heartDiseaseOptions'),
        ever_married = request.form.get('everMarriedOptions'),
        work_type = request.form.get('workTypeOptions'),
        residence_type = request.form.get('residence_type'),
        avg_glucose_level = request.form.get('avg_glucose_level'),
        bmi = request.form.get('bmi'),
        smoking_status = request.form.get('smoking_status'),
        stroke = request.form.get('strokeOptions')
    )
    new_patient_data = new_Patient.as_json()
    try:
        response = requests.post(NEW_PATIENT_URL, json=new_patient_data)
        if response.status_code == 201:
            return render_template('home.html', has_message=True, message_text="Patient has been successfully added.")
        else:
            return render_template('home.html', has_message=True, message_text=f"There was an error when adding new Patient. Code:{response.status_code}")
    except Exception as e:
        return render_template('home.html', has_message=True, message_text=f"There was an error connecting to the database.")

    

@app.route('/GetPatientById/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    try:
        url = f"http://127.0.0.1:5000/GetById/{patient_id}"
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        patient = Patient.read_from_json(json_data)
        return jsonify({
            "id": patient.id,
            "gender": patient.gender,
            "age": patient.age,
            "hypertension": patient.hypertension,
            "heart_disease": patient.heart_disease,
            "ever_married": patient.ever_married,
            "work_type": patient.work_type,
            "residence_type": patient.residence_type,
            "avg_glucose_level": patient.avg_glucose_level,
            "bmi": patient.bmi,
            "smoking_status": patient.smoking_status,
            "stroke": patient.stroke
        })

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Error fetching data from external API", "details": str(e)}), 500


@app.route('/get_patients', methods=['GET'])
def get_patients():
    try:
        url = "https://external.api/patients"
        response = requests.get(url)
        response.raise_for_status()
        
        json_data = response.json()
        patients = [Patient.read_from_json(patient_data) for patient_data in json_data]
        
        patients_list = [{
            "id": patient.id,
            "gender": patient.gender,
            "age": patient.age,
            "hypertension": patient.hypertension,
            "heart_disease": patient.heart_disease,
            "ever_married": patient.ever_married,
            "work_type": patient.work_type,
            "residence_type": patient.residence_type,
            "avg_glucose_level": patient.avg_glucose_level,
            "bmi": patient.bmi,
            "smoking_status": patient.smoking_status,
            "stroke": patient.stroke
        } for patient in patients]
        
        return jsonify(patients_list)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Error fetching data from external API", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(port=RUNNING_PORT, debug=RUN_IN_DEBUG_MODE)