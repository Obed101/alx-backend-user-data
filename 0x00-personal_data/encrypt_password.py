#!/usr/bin/env python3
"""Encrypts password"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Encrypts the password using hashpw
    """
    return bcrypt.hashpw(password.encode('utf-8'),
                         bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ checks if password is valid """
    return bcrypt.checkpw(password.encode('utf-8'),
                          hashed_password)
