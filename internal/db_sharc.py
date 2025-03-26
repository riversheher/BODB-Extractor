import os

import psycopg2

def get_connection():
    if "PGHOST" not in os.environ:
        job_id = os.environ.get("SLURM_JOB_ID")
        if job_id:
            os.environ["PGHOST"] = f"/home/nabbasey/scratch/pg_sock{job_id}"

    return psycopg2.connect(
        dbname="bodb",
        user="nabbasey",
        host=os.environ.get("PGHOST", "/tmp"),
        port=os.environ.get("PGPORT", 5432)
    )

#port=5432