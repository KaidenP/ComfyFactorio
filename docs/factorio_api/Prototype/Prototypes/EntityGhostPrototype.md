---
title: EntityGhostPrototype
tags: [factorio-api, prototype]
---
# EntityGhostPrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `entity-ghost`

The entity used for ghosts of entities. In-game, the inner entity (the entity this is a ghost of) is rendered with a [[UtilityConstants (prototype)#ghost_tint|UtilityConstants::ghost_tint]].

## Properties

### medium_build_sound
- **Type:** [[Sound]]
- **Optional**

### large_build_sound
- **Type:** [[Sound]]
- **Optional**

### huge_build_sound
- **Type:** [[Sound]]
- **Optional**

### small_build_animated_sound
- **Type:** [[Sound]]
- **Optional**

### medium_build_animated_sound
- **Type:** [[Sound]]
- **Optional**

### large_build_animated_sound
- **Type:** [[Sound]]
- **Optional**

### huge_build_animated_sound
- **Type:** [[Sound]]
- **Optional**

## Example

```
{
  type = "entity-ghost",
  name = "entity-ghost",
  icon = "__core__/graphics/icons/mip/ghost-entity.png",
  icon_size = 64,
  build_sound = { { filename = "__core__/sound/build-ghost-small.ogg",  volume = 0.6 } },
  medium_build_sound = { { filename = "__core__/sound/build-ghost-medium.ogg",  volume = 0.7 } },
  large_build_sound = { { filename = "__core__/sound/build-ghost-large.ogg",  volume = 0.7 } },
  minable = { mining_time = 0, results = {} },
  mined_sound = { { filename = "__core__/sound/deconstruct-ghost.ogg",  volume = 0.4 } }
}
```
