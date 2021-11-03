from enum import Enum 

class TemporalType(Enum):
    DATETIME = 0
    DATE = 1
    HOUR = 2 
    DAY = 3
    MONTH = 4
    YEAR = 5

class Temporal:
    def __init__(self, id:int=0, mapname:str = '', temporal_type:TemporalType = TemporalType.DATETIME):
        self.id = id 
        self.mapname = mapname 
        self.temporal_type = temporal_type
    


