#!/usr/bin/env python3
""" This module filters user data """

import logging
from multiprocessing import connection
from os import environ
import re
from typing import List

PII_FIELDS = ('database', 'email', 'phone', 'password', 'ssn')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """filters datum with regex"""
    for field in fields:
        pattern = field + "=.*?" + separator
        repl = field + "=" + redaction + separator
    return re.sub(pattern=pattern, repl=repl, string=message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(database)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Instance initializer"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """uses filter_datum to format data"""
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """returns a Logger object from user data"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(stream_handler)

    return logger


def get_db() -> connection.MySQLConnection:
    """Connects securely to a database to read User Data"""
    database = environ.get("PERSONAL_DATA_DB_NAME")
    host = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    username = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = environ.get("PERSONAL_DATA_DB_PASSWORD", "")

    return connection.MySQLConnection(user=username, password=password,
                                           host=host, database=database)
