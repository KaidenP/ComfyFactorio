---
title: LightningAttractorPrototype
tags: [factorio-api, prototype]
---
# LightningAttractorPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `lightning-attractor` · **Requires:** `space_age`

Absorbs [[LightningPrototype|lightning]] and optionally converts it into electricity.

## Properties

### chargable_graphics
- **Type:** [[ChargableGraphics]]
- **Optional**

### lightning_strike_offset
- **Type:** [[MapPosition (type)]]
- **Optional**

### efficiency
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
Cannot be less than 0.

### range_elongation
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`

### energy_source
- **Type:** [[ElectricEnergySource]]
- **Optional**
Mandatory if `efficiency` is larger than 0. May not be defined if `efficiency` is 0.
