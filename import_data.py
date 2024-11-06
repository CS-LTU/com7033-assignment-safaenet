# import sqlite3
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import pandas as pd

# app = Flask(__name__)
# app.app_context().push()
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)

# class PatientModel(db.Model):
#     id = db.Column(db.Integer, primary_key = True, autoincrement=True)
#     gender = db.Column(db.Integer, nullable = False)
#     age = db.Column(db.Integer, nullable = False)
#     hypertension = db.Column(db.Boolean, nullable = False)
#     heart_disease = db.Column(db.Boolean, nullable = False)
#     ever_married = db.Column(db.Boolean, nullable = False)
#     work_type = db.Column(db.Integer, nullable = False)
#     residence_type = db.Column(db.Boolean, nullable = False)
#     avg_glucose_level = db.Column(db.Float, nullable = False)
#     bmi = db.Column(db.Float, nullable = True)
#     smoking_status = db.Column(db.Integer, nullable = False)
#     stroke = db.Column(db.Boolean, nullable = False)
    
#     def __repr__(self):
#         return f"Patient Id: {self.id}, Gender: {self.gender}, Age: {self.age}"

# db.create_all()

# conn = sqlite3.connect('instance/database.db')
# cursor = conn.cursor()

# df = pd.read_csv('healthcare-dataset-stroke-data2.csv')

# df.to_sql('patient_model', conn, if_exists='append', index=False)

# conn.commit()
# conn.close()




import csv
import sqlite3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from services.patientService import encryptValue
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
    residence_type = db.Column(db.Boolean, nullable = False)
    avg_glucose_level = db.Column(db.Float, nullable = False)
    bmi = db.Column(db.Float, nullable = True)
    smoking_status = db.Column(db.Integer, nullable = False)
    stroke = db.Column(db.Boolean, nullable = False)
    
    def __repr__(self):
        return f"Patient Id: {self.id}, Gender: {self.gender}, Age: {self.age}"

db.create_all()

# Connect to the database
conn = sqlite3.connect('instance/database.db')
cursor = conn.cursor()

# Open and read the CSV file
with open('healthcare-dataset-stroke-data2.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Create a list of modified rows
    rows_to_insert = []
    for row in reader:
        # Step 2: Modify Values Before Inserting
        # Example modification: Convert 'Male'/'Female' in 'gender' column to 1/0
        row['avg_glucose_level'] = encryptValue(row['avg_glucose_level'])
        row['bmi'] = encryptValue(row['bmi']) if row['bmi'] != "N/A" else None

        # Add modified row to list
        rows_to_insert.append((
            row['id'], row['gender'], row['age'], row['hypertension'], row['heart_disease'],
            row['ever_married'], row['work_type'], row['Residence_type'],
            row['avg_glucose_level'], row['bmi'], row['smoking_status'], row['stroke']
        ))

# Step 3: Bulk Insert Data into the Database
cursor.executemany('''
    INSERT INTO patient_model 
    (id, gender, age, hypertension, heart_disease, ever_married, work_type, 
    residence_type, avg_glucose_level, bmi, smoking_status, stroke) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', rows_to_insert)

# Commit and close the connection
conn.commit()
conn.close()
