
# Explicit Content Settings Object

## Structure

`ExplicitContentSettingsObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filter_enabled` | `bool` | Optional | When `true`, indicates that explicit content should not be played. |
| `filter_locked` | `bool` | Optional | When `true`, indicates that the explicit content setting is locked and can't be changed by the user. |

## Example (as JSON)

```json
{
  "filter_enabled": false,
  "filter_locked": false
}
```

