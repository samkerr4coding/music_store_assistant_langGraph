from langchain_core.tools import tool
from utils.db_util import execute_query

@tool
def get_invoice_line_by_id(invoice_line_id: int) -> list:
    """
    Retrieve an invoice line from the database based on its ID.

    Args:
        invoice_line_id (int): The ID of the invoice line to retrieve.

    Returns:
        list: A list of invoice line records matching the given ID.
    """
    query = f"SELECT * FROM invoice_line WHERE invoice_line_id = {invoice_line_id}"
    result = execute_query(query)
    return result

@tool
def get_invoice_lines_by_invoice_id(invoice_id: int) -> list:
    """
    Retrieve all invoice lines from the database for a given invoice ID.

    Args:
        invoice_id (int): The ID of the invoice to retrieve lines for.

    Returns:
        list: A list of invoice lines associated with the given invoice ID.
    """
    query = f"""
        SELECT * FROM invoice_line
        WHERE invoice_id = {invoice_id}
    """
    result = execute_query(query)
    return result

@tool
def insert_invoice_line(invoice_id: int, track_id: int, unit_price: float, quantity: int) -> None:
    """
    Insert a new invoice line into the database.

    Args:
        invoice_id (int): The ID of the invoice to associate the line with.
        track_id (int): The ID of the track included in the invoice line.
        unit_price (float): The unit price of the track.
        quantity (int): The quantity of the track purchased.
    """
    query = f"""
        INSERT INTO invoice_line (invoice_id, track_id, unit_price, quantity)
        VALUES ({invoice_id}, {track_id}, {unit_price}, {quantity})
    """
    execute_query(query)

@tool
def update_invoice_line(invoice_line_id: int, invoice_id: int, track_id: int, unit_price: float, quantity: int) -> None:
    """
    Update an existing invoice line in the database based on its ID.

    Args:
        invoice_line_id (int): The ID of the invoice line to update.
        invoice_id (int): The ID of the invoice to associate the updated line with.
        track_id (int): The ID of the track included in the updated invoice line.
        unit_price (float): The new unit price of the track.
        quantity (int): The new quantity of the track purchased.
    """
    query = f"""
        UPDATE invoice_line
        SET invoice_id = {invoice_id}, track_id = {track_id}, unit_price = {unit_price}, quantity = {quantity}
        WHERE invoice_line_id = {invoice_line_id}
    """
    execute_query(query)

@tool
def delete_invoice_line(invoice_line_id: int) -> None:
    """
    Delete an invoice line from the database based on its ID.

    Args:
        invoice_line_id (int): The ID of the invoice line to delete.
    """
    query = f"DELETE FROM invoice_line WHERE invoice_line_id = {invoice_line_id}"
    execute_query(query)