from langchain_core.tools import tool

from utils.db_util import execute_query


@tool
def get_playlist_by_id(playlist_id: int) -> list:
    """
    Retrieve a playlist from the database based on its ID.

    Args:
        playlist_id (int): The ID of the playlist to retrieve.

    Returns:
        list: A list of playlist records matching the given ID.
    """
    query = f"SELECT * FROM Playlist WHERE PlaylistId = {playlist_id}"
    result = execute_query(query)
    return result


@tool
def get_playlists_by_name(playlist_name: str) -> list:
    """
    Retrieve all playlists from the database whose names match the given string.

    Args:
        playlist_name (str): The name of the playlist to search for.

    Returns:
        list: A list of playlists whose names match the given string.
    """
    query = f"""
        SELECT * FROM Playlist
        WHERE Name LIKE '%{playlist_name}%'
    """
    result = execute_query(query)
    return result


@tool
def insert_playlist(name: str) -> None:
    """
    Insert a new playlist into the database.

    Args:
        name (str): The name of the new playlist.
    """
    query = f"""
        INSERT INTO Playlist (Name)
        VALUES ('{name}')
    """
    execute_query(query)


@tool
def update_playlist(playlist_id: int, name: str) -> None:
    """
    Update an existing playlist in the database based on its ID.

    Args:
        playlist_id (int): The ID of the playlist to update.
        name (str): The new name of the playlist.
    """
    query = f"""
        UPDATE Playlist
        SET Name = '{name}'
        WHERE PlaylistId = {playlist_id}
    """
    execute_query(query)


@tool
def delete_playlist(playlist_id: int) -> None:
    """
    Delete a playlist from the database based on its ID.

    Args:
        playlist_id (int): The ID of the playlist to delete.
    """
    query = f"DELETE FROM Playlist WHERE PlaylistId = {playlist_id}"
    execute_query(query)
