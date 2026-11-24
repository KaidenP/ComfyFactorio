---
title: TileBuildabilityRule
tags: [factorio-api, prototype, type]
---
# TileBuildabilityRule

*Note: `TileBuildabilityRule (type)`.*

Defines restrictions on what tiles an entity can or must be built on.

Note that once the entity has been placed, placing new tiles is not always restricted by these rules for performance reasons. In particular, for most entities these rules are only checked when placing tiles within the collision box of the entity. The exception to this are thrusters and asteroid collectors, for which the rules are always checked.

## Properties

### area
- **Type:** [[SimpleBoundingBox (type)]]

### required_tiles
- **Type:** [[TileCollisionMaskConnector]]
- **Optional**
- **Default:** Any mask

### colliding_tiles
- **Type:** [[TileCollisionMaskConnector]]
- **Optional**
- **Default:** No masks

### remove_on_collision
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
