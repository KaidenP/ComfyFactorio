---
title: DecorativePrototype
tags: [factorio-api, prototype]
---
# DecorativePrototype

> **Parent:** [[Prototype]] · **Type name:** `optimized-decorative` · **Instance limit:** 65535

Simple decorative purpose objects on the map, they have no health and some of them are removed when the player builds over. Usually used for grass patches, roots, small plants etc.

## Properties

### pictures
- **Type:** [[SpriteVariations]]
Must contain at least 1 picture.

### stateless_visualisation
- **Type:** [[StatelessVisualisation]] | array<[[StatelessVisualisation]]>
- **Optional**
Can be defined only when decorative is not "decal" (see `render_layer`).

### stateless_visualisation_variations
- **Type:** array<[[StatelessVisualisation]] | array<[[StatelessVisualisation]]>>
- **Optional**
Only loaded if `stateless_visualisation` is not defined. Can be defined only when decorative is not "decal" (see `render_layer`).

### collision_box
- **Type:** [[BoundingBox (type)]]
- **Optional**
Must contain the [0,0] point. Max radius of the collision box is 8.

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"decorative"`
When "decals" render layer is used, the decorative is treated as decal. That means it will be rendered within tile layers instead of normal sprite layers.

### grows_through_rail_path
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### opacity_over_water
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
- **Requires:** `space_age`
Loaded only if `render_layer` = "decals". Value lower than 1 enables masking by water for decals with `tile_layer` greater or equal to [[UtilityConstants (prototype)#capture_water_mask_at_layer|UtilityConstants::capture_water_mask_at_layer]]. Water tiles must use water `tile-effect` with [[WaterTileEffectParameters#lightmap_alpha|WaterTileEffectParameters::lightmap_alpha]] set to 0 or value less than 1. Graphics option `Occlude light sprites` must be enabled, as water mask is captured into terrain lightmap alpha channel. Tiles rendered in layer between [[UtilityConstants (prototype)#capture_water_mask_at_layer|UtilityConstants::capture_water_mask_at_layer]] and decal's `tile_layer` will likely also mask decals in some way, as water mask will likely be 0 at their position, but this is considered undefined behavior.

### tile_layer
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** `0`
Mandatory if `render_layer` = "decals". This int16 is converted to a [[TileRenderLayer]] internally. It is offset from `ground-natural`.

### decal_overdraw_priority
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`
Loaded only if `render_layer` = "decals". When decoratives are being spawned by [[EnemySpawnerPrototype#spawn_decoration|EnemySpawnerPrototype::spawn_decoration]] or [[TurretPrototype#spawn_decoration|TurretPrototype::spawn_decoration]], decals with `decal_overdraw_priority` greater than 0 will be filtered such that they don't overlap too much. If two or more decals would overlap, only the one with the largest value of `decal_overdraw_priority` is placed.

### collision_mask
- **Type:** [[CollisionMaskConnector]]
- **Optional**
Defaults to the mask from [[UtilityConstants (prototype)#default_collision_masks|UtilityConstants::default_collision_masks]] when indexed by `"decorative"`.

### walking_sound
- **Type:** [[Sound]]
- **Optional**

### trigger_effect
- **Type:** [[TriggerEffect]]
- **Optional**
Called by [[DestroyDecorativesTriggerEffectItem]].

### minimal_separation
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.0`

### target_count
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`

### placed_effect
- **Type:** [[TriggerEffect]]
- **Optional**

### autoplace
- **Type:** [[AutoplaceSpecification (type)]]
- **Optional**
