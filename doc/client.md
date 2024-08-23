
# Client Class Documentation

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
| `authorization_code_auth_credentials` | [`AuthorizationCodeAuthCredentials`](auth/oauth-2-authorization-code-grant.md) | The credential object for OAuth 2 Authorization Code Grant |

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

## Spotify Web API Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| albums | Gets AlbumsController |
| artists | Gets ArtistsController |
| audiobooks | Gets AudiobooksController |
| categories | Gets CategoriesController |
| chapters | Gets ChaptersController |
| episodes | Gets EpisodesController |
| genres | Gets GenresController |
| markets | Gets MarketsController |
| player | Gets PlayerController |
| playlists | Gets PlaylistsController |
| search | Gets SearchController |
| shows | Gets ShowsController |
| tracks | Gets TracksController |
| users | Gets UsersController |
| o_auth_authorization | Gets OAuthAuthorizationController |

