if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[2]))

import unittest
from unittest.mock import Mock
from classes.repository.subject import Subject, SubjectRepository
from classes.entity.subject_attribute import SubjectAttribute
from classes.repository.dbconnection import DbConnection

class SubjectRepositoryTest(unittest.TestCase):

    def setUp(self) -> None:
        DbConnection().create_test_database()
        self.repository:SubjectRepository = SubjectRepository()
        self.subject_attribute:SubjectAttribute = SubjectAttribute(name='product_id', value='0100102000')
        self.subject_attribute2:SubjectAttribute = SubjectAttribute(name='company_id', value='010101')
        
        self.domain:Mock = Mock(id=1, description='Alguma descricao')
        self.domain2:Mock = Mock(id=2, description='Outro Dominio')
        self.subject:Subject = Subject()
        return super().setUp()

    def test_save_subject(self):
        subject:Subject = self.repository.save(subject=self.subject, domain=self.domain)
        self.assertGreater(subject.id, 0)

    
    def test_update_subject(self):
        subject:Subject = self.repository.save(subject=self.subject, domain=self.domain)
        self.assertGreater(subject.id, 0)
        updated:Subject = self.repository.update(subject=subject, domain=self.domain)
        self.assertEqual(subject.id, updated.id)

    def test_delete_subject(self):
        subject:Subject = self.repository.save(subject=self.subject, domain=self.domain)
        self.assertTrue(self.repository.delete(subject))

    def test_save_attribute(self):
        subject:Mock = Mock(id=1)
        subject_attribute:SubjectAttribute = self.repository.save_attribute(self.subject_attribute, subject=subject)
        self.assertGreater(subject_attribute.id, 0)
        self.assertEqual(subject_attribute.name, self.subject_attribute.name)
        self.assertEqual(subject_attribute.value, self.subject_attribute.value)

    def test_update_attribute(self):
        subject:Mock = Mock(id=1)
        subject_attribute:SubjectAttribute = self.repository.save_attribute(self.subject_attribute, subject=subject)
        subject_attribute.name = 'other attribute name'
        subject_attribute.value = 'other value'
        updated:SubjectAttribute = self.repository.update_attribute(subject_attribute)
        self.assertEqual(subject_attribute.id, updated.id)
        self.assertEqual(subject_attribute.name, updated.name)
        self.assertEqual(subject_attribute.value, updated.value)

    def test_delete_subject_attribute(self):
        subject:Mock = Mock(id=1)
        subject_attribute:SubjectAttribute = self.repository.save_attribute(self.subject_attribute, subject=subject)    
        self.assertTrue(self.repository.delete_attribute(subject_attribute=subject_attribute))
    
    def test_fetch_attribute(self):
        subject:Mock = Mock(id=1)
        subject_attribute:SubjectAttribute = self.repository.save_attribute(self.subject_attribute, subject=subject)   
        fetched = self.repository.fetch_attribute(subject_attribute.id)
        self.assertEqual(subject_attribute.id, fetched.id)
        self.assertEqual(subject_attribute.name, fetched.name)
        self.assertEqual(subject_attribute.value, fetched.value)    

    def test_fetch_attribute_by_subject(self):
        subject:Mock = Mock(id=1)
        self.repository.save_attribute(self.subject_attribute, subject=subject)   
        self.repository.save_attribute(self.subject_attribute2, subject=subject)
        attributes_list:list = self.repository.fetch_attributes_by_subject(subject=subject)
        self.assertEqual(len(attributes_list),2)

    def test_fetch_subjects_by_attributes(self):
        subject:Subject = self.repository.save(subject=self.subject, domain=Mock(id=1))
        
        
        


if __name__ == '__main__':
    unittest.main()

