if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[2]))

import unittest
from unittest.mock import Mock
from classes.manager.subject import SubjectManager, Subject
from classes.entity.subject_attribute import SubjectAttribute
from classes.repository.dbconnection import DbConnection

class SubjectManagerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.domain:Mock = Mock(id=1)
        self.subject_with_none_domain = Subject()
        self.subject:Subject = Subject()
        self.company_id:SubjectAttribute = SubjectAttribute(name='company_id', value='010101')
        self.product_id:SubjectAttribute = SubjectAttribute(name='product_id', value='0100102000')
        DbConnection().create_test_database()
        self.manager = SubjectManager()
        return super().setUp()


    def test_save_subject(self):
        subject:Subject = self.manager.save(self.subject, domain=self.domain)
        self.assertEqual(self.subject.id, subject.id)

    def test_should_not_delete(self):
        self.assertFalse(self.manager.delete(subject=Subject()))

    def test_should_not_save_attribute_without_subject(self):
        self.assertIsNone(self.manager.save_attribute(self.company_id, subject=self.subject))

    def test_save_attribute(self):
        self.subject.id = 1
        subject_attribute:SubjectAttribute = self.manager.save_attribute(subject_attribute=self.company_id, subject=self.subject)
        self.assertEqual(subject_attribute.name, self.company_id.name)
        self.assertEqual(subject_attribute.value, self.company_id.value)

    def test_delete_attribute(self):
        self.subject.id = 1
        subject_attribute:SubjectAttribute = self.manager.save_attribute(subject_attribute=self.company_id, subject=self.subject)
        self.assertTrue(self.manager.delete_attribute(subject_attribute))

    def test_fetch_attribute(self):
        self.subject.id = 1
        subject_attribute:SubjectAttribute = self.manager.save_attribute(subject_attribute=self.company_id, subject=self.subject)
        fetched:SubjectAttribute = self.manager.fetch_attribute(subject_attribute.id)
        self.assertEqual(subject_attribute.name, fetched.name)
        self.assertEqual(subject_attribute.value, fetched.value)

    def test_fetch_attributes_by_subject(self):
        self.subject.id = 1
        company_id:SubjectAttribute = self.manager.save_attribute(subject_attribute=self.company_id, subject=self.subject)   
        product_id:SubjectAttribute = self.manager.save_attribute(subject_attribute=self.product_id, subject=self.subject)     
        list_attribute:list = self.manager.fetch_attributes_by_subject(self.subject)
        self.assertEqual(len(list_attribute), 2)

    def test_fetch_subjects_by_attributes(self):
        self.subject = self.manager.save(subject=self.subject, domain=self.domain)
        self.manager.save_attribute(subject_attribute=self.company_id, subject=self.subject)   
        self.manager.save_attribute(subject_attribute=self.product_id, subject=self.subject)     
        list_attribute:list = self.manager.fetch_attributes_by_subject(self.subject)
        subject:Subject = self.manager.fetch_subject_by_attribute(subject_attributes=list_attribute)
        self.assertEqual(subject.id, self.subject.id)    

    def test_should_now_found_ambiguous_subject(self):
        subject:Subject = self.manager.save(subject=Subject(), domain=self.domain)
        self.manager.save_attribute(subject_attribute=self.company_id, subject=self.subject)   
        self.manager.save_attribute(subject_attribute=self.product_id, subject=self.subject)     
        subject:Subject = self.manager.save(subject=Subject(), domain=self.domain)
        self.manager.save_attribute(subject_attribute=self.company_id, subject=self.subject)   
        self.manager.save_attribute(subject_attribute=self.product_id, subject=self.subject)        
        subject:Subject = self.manager.fetch_subject_by_attribute(subject_attributes=[self.company_id, self.product_id])   
        self.assertIsNone(subject)         




if __name__ == '__main__':
    unittest.main()