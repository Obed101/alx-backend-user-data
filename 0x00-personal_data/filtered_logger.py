#!/usr/bin/env python3
""" This module filters user data """

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 seperator: str):
    """filters datum with regex"""
    for field in fields:
        pattern = field + "=.*?" + seperator
        repl = field + "=" + redaction + seperator
    return re.sub(pattern=pattern, repl=repl, string=message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Instance initializer"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Describes the format"""
        NotImplementedError
