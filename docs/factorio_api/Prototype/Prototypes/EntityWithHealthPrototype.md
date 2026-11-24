---
title: EntityWithHealthPrototype
tags: [factorio-api, prototype]
---
# EntityWithHealthPrototype

> **Parent:** [[EntityPrototype]] · **Abstract**

Abstract base of all entities with health in the game.

## Properties

### max_health
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `10`
The unit health can never go over the maximum. Default health of units on creation is set to max. Must be greater than 0.
**Examples:**

```
max_health = 50
```

### healing_per_tick
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
The amount of health automatically regenerated per tick. If the value is in range [-0.0166, 0.0166], then healing is considered slow and will apply 60 * healing_per_tick once every second.
**Examples:**

```
healing_per_tick = 0.01
```

### repair_speed_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Multiplier of [[RepairToolPrototype#speed|RepairToolPrototype::speed]] for this entity prototype.

### dying_explosion
- **Type:** [[ExplosionDefinition (type)]] | array<[[ExplosionDefinition (type)]]>
- **Optional**
The entities that are spawned in place of this one when it dies.

### dying_trigger_effect
- **Type:** [[TriggerEffect]]
- **Optional**

### damaged_trigger_effect
- **Type:** [[TriggerEffect]]
- **Optional**

### loot
- **Type:** array<[[ItemProductPrototype]]>
- **Optional**
The loot is dropped on the ground when the entity is killed.
**Examples:**

```
loot =
{
  {
    type = "item",
    name = "stone",
    amount_min = 2,
    amount_max = 10,
    independent_probability = 1
  }
}
```

### resistances
- **Type:** array<[[Resistance (type)]]>
- **Optional**
See [damage](https://wiki.factorio.com/Damage).
**Examples:**

```
resistances =
{
  {
    type = "fire",
    percent = 80
  },
  {
    type = "explosion",
    percent = 30
  }
}
```

### attack_reaction
- **Type:** [[AttackReactionItem (type)]] | array<[[AttackReactionItem (type)]]>
- **Optional**
- **Default:** Empty

### repair_sound
- **Type:** [[Sound]]
- **Optional**
- **Default:** Utility sound defaultManualRepair
Played when this entity is repaired with a [[RepairToolPrototype]].

### alert_when_damaged
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### hide_resistances
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the resistances of this entity should be hidden in the entity tooltip.

### create_ghost_on_death
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### random_corpse_variation
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### integration_patch_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"lower-object"`
May also be defined inside `graphics_set` instead of directly in the entity prototype. This is useful for entities that use a `graphics_set` property to define their graphics, because then all graphics can be defined in one place.

### corpse
- **Type:** [[EntityID (type)]] | array<[[EntityID (type)]]>
- **Optional**
- **Default:** Empty
Specifies the names of the [[CorpsePrototype]] to be used when this entity dies.

### integration_patch
- **Type:** [[Sprite4Way]]
- **Optional**
May also be defined inside `graphics_set` instead of directly in the entity prototype. This is useful for entities that use a `graphics_set` property to define their graphics, because then all graphics can be defined in one place.

Sprite drawn on ground under the entity to make it feel more integrated into the ground.

### overkill_fraction
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.05`
Fraction of health by which predicted damage must be exceeded before entity is considered as "predicted to die" causing turrets (and others) to stop shooting more projectiles. If entity is healing it is better to keep larger margin to avoid cases where not enough projectiles goes towards a target and it heals causing it to survive all the incoming projectiles. If entity does not heal, margin may be reduced. Must be >= 0.

## Example

```
{
  type = "container",
  name = "wooden-chest",
  icon = "__base__/graphics/icons/wooden-chest.png",
  flags = { "placeable-neutral", "player-creation" },
  minable = { mining_time = 1, result = "wooden-chest" },
  max_health = 100,
  corpse = "small-remnants",
  collision_box = { {-0.35, -0.35}, {0.35, 0.35} },
  fast_replaceable_group = "container",
  selection_box = { {-0.5, -0.5}, {0.5, 0.5} },
  inventory_size = 16,
  open_sound = { filename = "__base__/sound/wooden-chest-open.ogg" },
  close_sound = { filename = "__base__/sound/wooden-chest-close.ogg" },
  picture =
  {
    filename = "__base__/graphics/entity/wooden-chest/wooden-chest.png",
    priority = "extra-high",
    width = 46,
    height = 33,
    shift = {0.25, 0.015625}
  }
}
```
