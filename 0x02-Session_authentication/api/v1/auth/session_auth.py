#!/usr/bin/env python3
""" Session Authentication module
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """Session Authenticator"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session for a user
        """
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User's ID based on session_id
        """
        if session_id is None or type(session_id) is not str:
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Returns a User object based on cookie
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """
        User log out method
        """
        if request is None:
            return False

        cookie = self.session_cookie(request)

        if cookie is None or self.user_id_for_session_id(cookie) is None:
            return False

        del self.user_id_by_session_id[cookie]

        return True
