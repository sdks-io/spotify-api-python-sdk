# Markets

```python
markets_controller = client.markets
```

## Class Name

`MarketsController`


# Get-Available-Markets

Get the list of markets where Spotify is available.

```python
def get_available_markets(self)
```

## Response Type

This method returns a `ApiResponse` instance. The `body` property of this instance returns the response data which is of type [`Markets`](../../doc/models/markets.md).

## Example Usage

```python
result = markets_controller.get_available_markets()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Bad or expired token. This can happen if the user revoked a token or<br>the access token has expired. You should re-authenticate the user. | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 403 | Bad OAuth request (wrong consumer key, bad nonce, expired<br>timestamp...). Unfortunately, re-authenticating the user won't help here. | [`ForbiddenException`](../../doc/models/forbidden-exception.md) |
| 429 | The app has exceeded its rate limits. | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |

