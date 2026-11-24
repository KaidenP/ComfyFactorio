---
title: TileSearchFilters
tags: [factorio-api, runtime, concept]
---
# TileSearchFilters

## Fields

### area
- **Type:** [[BoundingBox]]
- **Optional**

### position
- **Type:** [[MapPosition]]
- **Optional**
Ignored if not given with radius.

### radius
- **Type:** [[double]]
- **Optional**
If given with position, will return all tiles within the radius of the position.

### name
- **Type:** [[TileID]] | array<[[TileID]]>
- **Optional**
An empty array means nothing matches the name filter.

### limit
- **Type:** [[uint32]]
- **Optional**

### has_hidden_tile
- **Type:** [[boolean]]
- **Optional**

### has_double_hidden_tile
- **Type:** [[boolean]]
- **Optional**
Can be further filtered by supplying a `force` filter.

### has_tile_ghost
- **Type:** [[boolean]]
- **Optional**
Can be further filtered by supplying a `force` filter.

### to_be_deconstructed
- **Type:** [[boolean]]
- **Optional**
Can be further filtered by supplying a `force` filter.

### collision_mask
- **Type:** [[CollisionLayerID]] | array<[[CollisionLayerID]]> | dictionary<[[CollisionLayerID]] → `true`>
- **Optional**

### force
- **Type:** [[ForceSet]]
- **Optional**

### invert
- **Type:** [[boolean]]
- **Optional**
If the filters should be inverted.
