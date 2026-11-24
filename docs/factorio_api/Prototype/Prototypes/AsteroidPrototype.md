---
title: AsteroidPrototype
tags: [factorio-api, prototype]
---
# AsteroidPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `asteroid` · **Requires:** `space_age`

## Properties

### damage_per_hp
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
How much damage should entities and tiles get for each asteroid health point lost due to collision with these objects.

### graphics_set
- **Type:** [[AsteroidGraphicsSet]]
- **Optional**

### emissions_per_second
- **Type:** dictionary<[[AirbornePollutantID]] → [[double (type)]]>
- **Optional**
- **Overrides parent**
Emissions cannot be larger than zero, asteroids cannot produce pollution.
