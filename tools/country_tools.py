from langchain_core.tools import tool
from utils.db_util import execute_query

@tool
def get_country_by_id(country_id: int) -> list:
    """
    Retrieve a country from the database based on its ID.

    Args:
        country_id (int): The ID of the country to retrieve.

    Returns:
        list: A list of country records matching the given ID.
    """
    query = f"SELECT * FROM country WHERE country_id = {country_id}"
    result = execute_query(query)
    return result

@tool
def get_countries_by_name(country_name: str) -> list:
    """
    Retrieve all countries from the database whose names match the given string.

    Args:
        country_name (str): The name of the country to search for.

    Returns:
        list: A list of countries whose names match the given string.
    """
    query = f"""
        SELECT * FROM country
        WHERE name LIKE '%{country_name}%'
    """
    result = execute_query(query)
    return result

@tool
def insert_country(name: str) -> None:
    """
    Insert a new country into the database.

    Args:
        name (str): The name of the new country.
    """
    query = f"""
        INSERT INTO country (name)
        VALUES ('{name}')
    """
    execute_query(query)

@tool
def update_country(country_id: int, name: str) -> None:
    """
    Update an existing country in the database based on its ID.

    Args:
        country_id (int): The ID of the country to update.
        name (str): The new name of the country.
    """
    query = f"""
        UPDATE country
        SET name = '{name}'
        WHERE country_id = {country_id}
    """
    execute_query(query)

@tool
def delete_country(country_id: int) -> None:
    """
    Delete a country from the database based on its ID.

    Args:
        country_id (int): The ID of the country to delete.
    """
    query = f"DELETE FROM country WHERE country_id = {country_id}"
    execute_query(query)
