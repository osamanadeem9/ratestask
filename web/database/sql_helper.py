import os

import psycopg2
from database.queries import RATES_QUERY


class Database:
    # connects to our Postgres DB, and returns connection object.
    def __init__(self):
        self.connection = None

    def get_connection(self):
        self.connection = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USERNAME"),
            password=os.getenv("POSTGRES_PASSWORD"))
        return self.connection

    # executes query from sql file, and fetches relevant records from DB
    def fetch_avg_rates(self, params):
        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                query = RATES_QUERY
                cursor.execute(query,
                               {'origin': params['origin'], 'destination': params['destination'],
                                'date_from': str(params['date_from']), 'date_to': str(params['date_to']), })
                records = cursor.fetchall()
                records_arr = [{'day': str(record[0]), 'average': record[1]} for record in records]

        return records_arr
