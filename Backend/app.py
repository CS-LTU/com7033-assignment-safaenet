from flask import Flask
from flask_restful import Api
from controllers.patientsController import PatientResource
from controllers.usersController import auth_bp
from models.patientModel import db

app = Flask(__name__)
# app.app_context().push()
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

api.add_resource(PatientResource, "/GetById/<int:patient_id>", "/AddPatient", "/UpdatePatient/<int:patient_id>",
                 "/GetByValue/<string:search_value>", "/GetAll", "/DeletePatient/<int:patient_id>")
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == "__main__":
    app.run(debug=True)
