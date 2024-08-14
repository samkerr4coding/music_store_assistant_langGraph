from langchain_core.tools import tool

from utils.db_util import execute_query


@tool
def get_invoice_by_id(invoice_id: int) -> list:
    """
    Retrieve an invoice from the database based on its ID.

    Args:
        invoice_id (int): The ID of the invoice to retrieve.

    Returns:
        list: A list of invoice records matching the given ID.
    """
    query = f"SELECT * FROM Invoice WHERE InvoiceId = {invoice_id}"
    result = execute_query(query)
    return result


@tool
def get_invoices_by_customer_name(customer_name: str) -> list:
    """
    Retrieve all invoices from the database for customers whose names match the given string.

    Args:
        customer_name (str): The name of the customer to search for.

    Returns:
        list: A list of invoices for customers whose names match the given string.
    """
    query = f"""
        SELECT Invoice.*
        FROM Invoice
        JOIN Customer ON Invoice.CustomerId = Customer.CustomerId
        WHERE Customer.FirstName LIKE '%{customer_name}%' OR Customer.LastName LIKE '%{customer_name}%'
    """
    result = execute_query(query)
    return result


@tool
def insert_invoice(customer_id: int, invoice_date: str, billing_address: str, billing_city: str, billing_state: str,
                   billing_country: str, billing_postal_code: str, total: float) -> None:
    """
    Insert a new invoice into the database.

    Args:
        customer_id (int): The ID of the customer associated with the invoice.
        invoice_date (str): The date of the invoice.
        billing_address (str): The billing address for the invoice.
        billing_city (str): The billing city for the invoice.
        billing_state (str): The billing state for the invoice.
        billing_country (str): The billing country for the invoice.
        billing_postal_code (str): The billing postal code for the invoice.
        total (float): The total amount of the invoice.
    """
    query = f"""
        INSERT INTO Invoice (CustomerId, InvoiceDate, BillingAddress, BillingCity, BillingState, BillingCountry, BillingPostalCode, Total)
        VALUES ({customer_id}, '{invoice_date}', '{billing_address}', '{billing_city}', '{billing_state}', '{billing_country}', '{billing_postal_code}', {total})
    """
    execute_query(query)


@tool
def update_invoice(invoice_id: int, customer_id: int, invoice_date: str, billing_address: str, billing_city: str,
                   billing_state: str, billing_country: str, billing_postal_code: str, total: float) -> None:
    """
    Update an existing invoice in the database based on its ID.

    Args:
        invoice_id (int): The ID of the invoice to update.
        customer_id (int): The ID of the customer associated with the invoice.
        invoice_date (str): The new date of the invoice.
        billing_address (str): The new billing address for the invoice.
        billing_city (str): The new billing city for the invoice.
        billing_state (str): The new billing state for the invoice.
        billing_country (str): The new billing country for the invoice.
        billing_postal_code (str): The new billing postal code for the invoice.
        total (float): The new total amount of the invoice.
    """
    query = f"""
        UPDATE Invoice
        SET CustomerId = {customer_id}, InvoiceDate = '{invoice_date}', BillingAddress = '{billing_address}', BillingCity = '{billing_city}', BillingState = '{billing_state}', BillingCountry = '{billing_country}', BillingPostalCode = '{billing_postal_code}', Total = {total}
        WHERE InvoiceId = {invoice_id}
    """
    execute_query(query)


@tool
def delete_invoice(invoice_id: int) -> None:
    """
    Delete an invoice from the database based on its ID.

    Args:
        invoice_id (int): The ID of the invoice to delete.
    """
    query = f"DELETE FROM Invoice WHERE InvoiceId = {invoice_id}"
    execute_query(query)
