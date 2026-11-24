---
title: BoxSpecification
tags: [factorio-api, prototype, type]
---
# BoxSpecification

A cursor box, for use in [[UtilitySprites]].

## Properties

### sprite
- **Type:** [[Sprite]]

### is_whole_box
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether this is a complete box or just the top left corner. If this is true, `side_length` and `side_height` must be present. Otherwise `max_side_length` must be present.

### side_length
- **Type:** [[double (type)]]
- **Optional**
Only loaded, and mandatory if `is_whole_box` is `true`.

### side_height
- **Type:** [[double (type)]]
- **Optional**
Only loaded, and mandatory if `is_whole_box` is `true`.

### max_side_length
- **Type:** [[double (type)]]
- **Optional**
Only loaded, and mandatory if `is_whole_box` is `false`.
