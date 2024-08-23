# Users

```python
users_controller = client.users
```

## Class Name

`UsersController`

## Methods

* [Get-Current-Users-Profile](../../doc/controllers/users.md#get-current-users-profile)
* [Get-Users-Profile](../../doc/controllers/users.md#get-users-profile)
* [Follow-Playlist](../../doc/controllers/users.md#follow-playlist)
* [Unfollow-Playlist](../../doc/controllers/users.md#unfollow-playlist)
* [Get-Followed](../../doc/controllers/users.md#get-followed)
* [Follow-Artists-Users](../../doc/controllers/users.md#follow-artists-users)
* [Unfollow-Artists-Users](../../doc/controllers/users.md#unfollow-artists-users)
* [Check-Current-User-Follows](../../doc/controllers/users.md#check-current-user-follows)
* [Check-If-User-Follows-Playlist](../../doc/controllers/users.md#check-if-user-follows-playlist)
* [Get-Users-Top-Artists](../../doc/controllers/users.md#get-users-top-artists)
* [Get-Users-Top-Tracks](../../doc/controllers/users.md#get-users-top-tracks)


# Get-Current-Users-Profile

Get detailed profile information about the current user (including the
current user's username).

```python
def get_current_users_profile(self)
```

## Requires scope

### oauth_2_0

`user-read-email`, `user-read-private`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PrivateUserObject`](../../doc/models/private-user-object.md).

## Example Usage

```python
result = users_controller.get_current_users_profile()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Get-Users-Profile

Get public profile information about a Spotify user.

```python
def get_users_profile(self,
                     user_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `user_id` | `str` | Template, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PublicUserObject`](../../doc/models/public-user-object.md).

## Example Usage

```python
user_id = 'smedjan'

result = users_controller.get_users_profile(user_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Follow-Playlist

Add the current user as a follower of a playlist.

```python
def follow_playlist(self,
                   playlist_id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_id` | `str` | Template, Required | - |
| `body` | [`PlaylistsFollowersRequest`](../../doc/models/playlists-followers-request.md) | Body, Optional | - |

## Requires scope

### oauth_2_0

`playlist-modify-private`, `playlist-modify-public`

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
playlist_id = '3cEYpjA9oz9GiPac4AsH4n'

body = PlaylistsFollowersRequest(
    public=False
)

result = users_controller.follow_playlist(
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


# Unfollow-Playlist

Remove the current user as a follower of a playlist.

```python
def unfollow_playlist(self,
                     playlist_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_id` | `str` | Template, Required | - |

## Requires scope

### oauth_2_0

`playlist-modify-private`, `playlist-modify-public`

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
playlist_id = '3cEYpjA9oz9GiPac4AsH4n'

result = users_controller.unfollow_playlist(playlist_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Get-Followed

Get the current user's followed artists.

```python
def get_followed(self,
                mtype,
                after=None,
                limit=20)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`ItemType1Enum`](../../doc/models/item-type-1-enum.md) | Query, Required | - |
| `after` | `str` | Query, Optional | - |
| `limit` | `int` | Query, Optional | - |

## Requires scope

### oauth_2_0

`user-follow-read`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`CursorPagedArtists`](../../doc/models/cursor-paged-artists.md).

## Example Usage

```python
mtype = ItemType1Enum.ARTIST

after = '0I2XqVXqHScXjHhk6AYYRe'

limit = 10

result = users_controller.get_followed(
    mtype,
    after=after,
    limit=limit
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Follow-Artists-Users

Add the current user as a follower of one or more artists or other Spotify users.

```python
def follow_artists_users(self,
                        mtype,
                        ids,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`ItemType2Enum`](../../doc/models/item-type-2-enum.md) | Query, Required | - |
| `ids` | `str` | Query, Required | - |
| `body` | [`MeFollowingRequest`](../../doc/models/me-following-request.md) | Body, Optional | - |

## Requires scope

### oauth_2_0

`user-follow-modify`

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
mtype = ItemType2Enum.ARTIST

ids = '2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6'

result = users_controller.follow_artists_users(
    mtype,
    ids
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Unfollow-Artists-Users

Remove the current user as a follower of one or more artists or other Spotify users.

```python
def unfollow_artists_users(self,
                          mtype,
                          ids,
                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`ItemType3Enum`](../../doc/models/item-type-3-enum.md) | Query, Required | - |
| `ids` | `str` | Query, Required | - |
| `body` | [`MeFollowingRequest1`](../../doc/models/me-following-request-1.md) | Body, Optional | - |

## Requires scope

### oauth_2_0

`user-follow-modify`

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
mtype = ItemType3Enum.ARTIST

ids = '2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6'

result = users_controller.unfollow_artists_users(
    mtype,
    ids
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Check-Current-User-Follows

Check to see if the current user is following one or more artists or other Spotify users.

```python
def check_current_user_follows(self,
                              mtype,
                              ids)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`ItemType3Enum`](../../doc/models/item-type-3-enum.md) | Query, Required | - |
| `ids` | `str` | Query, Required | - |

## Requires scope

### oauth_2_0

`user-follow-read`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type `List[bool]`.

## Example Usage

```python
mtype = ItemType3Enum.ARTIST

ids = '2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6'

result = users_controller.check_current_user_follows(
    mtype,
    ids
)
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


# Check-If-User-Follows-Playlist

Check to see if one or more Spotify users are following a specified playlist.

```python
def check_if_user_follows_playlist(self,
                                  playlist_id,
                                  ids)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `playlist_id` | `str` | Template, Required | - |
| `ids` | `str` | Query, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type `List[bool]`.

## Example Usage

```python
playlist_id = '3cEYpjA9oz9GiPac4AsH4n'

ids = 'jmperezperez,thelinmichael,wizzler'

result = users_controller.check_if_user_follows_playlist(
    playlist_id,
    ids
)
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


# Get-Users-Top-Artists

Get the current user's top artists based on calculated affinity.

```python
def get_users_top_artists(self,
                         time_range='medium_term',
                         limit=20,
                         offset=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time_range` | `str` | Query, Optional | - |
| `limit` | `int` | Query, Optional | - |
| `offset` | `int` | Query, Optional | - |

## Requires scope

### oauth_2_0

`user-top-read`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PagingArtistObject`](../../doc/models/paging-artist-object.md).

## Example Usage

```python
time_range = 'medium_term'

limit = 10

offset = 5

result = users_controller.get_users_top_artists(
    time_range=time_range,
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


# Get-Users-Top-Tracks

Get the current user's top tracks based on calculated affinity.

```python
def get_users_top_tracks(self,
                        time_range='medium_term',
                        limit=20,
                        offset=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `time_range` | `str` | Query, Optional | - |
| `limit` | `int` | Query, Optional | - |
| `offset` | `int` | Query, Optional | - |

## Requires scope

### oauth_2_0

`user-top-read`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PagingTrackObject`](../../doc/models/paging-track-object.md).

## Example Usage

```python
time_range = 'medium_term'

limit = 10

offset = 5

result = users_controller.get_users_top_tracks(
    time_range=time_range,
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

