from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Work Type:
#     CHILDREN = 0
#     GOVERNMENT = 1
#     PRIVATE = 2
#     SELF_EMPLOYED = 3
#     NEVER_WORKED = 4

# Smoking Status:
#     NEVER_SMOKED = 0
#     SMOKES = 1
#     FORMERLY_SMOKED = 2
#     UNKNOWN = 3

# Gender:
#     FEMALE = 0
#     MALE = 1
#     OTHER = 2

# Residence Type:
#     RURAL = False
#     URBAN = True

# This class is Patient Model to declare the Sqlite table for the SQLAlchemy library
class PatientModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gender = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    hypertension = db.Column(db.Boolean, nullable=False)
    heart_disease = db.Column(db.Boolean, nullable=False)
    ever_married = db.Column(db.Boolean, nullable=False)
    work_type = db.Column(db.Integer, nullable=False)
    residence_type = db.Column(db.Boolean, nullable=False)
    avg_glucose_level = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float, nullable=True)
    smoking_status = db.Column(db.Integer, nullable=False)
    stroke = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Patient {self.id}: Gender={self.gender}, Age={self.age}"

# This class is used when user wants to create a new Patient or when updating an existing Patient
class NewOrUpdatePatient:
    gender : int
    age : int
    hypertension : bool
    heart_disease : bool
    ever_married : bool
    work_type : int
    residence_type : bool
    avg_glucose_level : float
    bmi : float
    smoking_status : int
    stroke : bool
        
    def __init__(self, gender, age, hypertension, heart_disease, ever_married, work_type,
                 residence_type, avg_glucose_level, bmi, smoking_status, stroke):
        self.gender = gender
        self.age = age
        self.hypertension = hypertension
        self.heart_disease = heart_disease
        self.ever_married = ever_married
        self.work_type = work_type
        self.residence_type = residence_type
        self.avg_glucose_level = avg_glucose_level
        self.bmi = bmi
        self.smoking_status = smoking_status
        self.stroke = stroke

# This class is used when user loads a patient detail from the DB
class Patient:
    id : int
    gender : int
    age : int
    hypertension : bool
    heart_disease : bool
    ever_married : bool
    work_type : int
    residence_type : bool
    avg_glucose_level : float
    bmi : float
    smoking_status : int
    stroke : bool
    
    def __init__(self, id, gender, age, hypertension, heart_disease, ever_married, work_type,
                 residence_type, avg_glucose_level, bmi, smoking_status, stroke):
        self.id = id
        self.gender = gender
        self.age = age
        self.hypertension = hypertension
        self.heart_disease = heart_disease
        self.ever_married = ever_married
        self.work_type = work_type
        self.residence_type = residence_type
        self.avg_glucose_level = avg_glucose_level
        self.bmi = bmi
        self.smoking_status = smoking_status
        self.stroke = stroke