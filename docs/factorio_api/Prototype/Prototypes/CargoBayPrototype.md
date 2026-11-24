---
title: CargoBayPrototype
tags: [factorio-api, prototype]
---
# CargoBayPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `cargo-bay` · **Requires:** `space_age`

## Properties

### graphics_set
- **Type:** [[CargoBayConnectableGraphicsSet]]
- **Optional**

### platform_graphics_set
- **Type:** [[CargoBayConnectableGraphicsSet]]
- **Optional**
A special variant which renders on space platforms. If not specified, the game will fall back to the regular graphics set.

### inventory_size_bonus
- **Type:** [[ItemStackIndex (type)]]
Cannot be 0.

### has_direction
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### allow_unloading
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When set to `true`, inserters will be able to take items out of this cargo bay when it is connected to a cargo landing pad.

### use_unloading_distance_limit
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Only relevant for cargo bays that have [[CargoBayPrototype#allow_unloading|allow_unloading]] set.

When `false` this cargo bay will allow item unloading regardless of distance as long as it is connected to a cargo landing pad.

When `true` this cargo bay will allow item unloading only when connected to a cargo landing pad and cargo bay is within distance limit set by [[MaxCargoBayUnloadingDistanceModifier]] from that cargo landing pad.

### hatch_definitions
- **Type:** array<[[CargoHatchDefinition (type)]]>
- **Optional**

### build_grid_size
- **Type:** `2`
- **Optional**
- **Default:** `2`
- **Overrides parent**
Has to be 2 for 2x2 grid.
