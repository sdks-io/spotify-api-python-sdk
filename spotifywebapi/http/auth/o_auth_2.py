# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.authentication.header_auth import HeaderAuth
from spotifywebapi.api_helper import APIHelper
from spotifywebapi.configuration import Server
from spotifywebapi.models.o_auth_token import OAuthToken
from apimatic_core.utilities.auth_helper import AuthHelper
from spotifywebapi.controllers.o_auth_authorization_controller import\
    OAuthAuthorizationController


class OAuth2(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in AuthorizationCodeAuth

        """
        return "AuthorizationCodeAuth: OAuthToken is undefined or expired."

    def __init__(self, authorization_code_auth_credentials, config):
        self._o_auth_client_id = authorization_code_auth_credentials.o_auth_client_id \
            if authorization_code_auth_credentials is not None else None
        self._o_auth_client_secret = authorization_code_auth_credentials.o_auth_client_secret \
            if authorization_code_auth_credentials is not None else None
        self._o_auth_redirect_uri = authorization_code_auth_credentials.o_auth_redirect_uri \
            if authorization_code_auth_credentials is not None else None
        if authorization_code_auth_credentials is not None \
                and isinstance(authorization_code_auth_credentials.o_auth_token, OAuthToken):
            self._o_auth_token = OAuthToken.from_dictionary(
                APIHelper.to_dictionary(authorization_code_auth_credentials.o_auth_token))
        else:
            self._o_auth_token = authorization_code_auth_credentials.o_auth_token \
                if authorization_code_auth_credentials is not None else None
        if authorization_code_auth_credentials is not None \
                and isinstance(authorization_code_auth_credentials.o_auth_scopes, list):
            self._o_auth_scopes = authorization_code_auth_credentials.o_auth_scopes
        else:
            self._o_auth_scopes = None
        self._config = config
        self._o_auth_api = OAuthAuthorizationController(config)
        auth_params = {}
        if isinstance(self._o_auth_token, OAuthToken) and hasattr(self._o_auth_token, 'access_token'):
            auth_params = {"Authorization": "Bearer {}".format(self._o_auth_token.access_token)}
        super().__init__(auth_params=auth_params)

    def is_valid(self):
        return (self._o_auth_token and isinstance(self._o_auth_token, OAuthToken)
                and not self.is_token_expired(self._o_auth_token))

    def get_authorization_url(self, state=None, additional_params=None):
        """ Builds and returns an authorization URL. The user is expected to
            obtain an authorization code from this URL and then call the authorize
            function with that authorization code.

        Args:
            state (str): An opaque state string.
            additional_params (dict): Any additional query parameters to be added to the URL.

        Returns:
            str: The authorization URL.

        """
        auth_url = self._config.get_base_uri(Server.AUTH_SERVER)
        auth_url += '/authorize'
        query_params = {
            'response_type': 'code',
            'client_id': self._o_auth_client_id,
            'redirect_uri': self._o_auth_redirect_uri
        }
        if self._o_auth_scopes:
            query_params['scope'] = ' '.join(self._o_auth_scopes)
        if state:
            query_params['state'] = state
        if additional_params:
            query_params.update(additional_params)
        auth_url = APIHelper.append_url_with_query_parameters(auth_url, query_params)
        return APIHelper.clean_url(auth_url)

    def build_basic_auth_header(self):
        """ Builds the basic auth header for endpoints in the
            OAuth Authorization Controller.

        Returns:
            str: The value of the Authentication header.

        """
        return "Basic {}".format(AuthHelper.get_base64_encoded_value(
            self._o_auth_client_id, self._o_auth_client_secret))

    def fetch_token(self, auth_code, additional_params=None):
        """ Authorizes the client.

            auth_code (str): The authentication code.
            additional_params (dict):  Any additional form parameters.

        Returns:
            OAuthToken: The OAuth token.

        """
        token = self._o_auth_api.request_token(
            self.build_basic_auth_header(),
            auth_code,
            self._o_auth_redirect_uri,
            _optional_form_parameters=additional_params
        ).body
        if hasattr(token, 'expires_in'):
            current_utc_timestamp = AuthHelper.get_current_utc_timestamp()
            token.expiry = AuthHelper.get_token_expiry(current_utc_timestamp, token.expires_in)
        return token

    def is_token_expired(self, o_auth_token=None):
        """ Checks if OAuth token has expired.

        Args:
            o_auth_token (OAuthToken): The OAuth token whose expiry is to be checked.

        Returns:
            bool: True if OAuth token has expired, False otherwise.

        """
        if o_auth_token is None:
            return (hasattr(self._o_auth_token, 'expiry')
                    and AuthHelper.is_token_expired(self._o_auth_token.expiry))

        return (hasattr(o_auth_token, 'expiry')
                and AuthHelper.is_token_expired(o_auth_token.expiry))

    def refresh_token(self, additional_params=None):
        """ Refreshes OAuth token.

        Args:
            additional_params (dict):  Any additional form parameters.

        Returns:
            OAuthToken: The refreshed OAuth token.

        """
        token = self._o_auth_api.refresh_token(
            self.build_basic_auth_header(),
            self._o_auth_token.refresh_token,
            ' '.join(self._o_auth_scopes) if self._o_auth_scopes else None,
            _optional_form_parameters=additional_params
        ).body
        if hasattr(token, 'expires_in'):
            current_utc_timestamp = AuthHelper.get_current_utc_timestamp()
            token.expiry = AuthHelper.get_token_expiry(current_utc_timestamp, token.expires_in)
        return token


class AuthorizationCodeAuthCredentials:

    @property
    def o_auth_client_id(self):
        return self._o_auth_client_id

    @property
    def o_auth_client_secret(self):
        return self._o_auth_client_secret

    @property
    def o_auth_redirect_uri(self):
        return self._o_auth_redirect_uri

    @property
    def o_auth_token(self):
        return self._o_auth_token

    @property
    def o_auth_scopes(self):
        return self._o_auth_scopes

    def __init__(self, o_auth_client_id, o_auth_client_secret,
                 o_auth_redirect_uri, o_auth_token=None, o_auth_scopes=None):
        if o_auth_client_id is None:
            raise ValueError('o_auth_client_id cannot be None')
        if o_auth_client_secret is None:
            raise ValueError('o_auth_client_secret cannot be None')
        if o_auth_redirect_uri is None:
            raise ValueError('o_auth_redirect_uri cannot be None')
        self._o_auth_client_id = o_auth_client_id
        self._o_auth_client_secret = o_auth_client_secret
        self._o_auth_redirect_uri = o_auth_redirect_uri
        self._o_auth_token = o_auth_token
        self._o_auth_scopes = o_auth_scopes

    def clone_with(self, o_auth_client_id=None, o_auth_client_secret=None,
                   o_auth_redirect_uri=None, o_auth_token=None,
                   o_auth_scopes=None):
        return AuthorizationCodeAuthCredentials(
            o_auth_client_id or self.o_auth_client_id,
            o_auth_client_secret or self.o_auth_client_secret,
            o_auth_redirect_uri or self.o_auth_redirect_uri,
            o_auth_token or self.o_auth_token,
            o_auth_scopes or self.o_auth_scopes)
