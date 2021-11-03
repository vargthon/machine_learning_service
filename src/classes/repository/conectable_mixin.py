from sqlite3.dbapi2 import Cursor
from sqlite3 import Error
from classes.repository.dbconnection import DbConnection
import sqlite3
import os 

class ConnectableMixin():

    def __init__(self):
        self.dbconn = DbConnection()

    def execute(self, SQL, values):
        affectedRows = 0
        try:
            self.dbconn.create_connection()
            cursor = self.dbconn.conn.cursor()
            cursor.execute(SQL, values)
            affectedRows = cursor.rowcount 
            self.dbconn.conn.commit()
            cursor.close()
        except (Error) as error:
            print(error)
        finally:
            if self.dbconn.conn:
                self.dbconn.conn.close()
        
        return affectedRows


    def create_test_database(self) -> None:
        self.dbconn.create_connection()
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        cursor = self.dbconn.conn.cursor()
        file = open(os.path.join(fileDir, 'assets/db/schema.sql'))
        SQL = file.read()
        cursor.executescript(SQL)
        file.close()
        self.dbconn.conn.commit()
        cursor.close()
        self.dbconn.conn.close()


    def fetch_one(self, SQL, values):
        row = None
        try:
            self.dbconn.create_connection()
            cursor = self.dbconn.conn.cursor()
            cursor.execute(SQL, values)
            row = cursor.fetchone() 
            cursor.close()
        except (Error) as error:
            print(error)
        finally:
            if self.dbconn.conn:
                self.dbconn.conn.close()
        
        return row        

    def fetch_all(self, SQL, values):
        rows = None
        try:
            self.dbconn.create_connection()
            cursor = self.dbconn.conn.cursor()
            cursor.execute(SQL, values)
            rows = cursor.fetchall() 
            cursor.close()
        except (Error) as error:
            print(error)
        finally:
            if self.dbconn.conn:
                self.dbconn.conn.close()
        
        return rows  

    def execute_last_row_id(self, SQL, values):
        last_id = None
        try:
            self.dbconn.create_connection()
            cursor = self.dbconn.conn.cursor()
            cursor.execute(SQL, values)
            self.dbconn.conn.commit()
            last_id = cursor.lastrowid
            cursor.close()
        except (Exception, Error) as error:
            print(error)
        finally:
            if self.dbconn.conn:
                self.dbconn.conn.close()
        
        return last_id        