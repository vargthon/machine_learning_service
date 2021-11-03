from classes.repository.temporal import Temporal, TemporalRepository

class TemporalManager:

    def __init__(self):
        self.temporal_repository:TemporalRepository = TemporalRepository() 

    def save(self, temporal:Temporal) -> Temporal:
        if temporal.mapname == "":
            return None 
        return self.temporal_repository.save(temporal=temporal) 
    
    def update(self, temporal:Temporal) -> Temporal:
        if temporal.id == 0 or temporal.id == None:
            return None 
        return self.temporal_repository.update(temporal=temporal)
    
    def delete(self, temporal:Temporal) -> bool:
        if temporal.id == 0 or temporal.id == None:
            return False 
        return self.temporal_repository.delete(temporal=temporal)


    