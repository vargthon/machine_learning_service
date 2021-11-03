if __name__ == '__main__':
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[2]))

from datetime import datetime 
import unittest
from unittest.mock import Mock
from classes.repository.dbconnection import DbConnection
from classes.repository.temporal import TemporalRepository, Temporal, TemporalType

class TemporalRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        DbConnection().create_test_database()
        self.repository:TemporalRepository = TemporalRepository()
        self.temporal:Temporal = Temporal(mapname='data', temporal_type=TemporalType.DATETIME)
        return super().setUp()

    def test_save_temporal(self):
        temporal:Temporal = self.repository.save(temporal=self.temporal)
        self.assertGreater(self.temporal.id, 0)
        self.assertEqual(self.temporal.mapname, temporal.mapname)
        self.assertEqual(self.temporal.temporal_type, temporal.temporal_type)

    def test_update_temporal(self):
        temporal:Temporal = self.repository.save(temporal=self.temporal)
        temporal.mapname = 'data2'
        temporal.temporal_type = TemporalType.HOUR
        updated:Temporal = self.repository.update(temporal)
        self.assertEqual(self.temporal.id, updated.id)
        self.assertEqual(self.temporal.mapname, updated.mapname)
        self.assertEqual(self.temporal.temporal_type, updated.temporal_type) 

    def test_delete_temporal(self):
        temporal:Temporal = self.repository.save(temporal=self.temporal)
        self.assertTrue(self.repository.delete(temporal=temporal)) 

    def test_fetch_temporal(self):
        temporal:Temporal = self.repository.save(temporal=self.temporal) 
        fetched:Temporal = self.repository.fetch(temporal.id)
        self.assertEqual(self.temporal.id, fetched.id)
        self.assertEqual(self.temporal.mapname, fetched.mapname)
        self.assertEqual(self.temporal.temporal_type, fetched.temporal_type) 


if __name__ == '__main__':
    unittest.main()
