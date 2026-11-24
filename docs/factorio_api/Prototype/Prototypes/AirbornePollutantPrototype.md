---
title: AirbornePollutantPrototype
tags: [factorio-api, prototype]
---
# AirbornePollutantPrototype

> **Parent:** [[Prototype]] · **Type name:** `airborne-pollutant`

A type of pollution that can spread throughout the chunks of a map.

## Properties

### localised_name_with_amount
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `"airborne-pollutant-name-with-amount.<name>"`
The translated plural string key to use when displaying this pollution's name with an amount. See [Tutorial:Localisation](https://wiki.factorio.com/Tutorial:Localisation).

### chart_color
- **Type:** [[Color (type)]]

### icon
- **Type:** [[Sprite]]

### affects_evolution
- **Type:** [[boolean (type)]]

### affects_water_tint
- **Type:** [[boolean (type)]]
If true, large amounts of this pollution will cause water tiles to turn a sickly green.

### damages_trees
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If true, trees will occasionally take damage from this pollutant type. When they do, some amount of pollution is removed from the chunk equal to the map's `pollution_restored_per_tree_damage` setting.
