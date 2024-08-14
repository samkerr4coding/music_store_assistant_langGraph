from langchain_core.tools import tool

from utils.db_util import execute_query


@tool
def get_album_by_id(album_id: int) -> list:
    """
    Retrieve an album from the database based on its ID.

    Args:
        album_id (int): The ID of the album to retrieve.

    Returns:
        list: A list of album records matching the given ID.
    """
    query = f"SELECT * FROM Album WHERE AlbumId = {album_id}"
    result = execute_query(query)
    return result


@tool
def get_albums_by_artist_name(artist_name: str) -> list:
    """
    Retrieve all albums from the database by artists whose names match the given string.

    Args:
        artist_name (str): The name of the artist to search for.

    Returns:
        list: A list of albums by artists whose names match the given string.
    """
    query = f"""
        SELECT Album.*
        FROM Album
        JOIN Artist ON Album.ArtistId = Artist.ArtistId
        WHERE Artist.Name LIKE '%{artist_name}%'
    """
    result = execute_query(query)
    return result


@tool
def get_albums_by_title(album_title: str) -> list:
    """
    Retrieve all albums from the database with titles matching the given string.

    Args:
        album_title (str): The title of the album to search for.

    Returns:
        list: A list of albums with titles that match the given string.
    """
    query = f"""
        SELECT * FROM Album
        WHERE Title LIKE '%{album_title}%'
    """
    result = execute_query(query)
    return result


@tool
def insert_album(title: str, artist_id: int) -> None:
    """
    Insert a new album into the database.

    Args:
        title (str): The title of the album.
        artist_id (int): The ID of the artist who created the album.
    """
    query = f"""
        INSERT INTO Album (Title, ArtistId)
        VALUES ('{title}', {artist_id})
    """
    execute_query(query)


@tool
def update_album(album_id: int, title: str, artist_id: int) -> None:
    """
    Update an existing album in the database based on its ID.

    Args:
        album_id (int): The ID of the album to update.
        title (str): The new title of the album.
        artist_id (int): The new artist ID for the album.
    """
    query = f"""
        UPDATE Album
        SET Title = '{title}', ArtistId = {artist_id}
        WHERE AlbumId = {album_id}
    """
    execute_query(query)


@tool
def delete_album(album_id: int) -> None:
    """
    Delete an album from the database based on its ID.

    Args:
        album_id (int): The ID of the album to delete.
    """
    query = f"DELETE FROM Album WHERE AlbumId = {album_id}"
    execute_query(query)
