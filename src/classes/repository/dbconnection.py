import sqlite3 as sqlite
from sqlite3 import Error
import pathlib
from configparser import ConfigParser
import os

class DbConnection():
    def __init__(self):
        self.conn = None 
        self.environment = os.getenv('ENVIRONMENT') if os.getenv('ENVIRONMENT') else 'TEST'


    def create_connection(self):
        try:
            fileDir = os.path.dirname(os.path.realpath('__file__'))
            if self.environment == 'TEST':
                self.conn = sqlite.connect(fileDir + '/assets/db/test_database.sqlite')
            else:
                self.conn = sqlite.connect(fileDir + '/assets/db/database.sqlite')
        except (Exception, Error) as error:
            print(error)

    def create_test_database(self) -> None:
        self.create_connection()
        try:
            fileDir = os.path.dirname(os.path.realpath('__file__'))
            self.conn = sqlite.connect(fileDir + '/assets/db/test_database.sqlite')
            cursor = self.conn.cursor()
            file = open(os.path.join(fileDir, 'assets/db/schema.sql'))
            SQL = file.read()
            cursor.executescript(SQL)
            file.close()
            self.conn.commit()
            cursor.close()
            self.conn.close()
        except (Exception, Error) as error:
            print(error)        
        
        
        


        

    