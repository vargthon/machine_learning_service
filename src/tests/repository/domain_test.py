if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[2]))

import unittest
from unittest.mock import Mock
from classes.repository.domain import DomainRepository, Domain 
from classes.repository.dbconnection import DbConnection


class DomainRepositoryTest(unittest.TestCase):

    def setUp(self) -> None:
        self.repository:DomainRepository = DomainRepository()
        DbConnection().create_test_database()
        self.domain:Domain = Domain(description='Product Sales Atacado')
        return super().setUp()

    def test_save_domain(self):
        domain:Domain = self.repository.save(domain=self.domain)
        self.assertGreater(domain.id, 0)
        self.assertEqual(domain.description, self.domain.description)

    def test_update_domain(self):
        domain:Domain = self.repository.save(domain=self.domain) 
        domain.description = 'UPDATED'
        updated:Domain = self.repository.update(domain=domain)
        self.assertGreater(updated.id, 0)
        self.assertEqual(domain.id, updated.id)
        self.assertEqual(updated.description, domain.description)

    def test_fetch_domain(self):
        domain:Domain = self.repository.save(domain=self.domain)
        fetched:Domain = self.repository.fetch(domain.id)
        self.assertEqual(domain.id, fetched.id)
        self.assertEqual(domain.description, fetched.description)        

    def test_delete_domain(self):
        domain:Domain = self.repository.save(domain=self.domain)
        self.assertTrue(self.repository.delete(domain)) 

    def test_not_fetch_deleted_domains(self):
        domain:Domain = self.repository.save(domain=self.domain)
        self.repository.delete(domain)
        self.assertIsNone(self.repository.fetch(domain.id))



if __name__ == '__main__':
    unittest.main()