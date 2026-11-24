---
title: ItemWithEntityDataPrototype
tags: [factorio-api, prototype]
---
# ItemWithEntityDataPrototype

> **Parent:** [[ItemPrototype]] · **Type name:** `item-with-entity-data`

ItemWithEntityData saves data associated with the entity that it represents, for example the content of the equipment grid of a car.

## Properties

### icon_tintable_masks
- **Type:** array<[[IconData]]>
- **Optional**
Can't be an empty array.

Only loaded if `icon_tintable` is defined.

### icon_tintable_mask
- **Type:** [[FileName]]
- **Optional**
Path to the icon file.

Only loaded if `icon_tintable_masks` is not defined and `icon_tintable` is defined.

### icon_tintable_mask_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

Only loaded if `icon_tintable_masks` is not defined and `icon_tintable` is defined.

### icon_tintables
- **Type:** array<[[IconData]]>
- **Optional**
Can't be an empty array.

Only loaded if `icon_tintable` is defined (`icon_tintables` takes precedence over `icon_tintable`).

### icon_tintable
- **Type:** [[FileName]]
- **Optional**
Path to the icon file.

Only loaded if `icon_tintables` is not defined.

### icon_tintable_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

Only loaded if `icon_tintables` is not defined and `icon_tintable` is defined.
