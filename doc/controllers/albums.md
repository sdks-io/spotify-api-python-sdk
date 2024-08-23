# Albums

```python
albums_controller = client.albums
```

## Class Name

`AlbumsController`

## Methods

* [Get-an-Album](../../doc/controllers/albums.md#get-an-album)
* [Get-Multiple-Albums](../../doc/controllers/albums.md#get-multiple-albums)
* [Get-an-Albums-Tracks](../../doc/controllers/albums.md#get-an-albums-tracks)
* [Get-Users-Saved-Albums](../../doc/controllers/albums.md#get-users-saved-albums)
* [Save-Albums-User](../../doc/controllers/albums.md#save-albums-user)
* [Remove-Albums-User](../../doc/controllers/albums.md#remove-albums-user)
* [Check-Users-Saved-Albums](../../doc/controllers/albums.md#check-users-saved-albums)
* [Get-New-Releases](../../doc/controllers/albums.md#get-new-releases)


# Get-an-Album

Get Spotify catalog information for a single album.

```python
def get_an_album(self,
                id,
                market=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |
| `market` | `str` | Query, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AlbumObject`](../../doc/models/album-object.md).

## Example Usage

```python
id = '4aawyAB9vmqN3uQ7FjRGTy'

market = 'ES'

result = albums_controller.get_an_album(
    id,
    market=market
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Get-Multiple-Albums

Get Spotify catalog information for multiple albums identified by their Spotify IDs.

```python
def get_multiple_albums(self,
                       ids,
                       market=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `str` | Query, Required | - |
| `market` | `str` | Query, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ManyAlbums`](../../doc/models/many-albums.md).

## Example Usage

```python
ids = '382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc'

market = 'ES'

result = albums_controller.get_multiple_albums(
    ids,
    market=market
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Get-an-Albums-Tracks

Get Spotify catalog information about an album’s tracks.
Optional parameters can be used to limit the number of tracks returned.

```python
def get_an_albums_tracks(self,
                        id,
                        market=None,
                        limit=20,
                        offset=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |
| `market` | `str` | Query, Optional | - |
| `limit` | `int` | Query, Optional | - |
| `offset` | `int` | Query, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PagingSimplifiedTrackObject`](../../doc/models/paging-simplified-track-object.md).

## Example Usage

```python
id = '4aawyAB9vmqN3uQ7FjRGTy'

market = 'ES'

limit = 10

offset = 5

result = albums_controller.get_an_albums_tracks(
    id,
    market=market,
    limit=limit,
    offset=offset
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Get-Users-Saved-Albums

Get a list of the albums saved in the current Spotify user's 'Your Music' library.

```python
def get_users_saved_albums(self,
                          limit=20,
                          offset=0,
                          market=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | - |
| `offset` | `int` | Query, Optional | - |
| `market` | `str` | Query, Optional | - |

## Requires scope

### oauth_2_0

`user-library-read`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PagingSavedAlbumObject`](../../doc/models/paging-saved-album-object.md).

## Example Usage

```python
limit = 10

offset = 5

market = 'ES'

result = albums_controller.get_users_saved_albums(
    limit=limit,
    offset=offset,
    market=market
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Save-Albums-User

Save one or more albums to the current user's 'Your Music' library.

```python
def save_albums_user(self,
                    ids,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `str` | Query, Required | - |
| `body` | [`MeAlbumsRequest`](../../doc/models/me-albums-request.md) | Body, Optional | - |

## Requires scope

### oauth_2_0

`user-library-modify`

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
ids = '382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc'

result = albums_controller.save_albums_user(ids)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Remove-Albums-User

Remove one or more albums from the current user's 'Your Music' library.

```python
def remove_albums_user(self,
                      ids,
                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `str` | Query, Required | - |
| `body` | [`MeAlbumsRequest`](../../doc/models/me-albums-request.md) | Body, Optional | - |

## Requires scope

### oauth_2_0

`user-library-modify`

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
ids = '382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc'

result = albums_controller.remove_albums_user(ids)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Check-Users-Saved-Albums

Check if one or more albums is already saved in the current Spotify user's 'Your Music' library.

```python
def check_users_saved_albums(self,
                            ids)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `str` | Query, Required | - |

## Requires scope

### oauth_2_0

`user-library-read`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type `List[bool]`.

## Example Usage

```python
ids = '382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc'

result = albums_controller.check_users_saved_albums(ids)
```

## Example Response

```
[
  false,
  true
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Get-New-Releases

Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse” tab).

```python
def get_new_releases(self,
                    limit=20,
                    offset=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | - |
| `offset` | `int` | Query, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PagedAlbums`](../../doc/models/paged-albums.md).

## Example Usage

```python
limit = 10

offset = 5

result = albums_controller.get_new_releases(
    limit=limit,
    offset=offset
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |

