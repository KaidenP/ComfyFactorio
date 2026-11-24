---
title: RailRemnantsPrototype
tags: [factorio-api, prototype]
---
# RailRemnantsPrototype

> **Parent:** [[CorpsePrototype]] · **Type name:** `rail-remnants`

Used for rail corpses.

## Properties

### pictures
- **Type:** [[RailPictureSet]]
- **Optional**

### related_rail
- **Type:** [[EntityID (type)]]

### secondary_collision_box
- **Type:** [[BoundingBox (type)]]
- **Optional**

### build_grid_size
- **Type:** `2`
- **Optional**
- **Default:** `2`
- **Overrides parent**
Has to be 2 for 2x2 grid.

### collision_box
- **Type:** [[BoundingBox (type)]]
- **Optional**
- **Default:** Empty = `{{0, 0}, {0, 0}}`
- **Overrides parent**
"Rail remnant entities must have a non-zero [[EntityPrototype#collision_box|collision_box]] defined.
