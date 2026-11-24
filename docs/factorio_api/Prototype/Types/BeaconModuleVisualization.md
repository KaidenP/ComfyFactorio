---
title: BeaconModuleVisualization
tags: [factorio-api, prototype, type]
---
# BeaconModuleVisualization

## Properties

### has_empty_slot
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### secondary_draw_order
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `0`
Used to determine render order for sprites with the same `render_layer` in the same position. Sprites with a higher `secondary_draw_order` are drawn on top.

### apply_module_tint
- **Type:** [[ModuleTint]]
- **Optional**
- **Default:** `"none"`
Which tint set in [[ModulePrototype#beacon_tint|ModulePrototype::beacon_tint]] should be applied to this, if any.

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### pictures
- **Type:** [[SpriteVariations]]
- **Optional**
