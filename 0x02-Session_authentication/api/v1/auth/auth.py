#!/usr/bin/env python3
"""Contains Basic authentication class"""

from os import getenv
from typing import List, TypeVar
from flask import request
from requests import Request


class Auth:
    """Basic Authentication class"""

    def __init__(self) -> None:
        """Instance of Auth Class"""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns True if the Path is not in the Paths"""
        excluded_paths = self.add_slash(excluded_paths)
        if type(path) == str:
            path = path + "/" if not path.endswith("/") else path
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the value of Authorization in the header if any"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None"""
        return None

    # (not required) Function for validating url with slashes

    def add_slash(self, urls: List[str]) -> List[str]:
        """adds slash / to the url if it doesn't have"""
        if type(urls) is not List[str]:
            return urls
        for i, path in enumerate(urls):
            if not path.endswith("/"):
                urls[i] = path + "/"
        return urls

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""
        if not request:
            return None
        _my_session_id =  request.cookies.get(getenv('SESSION_NAME'))
        return _my_session_id
