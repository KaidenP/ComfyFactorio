---
title: PlanetPrototype
tags: [factorio-api, prototype]
---
# PlanetPrototype

> **Parent:** [[SpaceLocationPrototype]] · **Type name:** `planet`

## Properties

### map_seed_offset
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** CRC checksum of `name`

### entities_require_heating
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Requires:** `space_age`

### pollutant_type
- **Type:** [[AirbornePollutantID]]
- **Optional**

### persistent_ambient_sounds
- **Type:** [[PersistentWorldAmbientSoundsDefinition]]
- **Optional**

### surface_render_parameters
- **Type:** [[SurfaceRenderParameters (type)]]
- **Optional**

### player_effects
- **Type:** [[Trigger]]
- **Optional**

### ticks_between_player_effects
- **Type:** [[MapTick (type)]]
- **Optional**
- **Default:** `0`

### map_gen_settings
- **Type:** [[PlanetPrototypeMapGenSettings]]
- **Optional**

### surface_properties
- **Type:** dictionary<[[SurfacePropertyID (type)]] → [[double (type)]]>
- **Optional**

### lightning_properties
- **Type:** [[LightningProperties]]
- **Optional**
