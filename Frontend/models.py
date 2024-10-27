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

    def as_json(self):
        return {
            "gender" : self.gender,
            "age" : self.age,
            "hypertension" : self.hypertension,
            "heart_disease" : self.heart_disease,
            "ever_married" : self.ever_married,
            "work_type" : self.work_type,
            "residence_type" : self.residence_type,
            "avg_glucose_level" : self.avg_glucose_level,
            "bmi" : self.bmi,
            "smoking_status" : self.smoking_status,
            "stroke" : self.stroke,
        }


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

    @classmethod
    def read_from_json(cls, data):
        return cls(
            id=data.get("id"),
            gender=data.get("gender"),
            age=data.get("age"),
            hypertension=data.get("hypertension"),
            heart_disease=data.get("heart_disease"),
            ever_married=data.get("ever_married"),
            work_type=data.get("work_type"),
            residence_type=data.get("residence_type"),
            avg_glucose_level=data.get("avg_glucose_level"),
            bmi=data.get("bmi"),
            smoking_status=data.get("smoking_status"),
            stroke=data.get("stroke"),
        )
        

