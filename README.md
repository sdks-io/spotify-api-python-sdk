
# Getting Started with Spotify Web API

## Introduction

You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.

In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href="https://developer.spotify.com/documentation/general/guides/authorization-guide/">OAuth 2.0</a>.

The base URI for all Web API requests is `https://api.spotify.com/v1`.

Need help? See our <a href="https://developer.spotify.com/documentation/web-api/guides/">Web API guides</a> for more information, or visit the <a href="https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer">Spotify for Developers community forum</a> to ask questions and connect with other developers.

## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install spotify-api-sdk==1.0.0
```

You can also view the package at:
https://pypi.python.org/pypi/spotify-api-sdk/1.0.0

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `environment` | `Environment` | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `authorization_code_auth_credentials` | [`AuthorizationCodeAuthCredentials`](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/auth/oauth-2-authorization-code-grant.md) | The credential object for OAuth 2 Authorization Code Grant |

The API client can be initialized as follows:

```python
client = SpotifywebapiClient(
    authorization_code_auth_credentials=AuthorizationCodeAuthCredentials(
        o_auth_client_id='OAuthClientId',
        o_auth_client_secret='OAuthClientSecret',
        o_auth_redirect_uri='OAuthRedirectUri',
        o_auth_scopes=[
            OAuthScopeEnum.APP_REMOTE_CONTROL,
            OAuthScopeEnum.PLAYLIST_READ_PRIVATE
        ]
    )
)
```

API calls return an `ApiResponse` object that includes the following fields:

| Field | Description |
|  --- | --- |
| `status_code` | Status code of the HTTP response |
| `reason_phrase` | Reason phrase of the HTTP response |
| `headers` | Headers of the HTTP response as a dictionary |
| `text` | The body of the HTTP response as a string |
| `request` | HTTP request info |
| `errors` | Errors, if they exist |
| `body` | The deserialized body of the HTTP response |

## Authorization

This API uses the following authentication schemes.

* [`oauth_2_0 (OAuth 2 Authorization Code Grant)`](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/auth/oauth-2-authorization-code-grant.md)

## List of APIs

* [Albums](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/controllers/albums.md)
* [Artists](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/controllers/artists.md)
* [Audiobooks](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/controllers/audiobooks.md)
* [Categories](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/controllers/categories.md)
* [Chapters](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/controllers/chapters.md)
* [Episodes](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/controllers/episodes.md)
* [Genres](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/controllers/genres.md)
* [Markets](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/controllers/markets.md)
* [Player](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/controllers/player.md)
* [Playlists](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/controllers/playlists.md)
* [Search](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/controllers/search.md)
* [Shows](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/controllers/shows.md)
* [Tracks](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/controllers/tracks.md)
* [Users](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/controllers/users.md)

## Classes Documentation

* [Utility Classes](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/utility-classes.md)
* [HttpResponse](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/http-response.md)
* [HttpRequest](https://www.github.com/sdks-io/spotify-api-python-sdk/tree/1.0.0/doc/http-request.md)

