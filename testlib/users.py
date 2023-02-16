"""Main module."""
from .connhelpers import connection


def get_user_details(user_id):
    response = connection.get_users(user_id)
    for entry in response:
        entry['full_name'] = f"entry['first_name'] entry['last_name']"
    return response


def get_user_details_di(user_id, conn):
    response = conn.get_users(user_id)
    for entry in response:
        entry['full_name'] = f"entry['first_name'] entry['last_name']"
    return response
