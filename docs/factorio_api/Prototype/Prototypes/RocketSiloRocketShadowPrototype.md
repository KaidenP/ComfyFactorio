---
title: RocketSiloRocketShadowPrototype
tags: [factorio-api, prototype]
---
# RocketSiloRocketShadowPrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `rocket-silo-rocket-shadow`

The shadow of the rocket inside the rocket silo.

## Properties

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `19`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.

## Example

```
{
  type = "rocket-silo-rocket-shadow",
  name = "rocket-silo-rocket-shadow",
  flags = {"not-on-map"},
  hidden = true,
  collision_mask = {layers={}, not_colliding_with_itself=true},
  collision_box = {{0, 0}, {10, 3.5}},
  selection_box = {{0, 0}, {0, 0}}
}
```
