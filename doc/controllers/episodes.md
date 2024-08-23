# Episodes

```python
episodes_controller = client.episodes
```

## Class Name

`EpisodesController`

## Methods

* [Get-an-Episode](../../doc/controllers/episodes.md#get-an-episode)
* [Get-Multiple-Episodes](../../doc/controllers/episodes.md#get-multiple-episodes)
* [Get-Users-Saved-Episodes](../../doc/controllers/episodes.md#get-users-saved-episodes)
* [Save-Episodes-User](../../doc/controllers/episodes.md#save-episodes-user)
* [Remove-Episodes-User](../../doc/controllers/episodes.md#remove-episodes-user)
* [Check-Users-Saved-Episodes](../../doc/controllers/episodes.md#check-users-saved-episodes)


# Get-an-Episode

Get Spotify catalog information for a single episode identified by its
unique Spotify ID.

```python
def get_an_episode(self,
                  id,
                  market=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |
| `market` | `str` | Query, Optional | - |

## Requires scope

### oauth_2_0

`user-read-playback-position`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`EpisodeObject`](../../doc/models/episode-object.md).

## Example Usage

```python
id = '512ojhOuo1ktJprKbVcKyQ'

market = 'ES'

result = episodes_controller.get_an_episode(
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


# Get-Multiple-Episodes

Get Spotify catalog information for several episodes based on their Spotify IDs.

```python
def get_multiple_episodes(self,
                         ids,
                         market=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `str` | Query, Required | - |
| `market` | `str` | Query, Optional | - |

## Requires scope

### oauth_2_0

`user-read-playback-position`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ManyEpisodes`](../../doc/models/many-episodes.md).

## Example Usage

```python
ids = '77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf'

market = 'ES'

result = episodes_controller.get_multiple_episodes(
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


# Get-Users-Saved-Episodes

Get a list of the episodes saved in the current Spotify user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).

```python
def get_users_saved_episodes(self,
                            market=None,
                            limit=20,
                            offset=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `market` | `str` | Query, Optional | - |
| `limit` | `int` | Query, Optional | - |
| `offset` | `int` | Query, Optional | - |

## Requires scope

### oauth_2_0

`user-library-read`, `user-read-playback-position`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PagingSavedEpisodeObject`](../../doc/models/paging-saved-episode-object.md).

## Example Usage

```python
market = 'ES'

limit = 10

offset = 5

result = episodes_controller.get_users_saved_episodes(
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


# Save-Episodes-User

Save one or more episodes to the current user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).

```python
def save_episodes_user(self,
                      ids,
                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `str` | Query, Required | - |
| `body` | [`MeEpisodesRequest`](../../doc/models/me-episodes-request.md) | Body, Optional | - |

## Requires scope

### oauth_2_0

`user-library-modify`

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
ids = '77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf'

result = episodes_controller.save_episodes_user(ids)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Remove-Episodes-User

Remove one or more episodes from the current user's library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).

```python
def remove_episodes_user(self,
                        ids,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `str` | Query, Required | - |
| `body` | [`MeEpisodesRequest1`](../../doc/models/me-episodes-request-1.md) | Body, Optional | - |

## Requires scope

### oauth_2_0

`user-library-modify`

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
ids = '7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B'

result = episodes_controller.remove_episodes_user(ids)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Check-Users-Saved-Episodes

Check if one or more episodes is already saved in the current Spotify user's 'Your Episodes' library.<br/>
This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer)..

```python
def check_users_saved_episodes(self,
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
ids = '77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf'

result = episodes_controller.check_users_saved_episodes(ids)
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

