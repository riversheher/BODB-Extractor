from internal.db_sharc import get_connection
from models.record import Record

class db_operations_pg_trades():

    @staticmethod
    def insert(trade: Record) -> int:
        query = """
        INSERT INTO trades (timestamp, expiration_date, ticker, strike_price,
                            underlying_price, volume, price, fingerprint)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, trade.to_tuple())
                conn.commit()
                return cur.fetchone()[0]