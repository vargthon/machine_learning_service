from datetime import datetime
from classes.entity.temporal import Temporal, TemporalType 
from classes.repository.conectable_mixin import ConnectableMixin

class TemporalRepository(ConnectableMixin):
    def __init__(self):
        super().__init__() 

    def save(self, temporal:Temporal) -> Temporal:
        SQL = """
        INSERT INTO temporals 
        (
            temporal_type, 
            mapname
        ) VALUES (
            ?,
            ?
        )
        """ 
        temporal.id = self.execute_last_row_id(SQL, (temporal.temporal_type.value, temporal.mapname))
        if temporal.id:
            return temporal 
        else:
            return None 

    def update(self, temporal:Temporal) -> Temporal:
        SQL = """
        UPDATE 
            temporals
        SET   
            temporal_type = ?,
            mapname = ?        
        WHERE
            id = ? and deleted_at is null
        """
        if self.execute(SQL, (temporal.temporal_type.value, temporal.mapname, temporal.id)) == 1:
            return temporal 
        else:
            return None

    def delete(self, temporal:Temporal) -> bool:
        SQL = """
        UPDATE
            temporals
        SET 
            deleted_at = ? 
        WHERE 
            id = ?
        """
        return self.execute(SQL, (datetime.now(), temporal.id)) == 1
        

    def fetch(self, id:int) -> Temporal:
        SQL = """
        SELECT 
            id,
            temporal_type,
            mapname
        FROM 
            temporals
        WHERE 
            deleted_at is null and id = ?
        """
        row = self.fetch_one(SQL, (id,)) 
        if row:
            return Temporal(id=row[0], temporal_type=TemporalType(row[1]), mapname=row[2])
        else:
            return None 