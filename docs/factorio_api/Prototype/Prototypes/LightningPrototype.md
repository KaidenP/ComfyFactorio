---
title: LightningPrototype
tags: [factorio-api, prototype]
---
# LightningPrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `lightning` · **Requires:** `space_age`

Lightning randomly hits entities on planets with [[PlanetPrototype#lightning_properties|lightning_properties]].

If a [[LightningAttractorPrototype|lightning attractor]] is hit by lightning it will absorb the lightning hit for energy.

If a something that is not an attractor is hit by lightning it will be damaged by the strike.

## Properties

### graphics_set
- **Type:** [[LightningGraphicsSet]]
- **Optional**

### sound
- **Type:** [[Sound]]
- **Optional**

### attracted_volume_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### strike_effect
- **Type:** [[Trigger]]
- **Optional**
Effect that is triggered when lightning strikes something that is not a lightning attractor. Triggered before `damage` is applied.

### attractor_hit_effect
- **Type:** [[Trigger]]
- **Optional**
Effect that is triggered when lightning hits  a [[LightningAttractorPrototype|lightning attractor]]. Triggered after the attractor is charged by the lightning hit.

### source_offset
- **Type:** [[Vector (type)]]
- **Optional**

### source_variance
- **Type:** [[Vector (type)]]
- **Optional**

### damage
- **Type:** [[DamageParameters (type)]]
- **Optional**
When lightning strikes something that is not a lightning attractor, this damage is applied to the target.

### energy
- **Type:** [[Energy]]
- **Optional**
- **Default:** Max double
When lightning hits a [[LightningAttractorPrototype|lightning attractor]], this amount of energy is transferred to the lightning attractor.

### time_to_damage
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`
Must be less than or equal to `effect_duration`.

### effect_duration
- **Type:** [[uint16 (type)]]
