
import unittest
import psycopg2
from datetime import datetime

import internal.load
from models.quote_record import Quote
from models.record import Record
from models.record import OptionType

class TestQuoteRecord(unittest.TestCase):
    """
    This is a test class with a set of integration tests from a top down approach.
    
    Unit tests for each individual function are not included in this class.  They should be
    included in separate test classes.

    """            
    def setUp(self):
        """connect to the database, get a connection, and delete all rows that have the fingerprint 'test'
        """
        
        config = internal.load.load_config()
        
        try:
            # connecting to the PGSQL Server
            with psycopg2.connect(
                host = config['host'],
                database = config['database'],
                user = config['user'],
                password = config['password'],
                ) as conne:
                print("Connected to the database")
                self.conn = conne
        except (psycopg2.DatabaseError, Exception) as error:
            print(f"Error connecting to the database: {error}")
            self.conn = None
            
        if self.conn is None:
            self.fail("Could not connect to the database")
            
        # delete lines with the fingerprint 'test'
        with self.conn.cursor() as cursor:
            cursor.execute("DELETE FROM quotes WHERE fingerprint = 'test'")
            self.conn.commit()
            
    def tearDown(self):
        """disconnect from the database
        """
        self.conn.close()
        print("Disconnected from the database")
        
    def test_insert_quote(self):
        """
        Test the insertion of a trade record into the database
        """
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM quotes WHERE fingerprint = 'test'")
            count = cursor.fetchone()[0]
            self.assertEqual(count, 0)
            
        now = datetime.now()
        
        record = Record(now, now, 'AA', OptionType.call, 100, 100)
        
        trade = Quote(record, 100, 100, fingerprint='test')
        trade.fingerprint = 'test'
        trade.insert(self.conn)
        
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM quotes WHERE fingerprint = 'test'")
            count = cursor.fetchone()[0]
            self.assertEqual(count, 1)