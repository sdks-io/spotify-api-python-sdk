
# Paging Playlist Track Object

## Structure

`PagingPlaylistTrackObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `href` | `str` | Required | A link to the Web API endpoint returning the full result of the request |
| `limit` | `int` | Required | The maximum number of items in the response (as set in the query or by default). |
| `next` | `str` | Required | URL to the next page of items. ( `null` if none) |
| `offset` | `int` | Required | The offset of the items returned (as set in the query or by default) |
| `previous` | `str` | Required | URL to the previous page of items. ( `null` if none) |
| `total` | `int` | Required | The total number of items available to return. |
| `items` | [`List[PlaylistTrackObject]`](../../doc/models/playlist-track-object.md) | Required | - |

## Example (as JSON)

```json
{
  "href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20\n",
  "limit": 20,
  "next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
  "offset": 0,
  "previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
  "total": 4,
  "items": [
    {
      "added_at": "2016-03-13T12:52:32.123Z",
      "added_by": {
        "external_urls": {
          "spotify": "spotify6"
        },
        "followers": {
          "href": "href0",
          "total": 82
        },
        "href": "href6",
        "id": "id4",
        "type": "user"
      },
      "is_local": false,
      "track": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ]
}
```

