---
title: SolarPanelPrototype
tags: [factorio-api, prototype]
---
# SolarPanelPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `solar-panel`

A [solar panel](https://wiki.factorio.com/Solar_panel).

## Properties

### energy_source
- **Type:** [[ElectricEnergySource]]
Sets how this solar panel connects to the energy network. The most relevant property seems to be the output_priority.

### picture
- **Type:** [[SpriteVariations]]
- **Optional**
The picture displayed for this solar panel.

### production
- **Type:** [[Energy]]
The maximum amount of power this solar panel can produce.

### overlay
- **Type:** [[SpriteVariations]]
- **Optional**
Overlay has to be empty or have same number of variations as `picture`.

### performance_at_day
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### performance_at_night
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`

### solar_coefficient_property
- **Type:** [[SurfacePropertyID (type)]]
- **Optional**
- **Default:** `"solar-power"`
Surface property must have a positive [[SurfacePropertyPrototype#default_value|default value]]. When [[SolarPanelPrototype#solar_coefficient_property|SolarPanelPrototype::solar_coefficient_property]] is set to point at a different surface property than "solar-power", then [[LuaSurface#solar_power_multiplier|LuaSurface::solar_power_multiplier]] and [[SpaceLocationPrototype#solar_power_in_space|SpaceLocationPrototype::solar_power_in_space]] will be ignored as the solar panel power output will be only affected by value of this surface property set on the surface using [[PlanetPrototype#surface_properties|PlanetPrototype::surface_properties]] or [[LuaSurface#set_property|LuaSurface::set_property]].
