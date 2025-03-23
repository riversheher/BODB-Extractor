from internal.db_sharc import get_connection
from datetime import datetime

class db_operations_pg_tertiary:

    @staticmethod
    def insert(record_type: str, timestamp, ticker: str, raw_line: str, fingerprint: str) -> int:
        query = """
        INSERT INTO tertiary_records (record_type, timestamp, ticker, raw_line, fingerprint)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id;
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, toTuple(record_type, timestamp, ticker, raw_line, fingerprint))
                conn.commit()
                return cur.fetchone()[0]
            
            
def toTuple(record_type: str, timestamp: datetime, ticker: str, raw_line: str, fingerprint: str) -> tuple:
    return (record_type, timestamp.strftime('%Y-%m-%d %H:%M:%S'), ticker, raw_line, fingerprint)