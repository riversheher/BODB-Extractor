import psycopg2

from models.quote_record import Quote
from models.record import Record
from models.trade_record import Trade


def init_tables(conn) -> Exception:
    """
    Initializes the tables in the database
    
    An exception is returned if an error occurs, otherwise None is returned
    """
    try:
        cursor = conn.cursor()
        # Create the option type enum
        cursor.execute(Record.option_type_query)
        # Create the tables
        cursor.execute(Quote.create_table_query)
        cursor.execute(Trade.create_table_query)
        conn.commit()
        return None
    except psycopg2.DatabaseError as error:
        conn.rollback()
        return error
    
def reset_tables(conn) -> Exception:
    """
    Resets the tables in the database
    
    An exception is returned if an error occurs, otherwise None is returned
    """
    try:
        cursor = conn.cursor()
        # Drop the tables
        cursor.execute("DROP TABLE IF EXISTS trades")
        cursor.execute("DROP TABLE IF EXISTS quotes")
        # Drop the option type enum
        cursor.execute("DROP TYPE IF EXISTS optiontype")
        conn.commit()
        return None
    except psycopg2.DatabaseError as error:
        conn.rollback()
        return error