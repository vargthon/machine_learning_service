from datetime import datetime
from classes.repository.conectable_mixin import ConnectableMixin
from classes.entity.subject import Subject 
from classes.entity.subject_attribute import SubjectAttribute
from classes.entity.domain import Domain

class SubjectRepository(ConnectableMixin):

    def __init__(self):
        super().__init__()

    def save(self, subject:Subject, domain:Domain) -> Subject:
        SQL  = """
            INSERT INTO subjects (
                domain_id
            ) VALUES ( ? )
        """ 
        subject.id = self.execute_last_row_id(SQL, (domain.id,))
        if subject.id:
            return subject
        else:
            return None
        

    def update(self, subject:Subject, domain:Domain) -> Subject:
        SQL = """ 
            UPDATE
                subjects 
            SET 
                domain_id = ?
            WHERE 
                id = ?
                and deleted_at is null
        """ 
        affectedRows = self.execute(SQL, (domain.id, subject.id))
        if affectedRows == 1:
            return subject
        else:
            return None 

    def delete(self, subject:Subject) -> bool:
        SQL = """
        UPDATE 
            subjects
        SET 
            deleted_at = ? 
        WHERE 
            id = ?
            and deleted_at is null
        """ 
        return self.execute(SQL, (datetime.now(), subject.id)) == 1


    def save_attribute(self, subject_attribute:SubjectAttribute, subject:Subject) -> SubjectAttribute:
        SQL = """
        INSERT INTO subject_attributes (
            subject_id,
            name,
            value
        ) VALUES (
            ?,
            ?,
            ?
        )
        """ 
        subject_attribute.id = self.execute_last_row_id(SQL, (
            subject.id,
            subject_attribute.name,
            subject_attribute.value
        ))

        if subject_attribute.id:
            return subject_attribute
        else:
            return None 

    def update_attribute(self, subject_attribute:SubjectAttribute) -> SubjectAttribute:
        SQL = """
        UPDATE 
            subject_attributes
        SET 
            name=?,
            value=?
        WHERE 
            deleted_at is null
            and id = ?
        """
        affectedRows = self.execute(SQL, (
            subject_attribute.name,
            subject_attribute.value,
            subject_attribute.id
        ))
        if affectedRows == 1:
            return subject_attribute
        else:
            return None 

    def delete_attribute(self, subject_attribute:SubjectAttribute) -> bool:
        SQL = """
        UPDATE 
            subject_attributes
        SET 
            deleted_at = ?
        where 
            deleted_at is null and 
            id = ?
        """
        return self.execute(SQL, (datetime.now(), subject_attribute.id)) == 1

    def fetch_attribute(self, id:int) -> SubjectAttribute:
        SQL = """
        SELECT
            id, 
            subject_id,
            name,
            value
        FROM 
            subject_attributes
        WHERE   
            deleted_at is null 
            and id = ?
        """ 
        row = self.fetch_one(SQL, (id,))
        if row:
            return SubjectAttribute(id=row[0], name=row[2], value=row[3])
        else:
            return None 


    def fetch_attributes_by_subject(self, subject:Subject) -> list:
        attributes:list = [] 
        SQL = """
        SELECT
            id, subject_id, name, value
        FROM
            subject_attributes
        WHERE 
            deleted_at is null
            and subject_id = ?
        """
        rows = self.fetch_all(SQL, (subject.id,))
        if rows:
            for row in rows:
                attributes.append(SubjectAttribute(id=row[0], name=row[2], value=row[3]))
            return attributes 
        else:
            return None 


    def fetch_subjects_by_attribute_values(self, subject_attribute:SubjectAttribute) -> list:
        subjects:list = []
        SQL = """ 
        SELECT
            s.id
        FROM 
            subjects s, subject_attributes sa
        WHERE
            s.deleted_at is null and sa.deleted_at is null 
            and s.id = sa.subject_id
            and sa.name = ?  and sa.value = ?
        """
        rows = self.fetch_all(SQL, (subject_attribute.name, subject_attribute.value))
        if rows:
            for row in rows:
                subjects.append(Subject(id=row[0]))
            return subjects

