from flask_restful import Resource, marshal_with
from services.PatientService import PatientService
from models.patientModel import resource_fields
from parsers import patient_post_parser, patient_put_parser


class PatientResource(Resource):
    @marshal_with(resource_fields)
    def get(self, patient_id=None, search_value=None):
        if patient_id:
            return PatientService.get_patient_by_id(patient_id)
        elif search_value:
            return PatientService.search_patients_by_value(search_value)
        else:
            return PatientService.get_all_patients()
 
    @marshal_with(resource_fields)
    def post(self):
        args = patient_post_parser.parse_args()
        return PatientService.add_patient(args), 201
        
    def put(self, patient_id):
        args = patient_put_parser.parse_args()
        return PatientService.update_patient(patient_id, args)

    def delete(self, patient_id):
        return PatientService.delete_patient(patient_id)
