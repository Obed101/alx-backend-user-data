#!/usr/bin/env python3
"""
Module for Basic authentication
"""

import uuid
import base64
from typing import Tuple, TypeVar
from auth import Auth
from models.user import User


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
            _header = base64_authorization_header
            return base64.b64decode(_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """Returns The username and email from decoded str"""
        if not decoded_base64_authorization_header or type(
                decoded_base64_authorization_header) is not str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        splitted = decoded_base64_authorization_header.split(':')
        return (splitted[0], splitted[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Returns user instance if the email and psswd are fine"""
        if not user_email or not user_pwd or type(
                user_email) is not str or type(user_pwd) is not str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            return user if User.is_valid_password(user_pwd) else None

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the whole user instance"""
        header = self.authorization_header(request)
        base64 = self.extract_base64_authorization_header(header)
        decoded = self.decode_base64_authorization_header(base64)
        credentials = self.extract_user_credentials(decoded)
        user = self.user_object_from_credentials(*credentials)
        return user