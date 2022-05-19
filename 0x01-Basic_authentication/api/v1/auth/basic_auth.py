#!/usr/bin/env python3
"""
Module for Basic authentication
"""

import base64
from auth import Auth


class BasicAuth(Auth):
    """Basic Authentication only class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        extracts base64 authorization header
        """
        if not authorization_header or type(authorization_header) is not str:
            return None
        if type(authorization_header) == str:
            splitted = authorization_header.split(" ")
            if splitted[0] != 'Basic':
                return None
            try:
                return splitted[1]
            except Exception:
                return None
        return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes base64_authorization_header"""
        if not base64_authorization_header or type(
                base64_authorization_header) is not str:
            return None
        try:
            return base64.b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None
