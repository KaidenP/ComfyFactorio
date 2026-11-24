---
title: MouseCursor
tags: [factorio-api, prototype]
---
# MouseCursor

> **Type name:** `mouse-cursor`

Used by [[SelectionToolPrototype#mouse_cursor|SelectionToolPrototype::mouse_cursor]].

## Properties

### type
- **Type:** `"mouse-cursor"`

### name
- **Type:** [[string (type)]]
Name of the prototype.

### system_cursor
- **Type:** `"arrow"` | `"i-beam"` | `"crosshair"` | `"wait-arrow"` | `"size-all"` | `"no"` | `"hand"`
- **Optional**
Either this or the other three properties have to be present.

### filename
- **Type:** [[FileName]]
- **Optional**
Mandatory if `system_cursor` is not defined.

### hot_pixel_x
- **Type:** [[int16 (type)]]
- **Optional**
Mandatory if `system_cursor` is not defined.

### hot_pixel_y
- **Type:** [[int16 (type)]]
- **Optional**
Mandatory if `system_cursor` is not defined.

## Example

```
{
  type = "mouse-cursor",
  name = "selection-tool-cursor",
  filename = "__core__/graphics/cross-select-x32.png",
  hot_pixel_x = 16,
  hot_pixel_y = 16
}
```

```
{
  type = "mouse-cursor",
  name = "system-crosshair",
  system_cursor = "crosshair"
}
```
