---
title: PlantPrototype
tags: [factorio-api, prototype]
---
# PlantPrototype

> **Parent:** [[TreePrototype]] · **Type name:** `plant` · **Requires:** `space_age`

## Properties

### growth_ticks
- **Type:** [[MapTick (type)]]
Must be positive.

### harvest_emissions
- **Type:** dictionary<[[AirbornePollutantID]] → [[double (type)]]>
- **Optional**
The burst of pollution to emit when the plant is harvested.

### agricultural_tower_tint
- **Type:** [[RecipeTints]]
- **Optional**

### growth_variations
- **Type:** array<[[TreeGrowth]]>
- **Optional**
If defined, it can't be empty.

### growth_mounds
- **Type:** array<[[Sprite]]>
- **Optional**
Mound sprite drawn under growing trees which fades close to full growth. If defined, it can't be empty.
