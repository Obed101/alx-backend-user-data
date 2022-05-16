#!/usr/bin/env python3
"""Contains Basic authentication class"""

from typing import List, TypeVar
from flask import request


class Auth:
    """Basic Authentication class"""

    def __init__(self) -> None:
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
        """Returns None"""
        return None

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
