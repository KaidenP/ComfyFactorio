---
title: LocomotivePrototype
tags: [factorio-api, prototype]
---
# LocomotivePrototype

> **Parent:** [[RollingStockPrototype]] · **Type name:** `locomotive`

A [locomotive](https://wiki.factorio.com/Locomotive).

## Properties

### max_power
- **Type:** [[Energy]]

### reversing_power_modifier
- **Type:** [[double (type)]]

### energy_source
- **Type:** [[BurnerEnergySource]] | [[VoidEnergySource]]

### front_light
- **Type:** [[LightDefinition]]
- **Optional**

### front_light_pictures
- **Type:** [[RollingStockRotatedSlopedGraphics]]
- **Optional**

### darkness_to_render_light_animation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.3`

### max_snap_to_train_stop_distance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `3.0`
In tiles. A locomotive will snap to a nearby train stop when the player places it within this distance to the stop.
