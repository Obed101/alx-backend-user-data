#!/usr/bin/env python3
"""main module for testing the functions and the whole app"""

import requests

url = 'http://0.0.0.0:5000'


def register_user(email: str, password: str) -> None:
    """test register method"""
    credencials = {"email": email, "password": password}
    response = requests.post(f'{url}/users', data=credencials)
    assert response.status_code == 200, "Test fail"


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
