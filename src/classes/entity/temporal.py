from enum import Enum 

class TemporalType(Enum):
    DATETIME = 0
    HOUR = 1 
    DAY = 2
    MONTH = 3
    YEAR = 4

class Temporal:
    def __init__(self, id:int=0, mapname:str = '', temporal_type:TemporalType = TemporalType.DATETIME):
        self.id = id 
        self.mapname = mapname 
        self.temporal_type = temporal_type
    


