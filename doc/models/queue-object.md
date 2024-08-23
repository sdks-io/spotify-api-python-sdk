
# Queue Object

## Structure

`QueueObject`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currently_playing` | `object` | Optional | The currently playing track or episode. Can be `null`. |
| `queue` | `List[object]` | Optional | The tracks or episodes in the queue. Can be empty. |

## Example (as JSON)

```json
{
  "currently_playing": {
    "key1": "val1",
    "key2": "val2"
  },
  "queue": [
    {
      "key1": "val1",
      "key2": "val2"
    },
    {
      "key1": "val1",
      "key2": "val2"
    },
    {
      "key1": "val1",
      "key2": "val2"
    }
  ]
}
```

