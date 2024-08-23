from langchain.tools import tool
from utils.db_util import execute_query

@tool
def get_track_by_id(track_id: int) -> list:
    """
    Retrieve a track from the database based on its ID.
    """
    query = f"SELECT * FROM track WHERE track_id = {track_id}"
    result = execute_query(query)
    return result

@tool
def get_tracks_by_album_title(album_title: str) -> list:
    """
    Retrieve all tracks from the database that belong to albums with titles matching the given string.
    """
    query = f"""
        SELECT track.*
        FROM track
        JOIN album ON track.album_id = album.album_id
        WHERE album.title LIKE '%{album_title}%'
    """
    result = execute_query(query)
    return result

@tool
def get_tracks_by_artist_name(artist_name: str) -> list:
    """
    Retrieve all tracks from the database by artists whose names match the given string.
    """
    query = f"""
        SELECT track.*
        FROM track
        JOIN album ON track.album_id = album.album_id
        JOIN artist ON album.artist_id = artist.artist_id
        WHERE artist.name LIKE '%{artist_name}%'
    """
    result = execute_query(query)
    return result

@tool
def insert_track(name: str, album_id: int, media_type_id: int, genre_id: int, composer: str, milliseconds: int,
                 bytes: int, unit_price: float) -> None:
    """
    Insert a new track into the database.
    """
    query = f"""
        INSERT INTO track (name, album_id, media_type_id, genre_id, composer, milliseconds, bytes, unit_price)
        VALUES ('{name}', {album_id}, {media_type_id}, {genre_id}, '{composer}', {milliseconds}, {bytes}, {unit_price})
    """
    execute_query(query)

@tool
def update_track(track_id: int, name: str, album_id: int, media_type_id: int, genre_id: int, composer: str,
                 milliseconds: int, bytes: int, unit_price: float) -> None:
    """
    Update an existing track in the database based on its ID.
    """
    query = f"""
        UPDATE track
        SET name = '{name}', album_id = {album_id}, media_type_id = {media_type_id}, genre_id = {genre_id}, composer = '{composer}', milliseconds = {milliseconds}, bytes = {bytes}, unit_price = {unit_price}
        WHERE track_id = {track_id}
    """
    execute_query(query)

@tool
def delete_track(track_id: int) -> None:
    """
    Delete a track from the database based on its ID.
    """
    query = f"DELETE FROM track WHERE track_id = {track_id}"
    execute_query(query)
