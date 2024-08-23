# Tracks

```python
tracks_controller = client.tracks
```

## Class Name

`TracksController`

## Methods

* [Get-Track](../../doc/controllers/tracks.md#get-track)
* [Get-Several-Tracks](../../doc/controllers/tracks.md#get-several-tracks)
* [Get-Users-Saved-Tracks](../../doc/controllers/tracks.md#get-users-saved-tracks)
* [Save-Tracks-User](../../doc/controllers/tracks.md#save-tracks-user)
* [Remove-Tracks-User](../../doc/controllers/tracks.md#remove-tracks-user)
* [Check-Users-Saved-Tracks](../../doc/controllers/tracks.md#check-users-saved-tracks)
* [Get-Several-Audio-Features](../../doc/controllers/tracks.md#get-several-audio-features)
* [Get-Audio-Features](../../doc/controllers/tracks.md#get-audio-features)
* [Get-Audio-Analysis](../../doc/controllers/tracks.md#get-audio-analysis)
* [Get-Recommendations](../../doc/controllers/tracks.md#get-recommendations)


# Get-Track

Get Spotify catalog information for a single track identified by its
unique Spotify ID.

```python
def get_track(self,
             id,
             market=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |
| `market` | `str` | Query, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`TrackObject`](../../doc/models/track-object.md).

## Example Usage

```python
id = '11dFghVXANMlKmJXsNCbNl'

market = 'ES'

result = tracks_controller.get_track(
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


# Get-Several-Tracks

Get Spotify catalog information for multiple tracks based on their Spotify IDs.

```python
def get_several_tracks(self,
                      ids,
                      market=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `str` | Query, Required | - |
| `market` | `str` | Query, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ManyTracks`](../../doc/models/many-tracks.md).

## Example Usage

```python
ids = '7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B'

market = 'ES'

result = tracks_controller.get_several_tracks(
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


# Get-Users-Saved-Tracks

Get a list of the songs saved in the current Spotify user's 'Your Music' library.

```python
def get_users_saved_tracks(self,
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

`user-library-read`

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`PagingSavedTrackObject`](../../doc/models/paging-saved-track-object.md).

## Example Usage

```python
market = 'ES'

limit = 10

offset = 5

result = tracks_controller.get_users_saved_tracks(
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


# Save-Tracks-User

Save one or more tracks to the current user's 'Your Music' library.

```python
def save_tracks_user(self,
                    ids,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `str` | Query, Required | - |
| `body` | [`MeTracksRequest`](../../doc/models/me-tracks-request.md) | Body, Optional | - |

## Requires scope

### oauth_2_0

`user-library-modify`

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
ids = '7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B'

result = tracks_controller.save_tracks_user(ids)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Remove-Tracks-User

Remove one or more tracks from the current user's 'Your Music' library.

```python
def remove_tracks_user(self,
                      ids,
                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `str` | Query, Required | - |
| `body` | [`MeTracksRequest1`](../../doc/models/me-tracks-request-1.md) | Body, Optional | - |

## Requires scope

### oauth_2_0

`user-library-modify`

## Response Type

This method returns a `ApiResponse` instance.

## Example Usage

```python
ids = '7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B'

result = tracks_controller.remove_tracks_user(ids)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Check-Users-Saved-Tracks

Check if one or more tracks is already saved in the current Spotify user's 'Your Music' library.

```python
def check_users_saved_tracks(self,
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
ids = '7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B'

result = tracks_controller.check_users_saved_tracks(ids)
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


# Get-Several-Audio-Features

Get audio features for multiple tracks based on their Spotify IDs.

```python
def get_several_audio_features(self,
                              ids)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `str` | Query, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ManyAudioFeatures`](../../doc/models/many-audio-features.md).

## Example Usage

```python
ids = '7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B'

result = tracks_controller.get_several_audio_features(ids)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Get-Audio-Features

Get audio feature information for a single track identified by its unique
Spotify ID.

```python
def get_audio_features(self,
                      id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AudioFeaturesObject`](../../doc/models/audio-features-object.md).

## Example Usage

```python
id = '11dFghVXANMlKmJXsNCbNl'

result = tracks_controller.get_audio_features(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Get-Audio-Analysis

Get a low-level audio analysis for a track in the Spotify catalog. The audio analysis describes the track’s structure and musical content, including rhythm, pitch, and timbre.

```python
def get_audio_analysis(self,
                      id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`AudioAnalysisObject`](../../doc/models/audio-analysis-object.md).

## Example Usage

```python
id = '11dFghVXANMlKmJXsNCbNl'

result = tracks_controller.get_audio_analysis(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |


# Get-Recommendations

Recommendations are generated based on the available information for a given seed entity and matched against similar artists and tracks. If there is sufficient information about the provided seeds, a list of tracks will be returned together with pool size details.

For artists and tracks that are very new or obscure there might not be enough data to generate a list of tracks.

```python
def get_recommendations(self,
                       limit=20,
                       market=None,
                       seed_artists=None,
                       seed_genres=None,
                       seed_tracks=None,
                       min_acousticness=None,
                       max_acousticness=None,
                       target_acousticness=None,
                       min_danceability=None,
                       max_danceability=None,
                       target_danceability=None,
                       min_duration_ms=None,
                       max_duration_ms=None,
                       target_duration_ms=None,
                       min_energy=None,
                       max_energy=None,
                       target_energy=None,
                       min_instrumentalness=None,
                       max_instrumentalness=None,
                       target_instrumentalness=None,
                       min_key=None,
                       max_key=None,
                       target_key=None,
                       min_liveness=None,
                       max_liveness=None,
                       target_liveness=None,
                       min_loudness=None,
                       max_loudness=None,
                       target_loudness=None,
                       min_mode=None,
                       max_mode=None,
                       target_mode=None,
                       min_popularity=None,
                       max_popularity=None,
                       target_popularity=None,
                       min_speechiness=None,
                       max_speechiness=None,
                       target_speechiness=None,
                       min_tempo=None,
                       max_tempo=None,
                       target_tempo=None,
                       min_time_signature=None,
                       max_time_signature=None,
                       target_time_signature=None,
                       min_valence=None,
                       max_valence=None,
                       target_valence=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `limit` | `int` | Query, Optional | - |
| `market` | `str` | Query, Optional | - |
| `seed_artists` | `str` | Query, Optional | - |
| `seed_genres` | `str` | Query, Optional | - |
| `seed_tracks` | `str` | Query, Optional | - |
| `min_acousticness` | `float` | Query, Optional | - |
| `max_acousticness` | `float` | Query, Optional | - |
| `target_acousticness` | `float` | Query, Optional | - |
| `min_danceability` | `float` | Query, Optional | - |
| `max_danceability` | `float` | Query, Optional | - |
| `target_danceability` | `float` | Query, Optional | - |
| `min_duration_ms` | `int` | Query, Optional | - |
| `max_duration_ms` | `int` | Query, Optional | - |
| `target_duration_ms` | `int` | Query, Optional | - |
| `min_energy` | `float` | Query, Optional | - |
| `max_energy` | `float` | Query, Optional | - |
| `target_energy` | `float` | Query, Optional | - |
| `min_instrumentalness` | `float` | Query, Optional | - |
| `max_instrumentalness` | `float` | Query, Optional | - |
| `target_instrumentalness` | `float` | Query, Optional | - |
| `min_key` | `int` | Query, Optional | - |
| `max_key` | `int` | Query, Optional | - |
| `target_key` | `int` | Query, Optional | - |
| `min_liveness` | `float` | Query, Optional | - |
| `max_liveness` | `float` | Query, Optional | - |
| `target_liveness` | `float` | Query, Optional | - |
| `min_loudness` | `float` | Query, Optional | - |
| `max_loudness` | `float` | Query, Optional | - |
| `target_loudness` | `float` | Query, Optional | - |
| `min_mode` | `int` | Query, Optional | - |
| `max_mode` | `int` | Query, Optional | - |
| `target_mode` | `int` | Query, Optional | - |
| `min_popularity` | `int` | Query, Optional | - |
| `max_popularity` | `int` | Query, Optional | - |
| `target_popularity` | `int` | Query, Optional | - |
| `min_speechiness` | `float` | Query, Optional | - |
| `max_speechiness` | `float` | Query, Optional | - |
| `target_speechiness` | `float` | Query, Optional | - |
| `min_tempo` | `float` | Query, Optional | - |
| `max_tempo` | `float` | Query, Optional | - |
| `target_tempo` | `float` | Query, Optional | - |
| `min_time_signature` | `int` | Query, Optional | - |
| `max_time_signature` | `int` | Query, Optional | - |
| `target_time_signature` | `int` | Query, Optional | - |
| `min_valence` | `float` | Query, Optional | - |
| `max_valence` | `float` | Query, Optional | - |
| `target_valence` | `float` | Query, Optional | - |

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`RecommendationsObject`](../../doc/models/recommendations-object.md).

## Example Usage

```python
limit = 10

market = 'ES'

seed_artists = '4NHQUGzhtTLFvgF5SZesLK'

seed_genres = 'classical,country'

seed_tracks = '0c6xIDDpzE81m2q797ordA'

result = tracks_controller.get_recommendations(
    limit=limit,
    market=market,
    seed_artists=seed_artists,
    seed_genres=seed_genres,
    seed_tracks=seed_tracks
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |

