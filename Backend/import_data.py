import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class PatientModel(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    gender = db.Column(db.Integer, nullable = False)
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

db.create_all()

conn = sqlite3.connect('instance/database.db')
cursor = conn.cursor()

df = pd.read_csv('Backend/healthcare-dataset-stroke-data2.csv')

df.to_sql('patient_model', conn, if_exists='append', index=False)

conn.commit()
conn.close()