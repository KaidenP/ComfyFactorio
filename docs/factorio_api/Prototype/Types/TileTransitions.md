---
title: TileTransitions
tags: [factorio-api, prototype, type]
---
# TileTransitions

Used for [[TilePrototype]] graphics.

Use `layout` with `spritesheet` to define all the tile layers inside the `layout` property. The `*_enabled`, `*_layout` and `*_spritesheet` properties can be used to override specific layers of a reused layout.

## Properties

### layout
- **Type:** [[TileTransitionSpritesheetLayout]]
- **Optional**

### spritesheet
- **Type:** [[FileName]]
- **Optional**
Default spritesheet for all TileSpriteLayouts.

### overlay_enabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### mask_enabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### background_enabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### background_mask_enabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### effect_map_enabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### lightmap_enabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### auxiliary_effect_mask_enabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### overlay_layout
- **Type:** [[TileTransitionVariantLayout]]
- **Optional**
Overrides the `overlay` definition inside `layout`.

### mask_layout
- **Type:** [[TileTransitionVariantLayout]]
- **Optional**
Overrides the `mask` definition inside `layout`.

### background_layout
- **Type:** [[TileTransitionVariantLayout]]
- **Optional**
Overrides the `background` definition inside `layout`.

### background_mask_layout
- **Type:** [[TileTransitionVariantLayout]]
- **Optional**
Overrides the `background_mask` definition inside `layout`.

### effect_map_layout
- **Type:** [[TileTransitionVariantLayout]]
- **Optional**
Overrides the `effect_map` definition inside `layout`.

### lightmap_layout
- **Type:** [[TileTransitionVariantLayout]]
- **Optional**
Overrides the `lightmap` definition inside `layout`.

### auxiliary_effect_mask_layout
- **Type:** [[TileTransitionVariantLayout]]
- **Optional**
Overrides the `auxiliary_effect_mask` definition inside `layout`.

### mask_spritesheet
- **Type:** [[FileName]]
- **Optional**
- **Default:** Value of `spritesheet`
Only loaded if `layout` or `mask_layout` is defined.

Default spritesheet for `mask_layout` and `layout.mask`.

### background_spritesheet
- **Type:** [[FileName]]
- **Optional**
- **Default:** Value of `spritesheet`
Only loaded if `layout` or `background_layout` is defined.

Default spritesheet for `background_layout` and `layout.background`.

### background_mask_spritesheet
- **Type:** [[FileName]]
- **Optional**
- **Default:** Value of `spritesheet`
Only loaded if `layout` or `background_mask_layout` is defined.

Default spritesheet for `background_mask_layout` and `layout.background_mask`.

### effect_map_spritesheet
- **Type:** [[FileName]]
- **Optional**
- **Default:** Value of `spritesheet`
Only loaded if `layout` or `effect_map_layout` is defined.

Default spritesheet for `effect_map_layout` and `layout.effect_map`.

### lightmap_spritesheet
- **Type:** [[FileName]]
- **Optional**
- **Default:** Value of `spritesheet`
Only loaded if `layout` or `lightmap_layout` is defined.

Default spritesheet for `lightmap_layout` and `layout.lightmap`.

### auxiliary_effect_mask_spritesheet
- **Type:** [[FileName]]
- **Optional**
- **Default:** Value of `spritesheet`
Only loaded if `layout` or `auxiliary_effect_mask_layout` is defined.

Default spritesheet for `auxiliary_effect_mask_layout` and `layout.auxiliary_effect_mask`.

### water_patch
- **Type:** [[Sprite]]
- **Optional**

### overlay_layer_group
- **Type:** [[TileRenderLayer]]
- **Optional**

### background_layer_group
- **Type:** [[TileRenderLayer]]
- **Optional**

### waving_effect_time_scale
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.15`

### overlay_layer_offset
- **Type:** [[int8 (type)]]
- **Optional**

### masked_overlay_layer_offset
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `0`

### background_layer_offset
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `0`

### masked_background_layer_offset
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** Value of `background_layer_offset`

### draw_background_layer_under_tiles
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### background_layer_occludes_light
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If drawing under water which is supposed to yield water mask, set this to `false` to not mess up the water mask.

### apply_effect_color_to_overlay
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### apply_waving_effect_on_masks
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### apply_waving_effect_on_background_mask
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** Value of `apply_waving_effect_on_masks`

### draw_simple_outer_corner_over_diagonal
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### offset_background_layer_by_tile_layer
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### inner_corner_weights
- **Type:** array<[[float (type)]]>
- **Optional**

### outer_corner_weights
- **Type:** array<[[float (type)]]>
- **Optional**

### side_weights
- **Type:** array<[[float (type)]]>
- **Optional**

### side_variations_in_group
- **Type:** [[uint8 (type)]]
- **Optional**

### double_side_weights
- **Type:** array<[[float (type)]]>
- **Optional**

### double_side_variations_in_group
- **Type:** [[uint8 (type)]]
- **Optional**

### u_transition_weights
- **Type:** array<[[float (type)]]>
- **Optional**
