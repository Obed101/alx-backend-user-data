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
        message = re.sub(pattern=pattern, repl=repl, string=message)
    return message


fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
            "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
