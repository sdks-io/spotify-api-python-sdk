
# Public User Object

## Structure

`PublicUserObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_name` | `str` | Optional | The name displayed on the user's profile. `null` if not available. |
| `external_urls` | [`ExternalUrlObject`](../../doc/models/external-url-object.md) | Optional | Known public external URLs for this user. |
| `followers` | [`FollowersObject`](../../doc/models/followers-object.md) | Optional | Information about the followers of this user. |
| `href` | `str` | Optional | A link to the Web API endpoint for this user. |
| `id` | `str` | Optional | The [Spotify user ID](/documentation/web-api/concepts/spotify-uris-ids) for this user. |
| `images` | [`List[ImageObject]`](../../doc/models/image-object.md) | Optional | The user's profile image. |
| `mtype` | [`Type4Enum`](../../doc/models/type-4-enum.md) | Optional | The object type. |
| `uri` | `str` | Optional | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for this user. |

## Example (as JSON)

```json
{
  "display_name": "display_name6",
  "external_urls": {
    "spotify": "spotify6"
  },
  "followers": {
    "href": "href0",
    "total": 82
  },
  "href": "href8",
  "id": "id6"
}
```

