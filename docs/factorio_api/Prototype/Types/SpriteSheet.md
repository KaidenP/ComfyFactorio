---
title: SpriteSheet
tags: [factorio-api, prototype, type]
---
# SpriteSheet

> **Parent:** [[SpriteParameters]]

## Properties

### layers
- **Type:** array<[[SpriteSheet]]>
- **Optional**
If this property is present, all SpriteSheet definitions have to be placed as entries in the array, and they will all be loaded from there. `layers` may not be an empty table. Each definition in the array may also have the `layers` property.

If this property is present, all other properties, including those inherited from SpriteParameters, are ignored.

### variation_count
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`

### repeat_count
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`

### line_length
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** Value of `variation_count`

### filenames
- **Type:** array<[[FileName]]>
- **Optional**

### lines_per_file
- **Type:** [[uint32 (type)]]
- **Optional**
Mandatory if `filenames` is defined.

### dice
- **Type:** [[SpriteSizeType]]
- **Optional**
Number of slices this is sliced into when using the "optimized atlas packing" option. If you are a modder, you can just ignore this property. Example: If this is 4, the sprite will be sliced into a 4x4 grid.

### dice_x
- **Type:** [[SpriteSizeType]]
- **Optional**
Same as `dice` above, but this specifies only how many slices there are on the x axis.

### dice_y
- **Type:** [[SpriteSizeType]]
- **Optional**
Same as `dice` above, but this specifies only how many slices there are on the y axis.

### filename
- **Type:** [[FileName]]
- **Optional**
- **Overrides parent**
Only loaded, and mandatory if `layers` and `filenames` are not defined.

The path to the sprite file to use.
