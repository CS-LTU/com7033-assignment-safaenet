from flask import Flask, jsonify, redirect, render_template, request, session, url_for
import requests
import requests.cookies
from models.models import NewOrUpdatePatient, Patient
from services.userService import authenticate_user, register_user, update_password
from services.patientService import add_patient, delete_patient, get_all_patients, get_patient_by_id, update_patient
from models.patientModel import db

RUNNING_PORT = 5000
RUN_IN_DEBUG_MODE = True

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = '1qaz2wsx'

db.init_app(app)

def isBool(value):
        return value == '1'
    
@app.route('/')
def home():
    if("user" not in session):
        return render_template("login.html")
    else:
        return render_template("home.html")

@app.route('/signin', methods = ['POST'])
def signin():
    username = request.form.get('email')
    password = request.form.get('password')
    result = authenticate_user(username, password)
    if(result):
        session["user"] = username
        return render_template("home.html")
    else:
        return render_template("login.html", has_message = True, message_text = "Invalid Credentials")

@app.route('/signup', methods = ['POST'])
def signup():
    username = request.form.get('emailSignup')
    password = request.form.get('passwordSignup')
    result = register_user(username, password)
    if(result == False):
        return render_template("login.html", has_message = True, message_text = "Error when signing up. Maybe user already exists.")
    return redirect(url_for('home'))

@app.route('/logout', methods = ['POST'])
def logout():
    session.pop("user", None)
    return redirect(url_for('home'))

@app.route('/goto_change_password')
def goto_change_password():
    if("user" not in session):
        return redirect(url_for("home"))
    return render_template("change_password.html")

@app.route('/change_password', methods = ['POST'])
def change_password():
    if("user" not in session):
        return redirect(url_for("home"))
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')
    username = session["user"]
    if(old_password == new_password):
        return render_template('home.html', has_message=True, message_text=f"Old password and new password cannot be the same.")
    if(new_password == confirm_password):
        result = update_password(username, old_password, new_password)
    else:
        return render_template('home.html', has_message=True, message_text=f"New password and confirm password don't match.")
    if(result):
        return redirect(url_for('home'))
    else:
        return render_template('home.html', has_message=True, message_text=f"Old password doesn't match.")

@app.route('/add_new_patient_clicked', methods = ['POST'])
def add_new_patient_clicked():
    if("user" not in session):
        return redirect(url_for("home"))
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
    
    try:
        result = add_patient(vars(new_Patient))
        if result.id > 0:
            return render_template('home.html', has_message=True, message_text=f"Patient has been successfully added. New Id: {result.id}")
        else:
            return render_template('home.html', has_message=True, message_text=f"There was an error when adding new Patient.")
    except Exception as e:
        return render_template('home.html', has_message=True, message_text=f"There was an error connecting to the database. {e}")


@app.route('/update_patient_clicked', methods = ['POST'])
def update_patient_clicked():
    if("user" not in session):
        return redirect(url_for("home"))
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
    try:
        update_data = vars(update_Patient)
        result = update_patient(patient_id, update_data)
        if result == 200:
            return render_template('home.html', has_message=True, message_text="Patient has been successfully updated.")
        else:
            return render_template('home.html', has_message=True, message_text=f"There was an error when updating the Patient.")
    except Exception as e:
        return render_template('home.html', has_message=True, message_text=f"There was an error connecting to the database. {e}")
    

@app.route('/SearchPatientById', methods=['POST'])
def SearchPatientById():
    if("user" not in session):
        return redirect(url_for("home"))
    patientId = request.form.get('search_patient_id')
    try:
        result = get_patient_by_id(patientId)
        
        
        if(result == 404):
            return render_template('home.html', has_message=True, message_text=f"Patient with Id {patientId} was not found.")
        else:
            # patient = Patient.read_from_json(json_data)
            return render_template("home.html", has_patient_to_view=True, patient_to_view=result)
    except Exception as e:
        return render_template('home.html', has_message=True, message_text=f"There was an error connecting to the database. {e}")


@app.route('/DeletePatientById', methods=['POST'])
def DeletePatientById():
    if("user" not in session):
        return redirect(url_for("home"))
    patientId = request.form.get('delete_patient_id')
    try:
        result = delete_patient(patientId)
        if(result == 404):
            return render_template('home.html', has_message=True, message_text=f"Patient with Id {patientId} was not found.")
        else:
            return render_template('home.html', has_message=True, message_text=f"Patient with Id {patientId} has been deleted successfully.")
    except Exception as e:
        return render_template('home.html', has_message=True, message_text=f"There was an error connecting to the database. {e}")


@app.route('/get_patients', methods=['GET'])
def get_patients():
    if("user" not in session):
        return redirect(url_for("home"))
    try:
        result = get_all_patients()
        # patients = [Patient.read_from_json(patient_data) for patient_data in patients_json]        
        return render_template('patients_list.html', Patients = result)

    except requests.exceptions.RequestException as e:
        return render_template('home.html', has_message=True, message_text=f"There was an error connecting to the database. {e}")

if __name__ == '__main__':
    app.run(port=RUNNING_PORT, debug=RUN_IN_DEBUG_MODE)