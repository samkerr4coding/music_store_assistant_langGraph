import sqlite3


def execute_query(query: str) -> list:
    """
    Executes a SQL query against the SQLite database and returns the results as a list of dictionaries.

    :param query: The SQL query string to execute.
    :return: A list of dictionaries where each dictionary represents a row in the result set.
    """
    conn = sqlite3.connect('Chinook_Sqlite.sqlite')  # Replace with your database file name if different
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        result = []
    finally:
        cursor.close()
        conn.close()

    return result
