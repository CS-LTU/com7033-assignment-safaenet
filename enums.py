from enum import Enum

class WorkType(Enum):
    CHILDREN = 0
    GOVERNMENT = 1
    PRIVATE = 2
    SELF_EMPLOYED = 3
    NEVER_WORKED = 4
    
    
class SmokingStatus(Enum):
    NEVER_SMOKED = 0
    SMOKES = 1
    FORMERLY_SMOKED = 2
    UNKNOWN = 3
    
    
class Gender(Enum):
    Female = 0
    Male = 1
    Other = 2
    
    
class ResidenceType(Enum):
    Rural = False
    Urban = True
    
