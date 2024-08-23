from langchain_core.tools import tool
from utils.db_util import execute_query

@tool
def get_artist_by_id(artist_id: int) -> list:
    """
    Retrieve an artist from the database based on their ID.

    Args:
        artist_id (int): The ID of the artist to retrieve.

    Returns:
        list: A list of artist records matching the given ID.
    """
    query = f"SELECT * FROM artist WHERE artist_id = {artist_id}"
    result = execute_query(query)
    return result

@tool
def get_artist_by_name(artist_name: str) -> list:
    """
    Retrieve an artist from the database whose name matches the given string.

    Args:
        artist_name (str): The name of the artist to search for.

    Returns:
        list: A list of artist records whose names match the given string.
    """
    query = f"""
        SELECT * FROM artist
        WHERE name LIKE '%{artist_name}%'
    """
    result = execute_query(query)
    return result

@tool
def insert_artist(name: str) -> None:
    """
    Insert a new artist into the database.

    Args:
        name (str): The name of the artist.
    """
    query = f"""
        INSERT INTO artist (name)
        VALUES ('{name}')
    """
    execute_query(query)

@tool
def update_artist(artist_id: int, name: str) -> None:
    """
    Update an existing artist in the database based on their ID.

    Args:
        artist_id (int): The ID of the artist to update.
        name (str): The new name of the artist.
    """
    query = f"""
        UPDATE artist
        SET name = '{name}'
        WHERE artist_id = {artist_id}
    """
    execute_query(query)

@tool
def delete_artist(artist_id: int) -> None:
    """
    Delete an artist from the database based on their ID.

    Args:
        artist_id (int): The ID of the artist to delete.
    """
    query = f"DELETE FROM artist WHERE artist_id = {artist_id}"
    execute_query(query)
