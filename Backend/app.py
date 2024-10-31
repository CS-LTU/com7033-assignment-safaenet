from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from controllers.patientsController import PatientResource
from controllers.usersController import AuthAPI, SessionCheckAPI
from models.patientModel import db

app = Flask(__name__)
# app.app_context().push()
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = '1qaz2wsx'
CORS(app)

db.init_app(app)
api.add_resource(AuthAPI, '/auth')

api.add_resource(PatientResource, "/GetById/<int:patient_id>", "/AddPatient", "/UpdatePatient/<int:patient_id>",
                 "/GetByValue/<string:search_value>", "/GetAll", "/DeletePatient/<int:patient_id>")
api.add_resource(SessionCheckAPI, '/SessionCheck')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
