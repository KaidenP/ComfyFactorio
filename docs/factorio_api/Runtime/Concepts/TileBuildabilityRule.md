---
title: TileBuildabilityRule
tags: [factorio-api, runtime, concept]
---
# TileBuildabilityRule

A runtime representation of [[TileBuildabilityRule (type)|TileBuildabilityRule]].

## Fields

### area
- **Type:** [[BoundingBox]]
The area that this rule applies to.

### colliding_tiles
- **Type:** [[CollisionMask]]
The tiles that this rule collides with.

### required_tiles
- **Type:** [[CollisionMask]]
The tiles that this rule requires to be present.

### remove_on_collision
- **Type:** [[boolean]]
If the entity should be removed upon collision.
