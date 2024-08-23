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
    query = f"SELECT * FROM playlist WHERE playlist_id = {playlist_id}"
    result = execute_query(query)
    return result

# @tool
# def get_playlists_by_name(playlist_name: str) -> list:
#     """
#     Retrieve all playlists from the database whose names match the given string.
#
#     Args:
#         playlist_name (str): The name of the playlist to search for.
#
#     Returns:
#         list: A list of playlists whose names match the given string.
#     """
#     query = f"""
#         SELECT * FROM playlist
#         WHERE name LIKE '%{playlist_name}%'
#     """
#     result = execute_query(query)
#     return result

@tool
def insert_playlist(name: str) -> None:
    """
    Insert a new playlist into the database.

    Args:
        name (str): The name of the new playlist.
    """
    query = f"""
        INSERT INTO playlist (name)
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
        UPDATE playlist
        SET name = '{name}'
        WHERE playlist_id = {playlist_id}
    """
    execute_query(query)

@tool
def delete_playlist(playlist_id: int) -> None:
    """
    Delete a playlist from the database based on its ID.

    Args:
        playlist_id (int): The ID of the playlist to delete.
    """
    query = f"DELETE FROM playlist WHERE playlist_id = {playlist_id}"
    execute_query(query)

from langchain_core.tools import tool
from utils.db_util import execute_query

@tool
def get_playlists_by_composer_name(artist_name: str) -> list:
    """
    Retrieve playlists containing tracks by a given artist.

    Args:
        artist_name (str): The name of the artist to search for.

    Returns:
        list: A list of playlists containing tracks by the given artist.
    """
    query = f"""
        SELECT DISTINCT playlist.*
        FROM playlist
        JOIN playlist_track ON playlist.playlist_id = playlist_track.playlist_id
        JOIN track ON playlist_track.track_id = track.track_id
        JOIN artist ON track.composer LIKE '%{artist_name}%'
    """
    result = execute_query(query)
    return result

@tool
def get_playlists_by_song_name(song_name: str) -> list:
    """
    Retrieve playlists containing a specific song.

    Args:
        song_name (str): The name of the song to search for.

    Returns:
        list: A list of playlists containing the specified song.
    """
    query = f"""
        SELECT DISTINCT playlist.*
        FROM playlist
        JOIN playlist_track ON playlist.playlist_id = playlist_track.playlist_id
        JOIN track ON playlist_track.track_id = track.track_id
        WHERE track.name LIKE '%{song_name}%'
    """
    result = execute_query(query)
    return result

@tool
def get_playlists_by_genre(genre_name: str) -> list:
    """
    Retrieve playlists containing tracks of a specific genre.

    Args:
        genre_name (str): The name of the genre to search for.

    Returns:
        list: A list of playlists containing tracks of the specified genre.
    """
    query = f"""
        SELECT DISTINCT playlist.*
        FROM playlist
        JOIN playlist_track ON playlist.playlist_id = playlist_track.playlist_id
        JOIN track ON playlist_track.track_id = track.track_id
        JOIN genre ON track.genre_id = genre.genre_id
        WHERE genre.name LIKE '%{genre_name}%'
    """
    result = execute_query(query)
    return result

@tool
def get_playlists_by_album_name(album_name: str) -> list:
    """
    Retrieve playlists containing tracks from a specific album.

    Args:
        album_name (str): The name of the album to search for.

    Returns:
        list: A list of playlists containing tracks from the specified album.
    """
    query = f"""
        SELECT DISTINCT playlist.*
        FROM playlist
        JOIN playlist_track ON playlist.playlist_id = playlist_track.playlist_id
        JOIN track ON playlist_track.track_id = track.track_id
        JOIN album ON track.album_id = album.album_id
        WHERE album.name LIKE '%{album_name}%'
    """
    result = execute_query(query)
    return result

@tool
def get_playlists_by_playlist_name(playlist_name: str) -> list:
    """
    Retrieve playlists matching a specific name.

    Args:
        playlist_name (str): The name of the playlist to search for.

    Returns:
        list: A list of playlists matching the specified name.
    """
    query = f"""
        SELECT *
        FROM playlist
        WHERE name LIKE '%{playlist_name}%'
    """
    result = execute_query(query)
    return result
