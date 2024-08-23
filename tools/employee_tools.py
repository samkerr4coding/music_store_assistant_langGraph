from langchain_core.tools import tool
from utils.db_util import execute_query

@tool
def get_employee_by_id(employee_id: int) -> list:
    """
    Retrieve an employee from the database based on their ID.

    Args:
        employee_id (int): The ID of the employee to retrieve.

    Returns:
        list: A list of employee records matching the given ID.
    """
    query = f"SELECT * FROM employee WHERE employee_id = {employee_id}"
    result = execute_query(query)
    return result

@tool
def get_employees_by_name(employee_name: str) -> list:
    """
    Retrieve all employees from the database whose names match the given string.

    Args:
        employee_name (str): The name of the employee to search for.

    Returns:
        list: A list of employees whose names match the given string.
    """
    query = f"""
        SELECT * FROM employee
        WHERE first_name LIKE '%{employee_name}%' OR last_name LIKE '%{employee_name}%'
    """
    result = execute_query(query)
    return result

@tool
def insert_employee(last_name: str, first_name: str, title: str, reports_to: int, birth_date: str, hire_date: str,
                    address: str, city: str, state: str, country: str, postal_code: str, phone: str, fax: str,
                    email: str) -> None:
    """
    Insert a new employee into the database.

    Args:
        last_name (str): The last name of the employee.
        first_name (str): The first name of the employee.
        title (str): The job title of the employee.
        reports_to (int): The ID of the employee's manager.
        birth_date (str): The birth date of the employee.
        hire_date (str): The hire date of the employee.
        address (str): The address of the employee.
        city (str): The city of the employee.
        state (str): The state of the employee.
        country (str): The country of the employee.
        postal_code (str): The postal code of the employee.
        phone (str): The phone number of the employee.
        fax (str): The fax number of the employee.
        email (str): The email address of the employee.
    """
    query = f"""
        INSERT INTO employee (last_name, first_name, title, reports_to, birth_date, hire_date, address, city, state, country, postal_code, phone, fax, email)
        VALUES ('{last_name}', '{first_name}', '{title}', {reports_to}, '{birth_date}', '{hire_date}', '{address}', '{city}', '{state}', '{country}', '{postal_code}', '{phone}', '{fax}', '{email}')
    """
    execute_query(query)

@tool
def update_employee(employee_id: int, last_name: str, first_name: str, title: str, reports_to: int, birth_date: str,
                    hire_date: str, address: str, city: str, state: str, country: str, postal_code: str, phone: str,
                    fax: str, email: str) -> None:
    """
    Update an existing employee in the database based on their ID.

    Args:
        employee_id (int): The ID of the employee to update.
        last_name (str): The new last name of the employee.
        first_name (str): The new first name of the employee.
        title (str): The new job title of the employee.
        reports_to (int): The new ID of the employee's manager.
        birth_date (str): The new birth date of the employee.
        hire_date (str): The new hire date of the employee.
        address (str): The new address of the employee.
        city (str): The new city of the employee.
        state (str): The new state of the employee.
        country (str): The new country of the employee.
        postal_code (str): The new postal code of the employee.
        phone (str): The new phone number of the employee.
        fax (str): The new fax number of the employee.
        email (str): The new email address of the employee.
    """
    query = f"""
        UPDATE employee
        SET last_name = '{last_name}', first_name = '{first_name}', title = '{title}', reports_to = {reports_to}, birth_date = '{birth_date}', hire_date = '{hire_date}', address = '{address}', city = '{city}', state = '{state}', country = '{country}', postal_code = '{postal_code}', phone = '{phone}', fax = '{fax}', email = '{email}'
        WHERE employee_id = {employee_id}
    """
    execute_query(query)

@tool
def delete_employee(employee_id: int) -> None:
    """
    Delete an employee from the database based on their ID.

    Args:
        employee_id (int): The ID of the employee to delete.
    """
    query = f"DELETE FROM employee WHERE employee_id = {employee_id}"
    execute_query(query)
