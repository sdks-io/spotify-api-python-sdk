# Playlists

```python
playlists_controller = client.playlists
```

## Class Name

`PlaylistsController`

## Methods

* [Get-Playlist](../../doc/controllers/playlists.md#get-playlist)
* [Change-Playlist-Details](../../doc/controllers/playlists.md#change-playlist-details)
* [Get-Playlists-Tracks](../../doc/controllers/playlists.md#get-playlists-tracks)
* [Add-Tracks-to-Playlist](../../doc/controllers/playlists.md#add-tracks-to-playlist)
* [Reorder-or-Replace-Playlists-Tracks](../../doc/controllers/playlists.md#reorder-or-replace-playlists-tracks)
* [Remove-Tracks-Playlist](../../doc/controllers/playlists.md#remove-tracks-playlist)
* [Get-a-List-of-Current-Users-Playlists](../../doc/controllers/playlists.md#get-a-list-of-current-users-playlists)
* [Get-List-Users-Playlists](../../doc/controllers/playlists.md#get-list-users-playlists)
* [Create-Playlist](../../doc/controllers/playlists.md#create-playlist)
* [Get-Featured-Playlists](../../doc/controllers/playlists.md#get-featured-playlists)
* [Get-a-Categories-Playlists](../../doc/controllers/playlists.md#get-a-categories-playlists)
* [Get-Playlist-Cover](../../doc/controllers/playlists.md#get-playlist-cover)
* [Upload-Custom-Playlist-Cover](../../doc/controllers/playlists.md#upload-custom-playlist-cover)


# Get-Playlist

Get a playlist owned by a Spotify user.

```python
def get_playlist(self,
                playlist_id,
                market=None,
                fields=None,
                additional_types=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_id` | `str` | Template, Required | - |
| `market` | `str` | Query, Optional | - |
| `fields` | `str` | Query, Optional | - |
| `additional_types` | `str` | Query, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PlaylistObject`](../../doc/models/playlist-object.md).

## Example Usage

```python
playlist_id = '3cEYpjA9oz9GiPac4AsH4n'

market = 'ES'

fields = 'items(added_by.id,track(name,href,album(name,href)))'

result = playlists_controller.get_playlist(
    playlist_id,
    market=market,
    fields=fields
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Change-Playlist-Details

Change a playlist's name and public/private state. (The user must, of
course, own the playlist.)

```python
def change_playlist_details(self,
                           playlist_id,
                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_id` | `str` | Template, Required | - |
| `body` | [`PlaylistsRequest`](../../doc/models/playlists-request.md) | Body, Optional | - |

## Requires scope

### oauth_2_0

`playlist-modify-private`, `playlist-modify-public`

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
playlist_id = '3cEYpjA9oz9GiPac4AsH4n'

body = PlaylistsRequest(
    name='Updated Playlist Name',
    public=False,
    description='Updated playlist description'
)

result = playlists_controller.change_playlist_details(
    playlist_id,
    body=body
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Get-Playlists-Tracks

Get full details of the items of a playlist owned by a Spotify user.

```python
def get_playlists_tracks(self,
                        playlist_id,
                        market=None,
                        fields=None,
                        limit=20,
                        offset=0,
                        additional_types=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_id` | `str` | Template, Required | - |
| `market` | `str` | Query, Optional | - |
| `fields` | `str` | Query, Optional | - |
| `limit` | `int` | Query, Optional | - |
| `offset` | `int` | Query, Optional | - |
| `additional_types` | `str` | Query, Optional | - |

## Requires scope

### oauth_2_0

`playlist-read-private`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PagingPlaylistTrackObject`](../../doc/models/paging-playlist-track-object.md).

## Example Usage

```python
playlist_id = '3cEYpjA9oz9GiPac4AsH4n'

market = 'ES'

fields = 'items(added_by.id,track(name,href,album(name,href)))'

limit = 10

offset = 5

result = playlists_controller.get_playlists_tracks(
    playlist_id,
    market=market,
    fields=fields,
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


# Add-Tracks-to-Playlist

Add one or more items to a user's playlist.

```python
def add_tracks_to_playlist(self,
                          playlist_id,
                          position=None,
                          uris=None,
                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_id` | `str` | Template, Required | - |
| `position` | `int` | Query, Optional | - |
| `uris` | `str` | Query, Optional | - |
| `body` | [`PlaylistsTracksRequest`](../../doc/models/playlists-tracks-request.md) | Body, Optional | - |

## Requires scope

### oauth_2_0

`playlist-modify-private`, `playlist-modify-public`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PlaylistSnapshotId`](../../doc/models/playlist-snapshot-id.md).

## Example Usage

```python
playlist_id = '3cEYpjA9oz9GiPac4AsH4n'

position = 0

uris = 'spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M'

result = playlists_controller.add_tracks_to_playlist(
    playlist_id,
    position=position,
    uris=uris
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Reorder-or-Replace-Playlists-Tracks

Either reorder or replace items in a playlist depending on the request's parameters.
To reorder items, include `range_start`, `insert_before`, `range_length` and `snapshot_id` in the request's body.
To replace items, include `uris` as either a query parameter or in the request's body.
Replacing items in a playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a playlist.
<br/>
**Note**: Replace and reorder are mutually exclusive operations which share the same endpoint, but have different parameters.
These operations can't be applied together in a single request.

```python
def reorder_or_replace_playlists_tracks(self,
                                       playlist_id,
                                       uris=None,
                                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_id` | `str` | Template, Required | - |
| `uris` | `str` | Query, Optional | - |
| `body` | [`PlaylistsTracksRequest1`](../../doc/models/playlists-tracks-request-1.md) | Body, Optional | - |

## Requires scope

### oauth_2_0

`playlist-modify-private`, `playlist-modify-public`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PlaylistSnapshotId`](../../doc/models/playlist-snapshot-id.md).

## Example Usage

```python
playlist_id = '3cEYpjA9oz9GiPac4AsH4n'

body = PlaylistsTracksRequest1(
    range_start=1,
    insert_before=3,
    range_length=2
)

result = playlists_controller.reorder_or_replace_playlists_tracks(
    playlist_id,
    body=body
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Remove-Tracks-Playlist

Remove one or more items from a user's playlist.

```python
def remove_tracks_playlist(self,
                          playlist_id,
                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_id` | `str` | Template, Required | - |
| `body` | [`PlaylistsTracksRequest2`](../../doc/models/playlists-tracks-request-2.md) | Body, Optional | - |

## Requires scope

### oauth_2_0

`playlist-modify-private`, `playlist-modify-public`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PlaylistSnapshotId`](../../doc/models/playlist-snapshot-id.md).

## Example Usage

```python
playlist_id = '3cEYpjA9oz9GiPac4AsH4n'

body = PlaylistsTracksRequest2(
    tracks=[
        Track1()
    ]
)

result = playlists_controller.remove_tracks_playlist(
    playlist_id,
    body=body
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Get-a-List-of-Current-Users-Playlists

Get a list of the playlists owned or followed by the current Spotify
user.

```python
def get_a_list_of_current_users_playlists(self,
                                         limit=20,
                                         offset=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | - |
| `offset` | `int` | Query, Optional | - |

## Requires scope

### oauth_2_0

`playlist-read-private`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PagingPlaylistObject`](../../doc/models/paging-playlist-object.md).

## Example Usage

```python
limit = 10

offset = 5

result = playlists_controller.get_a_list_of_current_users_playlists(
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


# Get-List-Users-Playlists

Get a list of the playlists owned or followed by a Spotify user.

```python
def get_list_users_playlists(self,
                            user_id,
                            limit=20,
                            offset=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `str` | Template, Required | - |
| `limit` | `int` | Query, Optional | - |
| `offset` | `int` | Query, Optional | - |

## Requires scope

### oauth_2_0

`playlist-read-collaborative`, `playlist-read-private`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PagingPlaylistObject`](../../doc/models/paging-playlist-object.md).

## Example Usage

```python
user_id = 'smedjan'

limit = 10

offset = 5

result = playlists_controller.get_list_users_playlists(
    user_id,
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


# Create-Playlist

Create a playlist for a Spotify user. (The playlist will be empty until
you [add tracks](/documentation/web-api/reference/add-tracks-to-playlist).)
Each user is generally limited to a maximum of 11000 playlists.

```python
def create_playlist(self,
                   user_id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `str` | Template, Required | - |
| `body` | [`UsersPlaylistsRequest`](../../doc/models/users-playlists-request.md) | Body, Optional | - |

## Requires scope

### oauth_2_0

`playlist-modify-private`, `playlist-modify-public`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PlaylistObject`](../../doc/models/playlist-object.md).

## Example Usage

```python
user_id = 'smedjan'

body = UsersPlaylistsRequest(
    name='New Playlist',
    public=False,
    description='New playlist description'
)

result = playlists_controller.create_playlist(
    user_id,
    body=body
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Get-Featured-Playlists

Get a list of Spotify featured playlists (shown, for example, on a Spotify player's 'Browse' tab).

```python
def get_featured_playlists(self,
                          locale=None,
                          limit=20,
                          offset=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `locale` | `str` | Query, Optional | - |
| `limit` | `int` | Query, Optional | - |
| `offset` | `int` | Query, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PagingFeaturedPlaylistObject`](../../doc/models/paging-featured-playlist-object.md).

## Example Usage

```python
locale = 'sv_SE'

limit = 10

offset = 5

result = playlists_controller.get_featured_playlists(
    locale=locale,
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


# Get-a-Categories-Playlists

Get a list of Spotify playlists tagged with a particular category.

```python
def get_a_categories_playlists(self,
                              category_id,
                              limit=20,
                              offset=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category_id` | `str` | Template, Required | - |
| `limit` | `int` | Query, Optional | - |
| `offset` | `int` | Query, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PagingFeaturedPlaylistObject`](../../doc/models/paging-featured-playlist-object.md).

## Example Usage

```python
category_id = 'dinner'

limit = 10

offset = 5

result = playlists_controller.get_a_categories_playlists(
    category_id,
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


# Get-Playlist-Cover

Get the current image associated with a specific playlist.

```python
def get_playlist_cover(self,
                      playlist_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_id` | `str` | Template, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`List[ImageObject]`](../../doc/models/image-object.md).

## Example Usage

```python
playlist_id = '3cEYpjA9oz9GiPac4AsH4n'

result = playlists_controller.get_playlist_cover(playlist_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Upload-Custom-Playlist-Cover

Replace the image used to represent a specific playlist.

```python
def upload_custom_playlist_cover(self,
                                playlist_id,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_id` | `str` | Template, Required | - |
| `body` | `object` | Body, Required | - |

## Requires scope

### oauth_2_0

`playlist-modify-private`, `playlist-modify-public`, `ugc-image-upload`

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
playlist_id = '3cEYpjA9oz9GiPac4AsH4n'

body = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = playlists_controller.upload_custom_playlist_cover(
    playlist_id,
    body
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |

