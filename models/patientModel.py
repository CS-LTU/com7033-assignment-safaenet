from flask_sqlalchemy import SQLAlchemy
from flask_restful import fields

db = SQLAlchemy()

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

resource_fields = {
    'id' : fields.Integer,
    'gender' : fields.Integer,
    'age' : fields.Integer,
    'hypertension' : fields.Boolean,
    'heart_disease' : fields.Boolean,
    'ever_married' : fields.Boolean,
    'work_type' : fields.Integer,
    'residence_type' : fields.Boolean,
    'avg_glucose_level' : fields.Float,
    'bmi' : fields.Float,
    'smoking_status' : fields.Integer,
    'stroke' : fields.Boolean
}