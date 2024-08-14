from langchain.tools import tool

from utils.db_util import execute_query


@tool
def get_track_by_id(track_id: int) -> list:
    """
    Retrieve a track from the database based on its ID.
    """
    query = f"SELECT * FROM Track WHERE TrackId = {track_id}"
    result = execute_query(query)
    return result

@tool
def get_tracks_by_album_title(album_title: str) -> list:
    """
    Retrieve all tracks from the database that belong to albums with titles matching the given string.
    """
    query = f"""
        SELECT Track.*
        FROM Track
        JOIN Album ON Track.AlbumId = Album.AlbumId
        WHERE Album.Title LIKE '%{album_title}%'
    """
    result = execute_query(query)
    return result

@tool
def get_tracks_by_artist_name(artist_name: str) -> list:
    """
    Retrieve all tracks from the database by artists whose names match the given string.
    """
    query = f"""
        SELECT Track.*
        FROM Track
        JOIN Album ON Track.AlbumId = Album.AlbumId
        JOIN Artist ON Album.ArtistId = Artist.ArtistId
        WHERE Artist.Name LIKE '%{artist_name}%'
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
        INSERT INTO Track (Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice)
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
        UPDATE Track
        SET Name = '{name}', AlbumId = {album_id}, MediaTypeId = {media_type_id}, GenreId = {genre_id}, Composer = '{composer}', Milliseconds = {milliseconds}, Bytes = {bytes}, UnitPrice = {unit_price}
        WHERE TrackId = {track_id}
    """
    execute_query(query)

@tool
def delete_track(track_id: int) -> None:
    """
    Delete a track from the database based on its ID.
    """
    query = f"DELETE FROM Track WHERE TrackId = {track_id}"
    execute_query(query)
