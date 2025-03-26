import os

import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="bodb",
        user="nabbasey",
        host=os.environ.get("PGHOST", "localhost"),
        port=os.environ.get("PGPORT", 5432)
    )

#port=5432