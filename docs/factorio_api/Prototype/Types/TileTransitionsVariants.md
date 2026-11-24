---
title: TileTransitionsVariants
tags: [factorio-api, prototype, type]
---
# TileTransitionsVariants

## Properties

### main
- **Type:** array<[[TileMainPictures]]>
- **Optional**

### material_texture_width_in_tiles
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `8`

### material_texture_height_in_tiles
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `8`

### material_background
- **Type:** [[MaterialTextureParameters]]
- **Optional**

### light
- **Type:** array<[[TileLightPictures]]>
- **Optional**

### material_light
- **Type:** [[MaterialTextureParameters]]
- **Optional**
Must have the same `count` as material_background.

### empty_transitions
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### transition
- **Type:** [[TileTransitions]]
- **Optional**
Only loaded, and mandatory if `empty_transitions` is `false`.
