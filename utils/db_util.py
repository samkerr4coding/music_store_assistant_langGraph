import psycopg2
from psycopg2 import sql


def execute_query(query: str) -> list:
    """
    Executes a SQL query against the PostgreSQL database and returns the results as a list of dictionaries.

    :param query: The SQL query string to execute.
    :return: A list of dictionaries where each dictionary represents a row in the result set.
    """
    conn = None
    result = []
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="chinook_auto_increment",  # Replace with your database name
            user="postgres",  # Replace with your database user
            password="postgres",  # Replace with your password
            host="localhost",  # Your host
            port="5432"  # Your port
        )

        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        # Convert query result to a list of dictionaries
        result = [dict(zip(columns, row)) for row in rows]

    except psycopg2.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return result
