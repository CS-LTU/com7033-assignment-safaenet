from flask_restful import reqparse

patient_post_parser = reqparse.RequestParser()
patient_post_parser.add_argument('gender', type=int, help="Gender of the patient", required=True)
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

patient_put_parser = reqparse.RequestParser()
patient_put_parser.add_argument('gender', type=int, help="Gender of the patient", required=True)
patient_put_parser.add_argument('age', type=int, help="Age of the patient", required=True)
patient_put_parser.add_argument('hypertension', type=bool, help="Hypertension status", required=True)
patient_put_parser.add_argument('heart_disease', type=bool, help="Heart disease status", required=True)
patient_put_parser.add_argument('ever_married', type=bool, help="Ever married status", required=True)
patient_put_parser.add_argument('work_type', type=int, help="Work type", required=True)
patient_put_parser.add_argument('Residence_type', type=bool, help="Residence type", required=True)
patient_put_parser.add_argument('avg_glucose_level', type=float, help="Average glucose level", required=True)
patient_put_parser.add_argument('bmi', type=float, help="BMI", required=False)
patient_put_parser.add_argument('smoking_status', type=int, help="Smoking status", required=True)
patient_put_parser.add_argument('stroke', type=bool, help="Stroke status", required=True)