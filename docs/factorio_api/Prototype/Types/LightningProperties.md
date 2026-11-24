---
title: LightningProperties
tags: [factorio-api, prototype, type]
---
# LightningProperties

## Properties

### lightnings_per_chunk_per_tick
- **Type:** [[double (type)]]

### search_radius
- **Type:** [[double (type)]]

### lightning_types
- **Type:** array<[[EntityID (type)]]>
Cannot be an empty array. Names of [[LightningPrototype|lightning entities]].

### priority_rules
- **Type:** array<[[LightningPriorityRule]]>
- **Optional**

### exemption_rules
- **Type:** array<[[LightningRuleBase]]>
- **Optional**

### lightning_multiplier_at_day
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
Must be in range `[0, 1]`.

### lightning_multiplier_at_night
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Must be in range `[0, 1]`.

### multiplier_surface_property
- **Type:** [[SurfacePropertyID (type)]]
- **Optional**
When set, value of that surface property will be used as an additional multiplier to the lightning frequency.

Value of that surface property is divided by [[SurfacePropertyPrototype#default_value|default_value]] which means a default value must be positive (cannot be 0). When surface property has value at default, then this additional multiplier has value of 1.

### lightning_warning_icon
- **Type:** [[Sprite]]
- **Optional**
Icon to render on top of entities that are endangered by lightning. When not provided, a [[UtilitySprites#lightning_warning_icon|UtilitySprites::lightning_warning_icon]] will be used instead.
