
# Context Object

## Structure

`ContextObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | The object type, e.g. "artist", "playlist", "album", "show". |
| `href` | `str` | Optional | A link to the Web API endpoint providing full details of the track. |
| `external_urls` | [`ExternalUrlObject`](../../doc/models/external-url-object.md) | Optional | External URLs for this context. |
| `uri` | `str` | Optional | The [Spotify URI](/documentation/web-api/concepts/spotify-uris-ids) for the context. |

## Example (as JSON)

```json
{
  "type": "type6",
  "href": "href6",
  "external_urls": {
    "spotify": "spotify6"
  },
  "uri": "uri8"
}
```

