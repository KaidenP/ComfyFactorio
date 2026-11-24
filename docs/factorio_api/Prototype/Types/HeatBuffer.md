---
title: HeatBuffer
tags: [factorio-api, prototype, type]
---
# HeatBuffer

Used to specify heat capacity properties without a [[HeatEnergySource|heat energy source]].

## Properties

### max_temperature
- **Type:** [[double (type)]]
Must be >= `default_temperature`.

### specific_heat
- **Type:** [[Energy]]

### max_transfer
- **Type:** [[Energy]]

### default_temperature
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `15`

### min_temperature_gradient
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### min_working_temperature
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `15`
Must be >= `default_temperature` and <= `max_temperature`.

### minimum_glow_temperature
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### pipe_covers
- **Type:** [[Sprite4Way]]
- **Optional**

### heat_pipe_covers
- **Type:** [[Sprite4Way]]
- **Optional**

### heat_picture
- **Type:** [[Sprite4Way]]
- **Optional**

### heat_glow
- **Type:** [[Sprite4Way]]
- **Optional**

### connections
- **Type:** array<[[HeatConnectionDefinition (type)]]>
- **Optional**
May contain up to 32 connections.
