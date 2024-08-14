from langchain_core.tools import tool

from utils.db_util import execute_query


@tool
def get_genre_by_id(genre_id: int) -> list:
    """
    Retrieve a genre from the database based on its ID.

    Args:
        genre_id (int): The ID of the genre to retrieve.

    Returns:
        list: A list of genre records matching the given ID.
    """
    query = f"SELECT * FROM Genre WHERE GenreId = {genre_id}"
    result = execute_query(query)
    return result


@tool
def get_genres_by_name(genre_name: str) -> list:
    """
    Retrieve all genres from the database whose names match the given string.

    Args:
        genre_name (str): The name of the genre to search for.

    Returns:
        list: A list of genres whose names match the given string.
    """
    query = f"""
        SELECT * FROM Genre
        WHERE Name LIKE '%{genre_name}%'
    """
    result = execute_query(query)
    return result


@tool
def insert_genre(name: str) -> None:
    """
    Insert a new genre into the database.

    Args:
        name (str): The name of the new genre.
    """
    query = f"""
        INSERT INTO Genre (Name)
        VALUES ('{name}')
    """
    execute_query(query)


@tool
def update_genre(genre_id: int, name: str) -> None:
    """
    Update an existing genre in the database based on its ID.

    Args:
        genre_id (int): The ID of the genre to update.
        name (str): The new name of the genre.
    """
    query = f"""
        UPDATE Genre
        SET Name = '{name}'
        WHERE GenreId = {genre_id}
    """
    execute_query(query)


@tool
def delete_genre(genre_id: int) -> None:
    """
    Delete a genre from the database based on its ID.

    Args:
        genre_id (int): The ID of the genre to delete.
    """
    query = f"DELETE FROM Genre WHERE GenreId = {genre_id}"
    execute_query(query)
