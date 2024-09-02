import psycopg2
from psycopg2 import sql

def execute_query(query: str) -> list:
    """
    Executes a SQL query against the PostgreSQL database and returns the results if applicable.

    :param query: The SQL query string to execute.
    :return: A list of dictionaries for SELECT queries, or an empty list for non-returning queries.
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

        # Check if the query is a SELECT query
        if query.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]
        else:
            # For INSERT, UPDATE, DELETE, or other non-SELECT queries, commit the transaction
            conn.commit()

    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        if conn:
            conn.rollback()  # Rollback in case of error during a transaction

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return result
