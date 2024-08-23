# Genres

```python
genres_controller = client.genres
```

## Class Name

`GenresController`


# Get-Recommendation-Genres

Retrieve a list of available genres seed parameter values for [recommendations](/documentation/web-api/reference/get-recommendations).

```python
def get_recommendation_genres(self)
```

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`ManyGenres`](../../doc/models/many-genres.md).

## Example Usage

```python
result = genres_controller.get_recommendation_genres()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |

