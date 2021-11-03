from classes.repository.subject import SubjectRepository, Subject 
from classes.entity.subject_attribute import SubjectAttribute
from classes.entity.domain import Domain
class SubjectManager:

    def __init__(self):
        self.subject_respository = SubjectRepository()


    def save(self, subject:Subject, domain:Domain) -> Subject:
        try:
            return self.subject_respository.save(subject=subject, domain=domain)            
        except Exception as error:
            print(error)
        return None 
        


    def update(self, subject:Subject, domain:Domain) -> Subject:   
        return self.subject_respository.update(subject=subject, domain=domain) 

    def delete(self, subject:Subject) -> bool:
        if subject.id == 0 or subject.id == None:
            return False
        return self.subject_respository.delete(subject)


    def save_attribute(self, subject_attribute:SubjectAttribute, subject:Subject) -> SubjectAttribute:
        if not subject_attribute.name:
            return False 
        if not subject_attribute.value:
            return None 
        if subject.id:
            return self.subject_respository.save_attribute(subject_attribute=subject_attribute, subject=subject)
        else:
            return None

    def delete_attribute(self, subject_attribute:SubjectAttribute):
        if subject_attribute.id:
            return self.subject_respository.delete_attribute(subject_attribute)
        else:
            return None

    def fetch_attribute(self, id:int) -> SubjectAttribute:
        if id:
            return self.subject_respository.fetch_attribute(id)
        else:
            return None

    def fetch_attributes_by_subject(self, subject:Subject) -> list:
        attributes:list = [] 
        if subject.id:
            attributes = self.subject_respository.fetch_attributes_by_subject(subject)

        return attributes

    def fetch_subject_by_attribute(self, subject_attributes:list) -> Subject:
        subjects_list:list = []
        
        for attribute in subject_attributes:
            subjects_list.append(self.subject_respository.fetch_subjects_by_attribute_values(attribute))       
        subjects_found:list = []
        for subjects in subjects_list:
            if subjects:
                for subject in subjects:
                    subjects_found.append(subject.id)
        result_subjects = set(subjects_found)

        if len(result_subjects) == 1:
            return Subject(id=list(result_subjects)[0])
        else:
            return None 


        
    