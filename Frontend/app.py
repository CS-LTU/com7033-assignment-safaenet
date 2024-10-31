from flask import Flask, jsonify, render_template, request
import requests
from flask_cors import CORS
import requests.cookies
from models import NewOrUpdatePatient, Patient

RUNNING_PORT = 5001
RUN_IN_DEBUG_MODE = True
BASE_URL = "http://127.0.0.1:5000/"
NEW_PATIENT_URL = BASE_URL + "AddPatient"
GET_PATIENT_URL = BASE_URL + "GetById/"
UPDATE_PATIENT_URL = BASE_URL + "UpdatePatient/"
DELETE_PATIENT_URL = BASE_URL + "DeletePatient/"
PATIENTS_LIST_URL = BASE_URL + "GetAll"
SESSION_CHECK_URL = BASE_URL + "SessionCheck"
LOGOUT_URL = BASE_URL + "auth"

app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5000", "supports_credentials": True}})
def isBool(value):
        return value == '1'
    
@app.route('/')
def login():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template("login.html")

@app.route('/logout')
def logout():
    response = requests.delete(LOGOUT_URL, cookies=request.cookies)
    print(response.status_code)
    if response.ok:
        requests.cookies = None
        return render_template("login.html")

@app.route('/add_new_patient_clicked', methods = ['POST'])
def add_new_patient_clicked():
    new_Patient = NewOrUpdatePatient(
        gender = request.form.get('genderOptions'),
        age = request.form.get('age'),
        hypertension = isBool(request.form.get('hypertensionOptions')),
        heart_disease = isBool(request.form.get('heartDiseaseOptions')),
        ever_married = isBool(request.form.get('everMarriedOptions')),
        work_type = request.form.get('workTypeOptions'),
        residence_type = isBool(request.form.get('residence_type')),
        avg_glucose_level = request.form.get('avg_glucose_level'),
        bmi = request.form.get('bmi'),
        smoking_status = request.form.get('smoking_status'),
        stroke = isBool(request.form.get('strokeOptions'))
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


@app.route('/update_patient_clicked', methods = ['POST'])
def update_patient_clicked():
    patient_id = request.form.get('patiendId')
    update_Patient = NewOrUpdatePatient(
        gender = request.form.get('genderOptions'),
        age = request.form.get('age'),
        hypertension = isBool(request.form.get('hypertensionOptions')),
        heart_disease = isBool(request.form.get('heartDiseaseOptions')),
        ever_married = isBool(request.form.get('everMarriedOptions')),
        work_type = request.form.get('workTypeOptions'),
        residence_type = isBool(request.form.get('residence_type')),
        avg_glucose_level = request.form.get('avg_glucose_level'),
        bmi = request.form.get('bmi'),
        smoking_status = request.form.get('smoking_status'),
        stroke = isBool(request.form.get('strokeOptions'))
    )
    updated_patient_data = update_Patient.as_json()
    try:
        response = requests.put(UPDATE_PATIENT_URL + f"{patient_id}", json=updated_patient_data)
        if response.status_code == 200:
            return render_template('home.html', has_message=True, message_text="Patient has been successfully updated.")
        else:
            return render_template('home.html', has_message=True, message_text=f"There was an error when updating the Patient. Code:{response.status_code}")
    except Exception as e:
        return render_template('home.html', has_message=True, message_text=f"There was an error connecting to the database.")
    

@app.route('/SearchPatientById', methods=['POST'])
def SearchPatientById():
    patientId = request.form.get('search_patient_id')
    try:
        response = requests.get(GET_PATIENT_URL + f"{patientId}", cookies=request.cookies)
        if(response.status_code != 200):
            return render_template('home.html', has_message=True, message_text=f"Patient with Id {patientId} was not found. Code:{response.status_code}")
        else:
            json_data = response.json()
            patient = Patient.read_from_json(json_data)
            return render_template("home.html", has_patient_to_view=True, patient_to_view=patient)
    except Exception as e:
        return render_template('home.html', has_message=True, message_text=f"There was an error connecting to the database.")


@app.route('/DeletePatientById', methods=['POST'])
def DeletePatientById():
    patientId = request.form.get('delete_patient_id')
    try:
        response = requests.delete(DELETE_PATIENT_URL + f"{patientId}")
        if(response.status_code != 200):
            return render_template('home.html', has_message=True, message_text=f"Patient with Id {patientId} was not found. Code:{response.status_code}")
        else:
            return render_template('home.html', has_message=True, message_text=f"Patient with Id {patientId} has been deleted successfully.")
    except Exception as e:
        return render_template('home.html', has_message=True, message_text=f"There was an error connecting to the database.")


@app.route('/get_patients', methods=['GET'])
def get_patients():
    try:
        response = requests.get(PATIENTS_LIST_URL, cookies=request.cookies)
        response.raise_for_status()
        patients_json = response.json()
        patients = [Patient.read_from_json(patient_data) for patient_data in patients_json]        
        return render_template('patients_list.html', Patients = patients)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Error fetching data from API", "details": str(e)}), 500

def checkSession():
    response = requests.get(SESSION_CHECK_URL)
    if response.ok:
        result = response.json()
        if not result['loggedIn']:
            login()
    else:
        login()

if __name__ == '__main__':
    app.run(port=RUNNING_PORT, debug=RUN_IN_DEBUG_MODE)