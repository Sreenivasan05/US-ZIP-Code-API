import sqlite3
import os
from contextlib import contextmanager


class DatabaseManagement:
    def __init__(self, db_filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(base_dir, db_filename)
        self.connection = None
    
    def connect_to_db(self):
        try:
            self.connection = sqlite3.connect(self.db_path, check_same_thread = False)
            self.connection.row_factory = sqlite3.Row

            print("connected to SQLite db")
        except Exception as e:
            print(f"Error connecting to SQLite: {e}")

    @contextmanager
    def get_connection(self):

        if self.connection is None:
            self.connect_to_db()
        cursor = self.connection.cursor()
        try:
            yield cursor
        except Exception as e:
            self.connection.rollback()
            raise e
        finally:
            cursor.close()

    def close_pool(self):
        if self.connection:
            self.connection.close()
            print("closed SQLite connection")

db_conn = DatabaseManagement("US_zipcodes.db")