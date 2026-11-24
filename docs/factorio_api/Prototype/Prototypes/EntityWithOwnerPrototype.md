---
title: EntityWithOwnerPrototype
tags: [factorio-api, prototype]
---
# EntityWithOwnerPrototype

> **Parent:** [[EntityWithHealthPrototype]] · **Abstract**

Abstract base of all entities with a force in the game. These entities have a [[LuaEntity#unit_number|LuaEntity::unit_number]] during runtime. Can be high priority [military targets](https://wiki.factorio.com/Military_units_and_structures).

## Properties

### is_military_target
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether this prototype should be a high priority target for enemy forces. See [Military units and structures](https://wiki.factorio.com/Military_units_and_structures).

### allow_run_time_change_of_is_military_target
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this is true, this entity's `is_military_target` property can be changed during runtime (on the entity, not on the prototype itself).

### quality_indicator_shift
- **Type:** [[Vector (type)]]
- **Optional**
The shift from the bottom left corner of the selection box.

### quality_indicator_scale
- **Type:** [[double (type)]]
- **Optional**
- **Default:** Calculated based on entity tile_width and height
The default scale is based on the tile distance of the shorter dimension. Where size 3 results into scale 1. The default minimum is 0.5 and maximum 1.0.
