from classes.repository.conectable_mixin import ConnectableMixin
from classes.entity.domain import Domain
from datetime import datetime

class DomainRepository(ConnectableMixin):

    def __init__(self):
        super().__init__()

    def save(self, domain:Domain) -> Domain:
        SQL = """
        INSERT INTO domains (description, deleted_at) VALUES (?, ?)
        """
        domain.id = self.execute_last_row_id(SQL, (domain.description,None))
        if domain.id:
            return domain
        else:
            return None 


    def update(self, domain:Domain) -> Domain:
        SQL = """
        UPDATE
            domains 
        SET
            description = ? 
        WHERE  
            id = ? AND deleted_at is null
        """
        affectedRows = self.execute(SQL, (domain.description, domain.id))
        if affectedRows > 0:
            return domain
        else:
            return None         

    def delete(self, domain:Domain) -> bool:
        SQL = """
        UPDATE
            domains
        SET 
            deleted_at = ?
        WHERE 
            id = ? 
        """
        return self.execute(SQL, (datetime.now(), domain.id)) == 1


    def fetch(self, id:int) -> Domain:
        SQL = """ 
        SELECT 
            id, 
            description
        FROM 
            domains
        WHERE 
            id = ? and deleted_at is null
        """

        fetched = self.fetch_one(SQL, (id,))
        if fetched:
            return Domain(id=fetched[0], description=fetched[1])
        else:
            return None