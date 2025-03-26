import os

import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="bodb",
        user="nabbasey",
        host="localhost",
        port=5432
    )

#port=5432