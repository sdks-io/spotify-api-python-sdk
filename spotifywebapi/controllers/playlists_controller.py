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
from spotifywebapi.models.playlist_object import PlaylistObject
from spotifywebapi.models.paging_playlist_track_object import PagingPlaylistTrackObject
from spotifywebapi.models.playlist_snapshot_id import PlaylistSnapshotId
from spotifywebapi.models.paging_playlist_object import PagingPlaylistObject
from spotifywebapi.models.paging_featured_playlist_object import PagingFeaturedPlaylistObject
from spotifywebapi.models.image_object import ImageObject
from spotifywebapi.exceptions.unauthorized_exception import UnauthorizedException
from spotifywebapi.exceptions.forbidden_exception import ForbiddenException
from spotifywebapi.exceptions.too_many_requests_exception import TooManyRequestsException


class PlaylistsController(BaseController):

    """A Controller to access Endpoints in the spotifywebapi API."""
    def __init__(self, config):
        super(PlaylistsController, self).__init__(config)

    def get_playlist(self,
                     playlist_id,
                     market=None,
                     fields=None,
                     additional_types=None):
        """Does a GET request to /playlists/{playlist_id}.

        Get a playlist owned by a Spotify user.

        Args:
            playlist_id (str): TODO: type description here.
            market (str, optional): TODO: type description here.
            fields (str, optional): TODO: type description here.
            additional_types (str, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                playlist

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/playlists/{playlist_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('playlist_id')
                            .value(playlist_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('market')
                         .value(market))
            .query_param(Parameter()
                         .key('fields')
                         .value(fields))
            .query_param(Parameter()
                         .key('additional_types')
                         .value(additional_types))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PlaylistObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def change_playlist_details(self,
                                playlist_id,
                                body=None):
        """Does a PUT request to /playlists/{playlist_id}.

        Change a playlist's name and public/private state. (The user must, of
        course, own the playlist.)

        Args:
            playlist_id (str): TODO: type description here.
            body (PlaylistsRequest, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Playlist
                updated

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/playlists/{playlist_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('playlist_id')
                            .value(playlist_id)
                            .should_encode(True))
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

    def get_playlists_tracks(self,
                             playlist_id,
                             market=None,
                             fields=None,
                             limit=20,
                             offset=0,
                             additional_types=None):
        """Does a GET request to /playlists/{playlist_id}/tracks.

        Get full details of the items of a playlist owned by a Spotify user.

        Args:
            playlist_id (str): TODO: type description here.
            market (str, optional): TODO: type description here.
            fields (str, optional): TODO: type description here.
            limit (int, optional): TODO: type description here. Example: 20
            offset (int, optional): TODO: type description here. Example: 0
            additional_types (str, optional): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Pages of
                tracks

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/playlists/{playlist_id}/tracks')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('playlist_id')
                            .value(playlist_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('market')
                         .value(market))
            .query_param(Parameter()
                         .key('fields')
                         .value(fields))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('offset')
                         .value(offset))
            .query_param(Parameter()
                         .key('additional_types')
                         .value(additional_types))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PagingPlaylistTrackObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def add_tracks_to_playlist(self,
                               playlist_id,
                               position=None,
                               uris=None,
                               body=None):
        """Does a POST request to /playlists/{playlist_id}/tracks.

        Add one or more items to a user's playlist.

        Args:
            playlist_id (str): TODO: type description here.
            position (int, optional): TODO: type description here.
            uris (str, optional): TODO: type description here.
            body (PlaylistsTracksRequest, optional): TODO: type description
                here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                snapshot ID for the playlist

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/playlists/{playlist_id}/tracks')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('playlist_id')
                            .value(playlist_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .query_param(Parameter()
                         .key('position')
                         .value(position))
            .query_param(Parameter()
                         .key('uris')
                         .value(uris))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PlaylistSnapshotId.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def reorder_or_replace_playlists_tracks(self,
                                            playlist_id,
                                            uris=None,
                                            body=None):
        """Does a PUT request to /playlists/{playlist_id}/tracks.

        Either reorder or replace items in a playlist depending on the
        request's parameters.
        To reorder items, include `range_start`, `insert_before`,
        `range_length` and `snapshot_id` in the request's body.
        To replace items, include `uris` as either a query parameter or in the
        request's body.
        Replacing items in a playlist will overwrite its existing items. This
        operation can be used for replacing or clearing items in a playlist.
        <br/>
        **Note**: Replace and reorder are mutually exclusive operations which
        share the same endpoint, but have different parameters.
        These operations can't be applied together in a single request.

        Args:
            playlist_id (str): TODO: type description here.
            uris (str, optional): TODO: type description here.
            body (PlaylistsTracksRequest1, optional): TODO: type description
                here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                snapshot ID for the playlist

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/playlists/{playlist_id}/tracks')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('playlist_id')
                            .value(playlist_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .query_param(Parameter()
                         .key('uris')
                         .value(uris))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PlaylistSnapshotId.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def remove_tracks_playlist(self,
                               playlist_id,
                               body=None):
        """Does a DELETE request to /playlists/{playlist_id}/tracks.

        Remove one or more items from a user's playlist.

        Args:
            playlist_id (str): TODO: type description here.
            body (PlaylistsTracksRequest2, optional): TODO: type description
                here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                snapshot ID for the playlist

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/playlists/{playlist_id}/tracks')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('playlist_id')
                            .value(playlist_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PlaylistSnapshotId.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_a_list_of_current_users_playlists(self,
                                              limit=20,
                                              offset=0):
        """Does a GET request to /me/playlists.

        Get a list of the playlists owned or followed by the current Spotify
        user.

        Args:
            limit (int, optional): TODO: type description here. Example: 20
            offset (int, optional): TODO: type description here. Example: 0

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A paged
                set of playlists

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/me/playlists')
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
            .deserialize_into(PagingPlaylistObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_list_users_playlists(self,
                                 user_id,
                                 limit=20,
                                 offset=0):
        """Does a GET request to /users/{user_id}/playlists.

        Get a list of the playlists owned or followed by a Spotify user.

        Args:
            user_id (str): TODO: type description here.
            limit (int, optional): TODO: type description here. Example: 20
            offset (int, optional): TODO: type description here. Example: 0

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A paged
                set of playlists

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/users/{user_id}/playlists')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('user_id')
                            .value(user_id)
                            .should_encode(True))
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
            .deserialize_into(PagingPlaylistObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def create_playlist(self,
                        user_id,
                        body=None):
        """Does a POST request to /users/{user_id}/playlists.

        Create a playlist for a Spotify user. (The playlist will be empty
        until
        you [add
        tracks](/documentation/web-api/reference/add-tracks-to-playlist).)
        Each user is generally limited to a maximum of 11000 playlists.

        Args:
            user_id (str): TODO: type description here.
            body (UsersPlaylistsRequest, optional): TODO: type description
                here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A
                playlist

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/users/{user_id}/playlists')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('user_id')
                            .value(user_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PlaylistObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_featured_playlists(self,
                               locale=None,
                               limit=20,
                               offset=0):
        """Does a GET request to /browse/featured-playlists.

        Get a list of Spotify featured playlists (shown, for example, on a
        Spotify player's 'Browse' tab).

        Args:
            locale (str, optional): TODO: type description here.
            limit (int, optional): TODO: type description here. Example: 20
            offset (int, optional): TODO: type description here. Example: 0

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A paged
                set of playlists

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/browse/featured-playlists')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('locale')
                         .value(locale))
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
            .deserialize_into(PagingFeaturedPlaylistObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_a_categories_playlists(self,
                                   category_id,
                                   limit=20,
                                   offset=0):
        """Does a GET request to /browse/categories/{category_id}/playlists.

        Get a list of Spotify playlists tagged with a particular category.

        Args:
            category_id (str): TODO: type description here.
            limit (int, optional): TODO: type description here. Example: 20
            offset (int, optional): TODO: type description here. Example: 0

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A paged
                set of playlists

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/browse/categories/{category_id}/playlists')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('category_id')
                            .value(category_id)
                            .should_encode(True))
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
            .deserialize_into(PagingFeaturedPlaylistObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def get_playlist_cover(self,
                           playlist_id):
        """Does a GET request to /playlists/{playlist_id}/images.

        Get the current image associated with a specific playlist.

        Args:
            playlist_id (str): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A set of
                images

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/playlists/{playlist_id}/images')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('playlist_id')
                            .value(playlist_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ImageObject.from_dictionary)
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()

    def upload_custom_playlist_cover(self,
                                     playlist_id,
                                     body):
        """Does a PUT request to /playlists/{playlist_id}/images.

        Replace the image used to represent a specific playlist.

        Args:
            playlist_id (str): TODO: type description here.
            body (object): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Image
                uploaded

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/playlists/{playlist_id}/images')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('playlist_id')
                            .value(playlist_id)
                            .should_encode(True))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/json; charset=utf-8'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oauth_2_0'))
        ).response(
            ResponseHandler()
            .is_api_response(True)
            .local_error('401', 'Bad or expired token. This can happen if the user revoked a token or\nthe access token has expired. You should re-authenticate the user.\n', UnauthorizedException)
            .local_error('403', 'Bad OAuth request (wrong consumer key, bad nonce, expired\ntimestamp...). Unfortunately, re-authenticating the user won\'t help here.\n', ForbiddenException)
            .local_error('429', 'The app has exceeded its rate limits.\n', TooManyRequestsException)
        ).execute()
