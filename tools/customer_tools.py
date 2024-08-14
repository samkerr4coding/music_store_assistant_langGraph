from langchain_core.tools import tool

from utils.db_util import execute_query


@tool
def get_customer_by_id(customer_id: int) -> list:
    """
    Retrieve a customer from the database based on their ID.

    Args:
        customer_id (int): The ID of the customer to retrieve.

    Returns:
        list: A list of customer records matching the given ID.
    """
    query = f"SELECT * FROM Customer WHERE CustomerId = {customer_id}"
    result = execute_query(query)
    return result


@tool
def get_customers_by_name(customer_name: str) -> list:
    """
    Retrieve all customers from the database whose names match the given string.

    Args:
        customer_name (str): The name of the customer to search for.

    Returns:
        list: A list of customers whose names match the given string.
    """
    query = f"""
        SELECT * FROM Customer
        WHERE FirstName LIKE '%{customer_name}%' OR LastName LIKE '%{customer_name}%'
    """
    result = execute_query(query)
    return result


@tool
def get_customers_by_email(email: str) -> list:
    """
    Retrieve all customers from the database whose email addresses match the given string.

    Args:
        email (str): The email address to search for.

    Returns:
        list: A list of customers whose email addresses match the given string.
    """
    query = f"""
        SELECT * FROM Customer
        WHERE Email LIKE '%{email}%'
    """
    result = execute_query(query)
    return result


@tool
def insert_customer(first_name: str, last_name: str, company: str, address: str, city: str, state: str, country: str,
                    postal_code: str, phone: str, fax: str, email: str, support_rep_id: int) -> None:
    """
    Insert a new customer into the database.

    Args:
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        company (str): The company of the customer.
        address (str): The address of the customer.
        city (str): The city of the customer.
        state (str): The state of the customer.
        country (str): The country of the customer.
        postal_code (str): The postal code of the customer.
        phone (str): The phone number of the customer.
        fax (str): The fax number of the customer.
        email (str): The email address of the customer.
        support_rep_id (int): The ID of the support representative assigned to the customer.
    """
    query = f"""
        INSERT INTO Customer (FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId)
        VALUES ('{first_name}', '{last_name}', '{company}', '{address}', '{city}', '{state}', '{country}', '{postal_code}', '{phone}', '{fax}', '{email}', {support_rep_id})
    """
    execute_query(query)


@tool
def update_customer(customer_id: int, first_name: str, last_name: str, company: str, address: str, city: str,
                    state: str, country: str, postal_code: str, phone: str, fax: str, email: str,
                    support_rep_id: int) -> None:
    """
    Update an existing customer in the database based on their ID.

    Args:
        customer_id (int): The ID of the customer to update.
        first_name (str): The new first name of the customer.
        last_name (str): The new last name of the customer.
        company (str): The new company of the customer.
        address (str): The new address of the customer.
        city (str): The new city of the customer.
        state (str): The new state of the customer.
        country (str): The new country of the customer.
        postal_code (str): The new postal code of the customer.
        phone (str): The new phone number of the customer.
        fax (str): The new fax number of the customer.
        email (str): The new email address of the customer.
        support_rep_id (int): The new ID of the support representative assigned to the customer.
    """
    query = f"""
        UPDATE Customer
        SET FirstName = '{first_name}', LastName = '{last_name}', Company = '{company}', Address = '{address}', City = '{city}', State = '{state}', Country = '{country}', PostalCode = '{postal_code}', Phone = '{phone}', Fax = '{fax}', Email = '{email}', SupportRepId = {support_rep_id}
        WHERE CustomerId = {customer_id}
    """
    execute_query(query)


@tool
def delete_customer(customer_id: int) -> None:
    """
    Delete a customer from the database based on their ID.

    Args:
        customer_id (int): The ID of the customer to delete.
    """
    query = f"DELETE FROM Customer WHERE CustomerId = {customer_id}"
    execute_query(query)
