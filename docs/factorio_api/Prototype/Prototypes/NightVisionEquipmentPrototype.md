---
title: NightVisionEquipmentPrototype
tags: [factorio-api, prototype]
---
# NightVisionEquipmentPrototype

> **Parent:** [[EquipmentPrototype]] · **Type name:** `night-vision-equipment`

Used by [nightvision](https://wiki.factorio.com/Nightvision).

## Properties

### energy_input
- **Type:** [[Energy]]

### color_lookup
- **Type:** [[DaytimeColorLookupTable (type)]]

### darkness_to_turn_on
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.5`
Must be >= 0 and <= 1. By default, this equipment turns on when `surface_darkness >= darkness_to_turn_on`.

### sunglasses
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, this equipment turns on when `surface_darkness <= darkness_to_turn_on`.

### activate_sound
- **Type:** [[Sound]]
- **Optional**

### deactivate_sound
- **Type:** [[Sound]]
- **Optional**
