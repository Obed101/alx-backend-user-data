#!/usr/bin/env python3
""" This module filters user data """

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 seperator: str):
    """filters datum with regex"""
    for field in fields:
        pattern = field + "=.*?" + seperator
        repl = field + "=" + redaction + seperator
    return re.sub(pattern=pattern, repl=repl, string=message)
