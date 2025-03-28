from internal.db_sharc import get_connection
from models.record import Record
from psycopg2.extras import execute_values

class db_operations_pg_quotes:

    @staticmethod
    def insert_many(quotes: list[Record]) -> None:
        query = """
           INSERT INTO quotes (
               timestamp, expiration_date, ticker, strike_price,
               underlying_price, bid, ask, fingerprint
           ) VALUES %s
           """

        values = [q.to_tuple() for q in quotes]

        with get_connection() as conn:
            with conn.cursor() as cur:
                execute_values(cur, query, values, page_size=1000)
            conn.commit()

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