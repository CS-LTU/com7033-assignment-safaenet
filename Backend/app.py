from flask import Flask, redirect, url_for, request, render_template
from flask_restful import Api, Resource, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.app_context().push()
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class PatientModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    gender = db.Column(db.Boolean, nullable = False)
    age = db.Column(db.Integer, nullable = False)
    hypertension = db.Column(db.Boolean, nullable = False)
    heart_disease = db.Column(db.Boolean, nullable = False)
    ever_married = db.Column(db.Boolean, nullable = False)
    work_type = db.Column(db.Integer, nullable = False)
    Residence_type = db.Column(db.Boolean, nullable = False)
    avg_glucose_level = db.Column(db.Float, nullable = False)
    bmi = db.Column(db.Float, nullable = True)
    smoking_status = db.Column(db.Integer, nullable = False)
    stroke = db.Column(db.Boolean, nullable = False)
    
    def __repr__(self):
        return f"Patient Id: {self.id}, Gender: {self.gender}, Age: {self.age}"


patient_put_parser = reqparse.RequestParser()
patient_put_parser.add_argument('gender', type = bool, help = "gender of the patient", required = True)
patient_put_parser.add_argument('age', type = int, help = "age of the patient", required = True)
patient_put_parser.add_argument('hypertension', type = bool, help = "hypertension of the patient", required = True)
patient_put_parser.add_argument('heart_disease', type = bool, help = "heart disease of the patient", required = True)
patient_put_parser.add_argument('ever_married', type = bool, help = "ever married", required = True)
patient_put_parser.add_argument('work_type', type = int, help = "work type of the patient", required = True)
patient_put_parser.add_argument('Residence_type', type = bool, help = "Residence type of the patient", required = True)
patient_put_parser.add_argument('avg_glucose_level', type = float, help = "avg glucose level of the patient", required = True)
patient_put_parser.add_argument('bmi', type = float, help = "bmi of the patient", required = False)
patient_put_parser.add_argument('smoking_status', type = int, help = "smoking status of the patient", required = True)
patient_put_parser.add_argument('stroke', type = bool, help = "stroke of the patient", required = True)

patient_post_parser = reqparse.RequestParser()
patient_post_parser.add_argument('gender', type=bool, help="Gender of the patient", required=True)
patient_post_parser.add_argument('age', type=int, help="Age of the patient", required=True)
patient_post_parser.add_argument('hypertension', type=bool, help="Hypertension status", required=True)
patient_post_parser.add_argument('heart_disease', type=bool, help="Heart disease status", required=True)
patient_post_parser.add_argument('ever_married', type=bool, help="Ever married status", required=True)
patient_post_parser.add_argument('work_type', type=int, help="Work type", required=True)
patient_post_parser.add_argument('Residence_type', type=bool, help="Residence type", required=True)
patient_post_parser.add_argument('avg_glucose_level', type=float, help="Average glucose level", required=True)
patient_post_parser.add_argument('bmi', type=float, help="BMI", required=False)
patient_post_parser.add_argument('smoking_status', type=int, help="Smoking status", required=True)
patient_post_parser.add_argument('stroke', type=bool, help="Stroke status", required=True)

resource_fields = {
    'id' : fields.Integer,
    'gender' : fields.Boolean,
    'age' : fields.Integer,
    'hypertension' : fields.Boolean,
    'heart_disease' : fields.Boolean,
    'ever_married' : fields.Boolean,
    'work_type' : fields.Integer,
    'Residence_type' : fields.Boolean,
    'avg_glucose_level' : fields.Float,
    'bmi' : fields.Float,
    'smoking_status' : fields.Integer,
    'stroke' : fields.Boolean
}    

# db.create_all()

# @app.route('/')
# def home():
#     return render_template("home.html")




# @app.route('/patients/')
# def patients():
#     return "Welcome to Patients page"


class Patient(Resource):    
    @marshal_with(resource_fields)
    def get(self, patient_id = None, search_value = None):
        if(patient_id):
            result = PatientModel.query.get(patient_id)
            if not result:
                return {"message": "Patient not found"}, 404
            return result
        elif (search_value):
            sql_query = text(f"SELECT * FROM patient_model WHERE id = :value OR age = :value OR avg_glucose_level = :value OR bmi = :value")
            result = db.session.execute(sql_query, {'value': search_value})
            results = result.fetchall()

            patients = [{'id': row[0], 'gender': row[1], 'age': row[2], 'hypertension': row[3],
                        'heart_disease': row[4], 'ever_married': row[5], 'work_type': row[6],
                        'Residence_type': row[7], 'avg_glucose_level': row[8], 'bmi': row[9],
                        'smoking_status': row[10], 'stroke': row[11]} for row in results]

            if not patients:
                return {"message": "No matching patients found"}, 404
            
            return patients
        else:
            results = PatientModel.query.all()
            return results
    
    @marshal_with(resource_fields)
    def post(self):
        args = patient_post_parser.parse_args()
        new_patient = PatientModel(
            gender=args['gender'],
            age=args['age'],
            hypertension=args['hypertension'],
            heart_disease=args['heart_disease'],
            ever_married=args['ever_married'],
            work_type=args['work_type'],
            Residence_type=args['Residence_type'],
            avg_glucose_level=args['avg_glucose_level'],
            bmi=args['bmi'],
            smoking_status=args['smoking_status'],
            stroke=args['stroke']
        )
        db.session.add(new_patient)
        db.session.commit()
        return new_patient, 201
    
    def put(self, patient_id):
        args = patient_put_parser.parse_args()
        patient = PatientModel.query.get(patient_id)
        if not patient:
            return {"message": "Patient not found"}, 404
        patient.gender = args['gender']
        patient.age = args['age']
        patient.hypertension = args['hypertension']
        patient.heart_disease = args['heart_disease']
        patient.ever_married = args['ever_married']
        patient.work_type = args['work_type']
        patient.Residence_type = args['Residence_type']
        patient.avg_glucose_level = args['avg_glucose_level']
        patient.bmi = args['bmi']
        patient.smoking_status = args['smoking_status']
        patient.stroke = args['stroke']
        
        db.session.commit() 

        return {"message": "Patient updated successfully"}, 200
    
    def delete(self, patient_id):
        patient = PatientModel.query.get(patient_id)        
        if not patient:
            return {"message": "Patient not found"}, 404        
        db.session.delete(patient)
        db.session.commit()
        return {"message": "Patient deleted successfully"}, 200
    
    
api.add_resource(Patient, "/GetById/<int:patient_id>", "/AddPatient", "/UpdatePatient/<int:patient_id>", "/GetByValue/<string:search_value>", "/GetAll", "/Delete/<int:patient_id>")

if (__name__ == '__main__'):
    app.run(debug = True)