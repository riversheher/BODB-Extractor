from internal.db_sharc import get_connection
from models.record import Record

class db_operations_pg_quotes:

    @staticmethod
    def insert(quote: Record) -> int:
        query = """
        INSERT INTO quotes (timestamp, expiration_date, ticker, strike_price,
                            underlying_price, bid, ask, fingerprint)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, quote.to_tuple())
                conn.commit()
                return cur.fetchone()[0]