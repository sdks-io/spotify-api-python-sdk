# -*- coding: utf-8 -*-

"""
spotifywebapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from spotifywebapi.api_helper import APIHelper
from spotifywebapi.configuration import Server
from spotifywebapi.http.api_response import ApiResponse
from spotifywebapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from spotifywebapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from spotifywebapi.models.show_object import ShowObject
from spotifywebapi.models.many_simplified_shows import ManySimplifiedShows
from spotifywebapi.models.paging_simplified_episode_object import PagingSimplifiedEpisodeObject
from spotifywebapi.models.paging_saved_show_object import PagingSavedShowObject
from spotifywebapi.exceptions.unauthorized_exception import UnauthorizedException
from spotifywebapi.exceptions.forbidden_exception import ForbiddenException
from spotifywebapi.exceptions.too_many_requests_exception import TooManyRequestsException


class ShowsController(BaseController):

    """A Controller to access Endpoints in the spotifywebapi API."""
    def __init__(self, config):
        super(ShowsController, self).__init__(config)

    def get_a_show(self,
                   id,
                   market=None):
        """Does a GET request to /shows/{id}.

        Get Spotify catalog information for a single show identified by its
        unique Spotify ID.

        Args:
            id (str): TODO: type description here.
            market (str, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A show

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/shows/{id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('market')
                         .value(market))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ShowObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_multiple_shows(self,
                           ids,
                           market=None):
        """Does a GET request to /shows.

        Get Spotify catalog information for several shows based on their
        Spotify IDs.

        Args:
            ids (str): TODO: type description here.
            market (str, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A set of
                shows

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/shows')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('ids')
                         .value(ids))
            .query_param(Parameter()
                         .key('market')
                         .value(market))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ManySimplifiedShows.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_a_shows_episodes(self,
                             id,
                             market=None,
                             limit=20,
                             offset=0):
        """Does a GET request to /shows/{id}/episodes.

        Get Spotify catalog information about an show’s episodes. Optional
        parameters can be used to limit the number of episodes returned.

        Args:
            id (str): TODO: type description here.
            market (str, optional): TODO: type description here.
            limit (int, optional): TODO: type description here. Example: 20
            offset (int, optional): TODO: type description here. Example: 0

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Pages of
                episodes

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/shows/{id}/episodes')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('market')
                         .value(market))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('offset')
                         .value(offset))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PagingSimplifiedEpisodeObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_users_saved_shows(self,
                              limit=20,
                              offset=0):
        """Does a GET request to /me/shows.

        Get a list of shows saved in the current Spotify user's library.
        Optional parameters can be used to limit the number of shows
        returned.

        Args:
            limit (int, optional): TODO: type description here. Example: 20
            offset (int, optional): TODO: type description here. Example: 0

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Pages of
                shows

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/shows')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('offset')
                         .value(offset))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PagingSavedShowObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def save_shows_user(self,
                        ids,
                        body=None):
        """Does a PUT request to /me/shows.

        Save one or more shows to current Spotify user's library.

        Args:
            ids (str): TODO: type description here.
            body (MeShowsRequest, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Show
                saved

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/shows')
            .http_method(HttpMethodEnum.PUT)
            .query_param(Parameter()
                         .key('ids')
                         .value(ids))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def remove_shows_user(self,
                          ids,
                          market=None,
                          body=None):
        """Does a DELETE request to /me/shows.

        Delete one or more shows from current Spotify user's library.

        Args:
            ids (str): TODO: type description here.
            market (str, optional): TODO: type description here.
            body (MeShowsRequest, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Show
                removed

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/shows')
            .http_method(HttpMethodEnum.DELETE)
            .query_param(Parameter()
                         .key('ids')
                         .value(ids))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .query_param(Parameter()
                         .key('market')
                         .value(market))
            .body_param(Parameter()
                        .value(body))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def check_users_saved_shows(self,
                                ids):
        """Does a GET request to /me/shows/contains.

        Check if one or more shows is already saved in the current Spotify
        user's library.

        Args:
            ids (str): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Array of
                booleans

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/shows/contains')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('ids')
                         .value(ids))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()
