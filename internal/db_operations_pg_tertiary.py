from internal.db_sharc import get_connection

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
                cur.execute(query, (record_type, timestamp, ticker, raw_line, fingerprint))
                conn.commit()
                return cur.fetchone()[0]