from langchain_core.tools import tool
from utils.db_util import execute_query

@tool
def get_media_type_by_id(media_type_id: int) -> list:
    """
    Retrieve a media type from the database based on its ID.

    Args:
        media_type_id (int): The ID of the media type to retrieve.

    Returns:
        list: A list of media type records matching the given ID.
    """
    query = f"SELECT * FROM media_type WHERE media_type_id = {media_type_id}"
    result = execute_query(query)
    return result

@tool
def get_media_types_by_name(media_type_name: str) -> list:
    """
    Retrieve all media types from the database whose names match the given string.

    Args:
        media_type_name (str): The name of the media type to search for.

    Returns:
        list: A list of media types whose names match the given string.
    """
    query = f"""
        SELECT * FROM media_type
        WHERE name LIKE '%{media_type_name}%'
    """
    result = execute_query(query)
    return result

@tool
def insert_media_type(name: str) -> None:
    """
    Insert a new media type into the database.

    Args:
        name (str): The name of the new media type.
    """
    query = f"""
        INSERT INTO media_type (name)
        VALUES ('{name}')
    """
    execute_query(query)

@tool
def update_media_type(media_type_id: int, name: str) -> None:
    """
    Update an existing media type in the database based on its ID.

    Args:
        media_type_id (int): The ID of the media type to update.
        name (str): The new name of the media type.
    """
    query = f"""
        UPDATE media_type
        SET name = '{name}'
        WHERE media_type_id = {media_type_id}
    """
    execute_query(query)

@tool
def delete_media_type(media_type_id: int) -> None:
    """
    Delete a media type from the database based on its ID.

    Args:
        media_type_id (int): The ID of the media type to delete.
    """
    query = f"DELETE FROM media_type WHERE media_type_id = {media_type_id}"
    execute_query(query)
