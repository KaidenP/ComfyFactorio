---
title: TransportBeltConnectablePrototype
tags: [factorio-api, prototype]
---
# TransportBeltConnectablePrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Abstract**

Abstract class that anything that is a belt or can connect to belts uses.

## Properties

### belt_animation_set
- **Type:** [[TransportBeltAnimationSet]]
- **Optional**

### speed
- **Type:** [[double (type)]]
The speed of the belt: `speed × 480 = x Items/second`.

The raw value is expressed as the number of tiles traveled by each item on the belt per tick, relative to the belt's maximum density - e.g. `x items/second ÷ (4 items/lane × 2 lanes/belt × 60 ticks/second) = <speed> belts/tick` where a "belt" is the size of one tile. See [Transport_belts/Physics](https://wiki.factorio.com/Transport_belts/Physics) for more details.

Must be a positive non-infinite number. The number is a fixed point number with 8 bits reserved for decimal precision, meaning the smallest value step is `1/2^8 = 0.00390625`. In the simple case of a non-curved belt, the rate is multiples of `1.875` items/s, even though the entity tooltip may show a different rate.

### animation_speed_coefficient
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### collision_box
- **Type:** [[BoundingBox (type)]]
- **Optional**
- **Default:** Empty = `{{0, 0}, {0, 0}}`
- **Overrides parent**
Transport belt connectable entities must have [[EntityPrototype#collision_box|collision_box]] of an appropriate minimal size, they should occupy more than half of every tile the entity covers.
**Examples:**

```
collision_box = {{-0.4, -0.4}, {0.4, 0.4}}
```

### flags
- **Type:** [[EntityPrototypeFlags (type)]]
- **Optional**
- **Overrides parent**
Transport belt connectable entities cannot have the `"building-direction-8-way"` flag.

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `45`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
