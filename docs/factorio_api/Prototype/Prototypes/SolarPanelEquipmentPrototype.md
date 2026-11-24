---
title: SolarPanelEquipmentPrototype
tags: [factorio-api, prototype]
---
# SolarPanelEquipmentPrototype

> **Parent:** [[EquipmentPrototype]] · **Type name:** `solar-panel-equipment`

A [portable solar panel](https://wiki.factorio.com/Portable_solar_panel).

## Properties

### power
- **Type:** [[Energy]]
How much power should be provided.

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
Surface property must have a positive [[SurfacePropertyPrototype#default_value|default value]]. When [[SolarPanelEquipmentPrototype#solar_coefficient_property|SolarPanelEquipmentPrototype::solar_coefficient_property]] is set to point at a different surface property than "solar-power", then [[LuaSurface#solar_power_multiplier|LuaSurface::solar_power_multiplier]] and [[SpaceLocationPrototype#solar_power_in_space|SpaceLocationPrototype::solar_power_in_space]] will be ignored as the solar panel power output will be only affected by value of this surface property set on the surface using [[PlanetPrototype#surface_properties|PlanetPrototype::surface_properties]] or [[LuaSurface#set_property|LuaSurface::set_property]].

Due to equipment grid overall description, when solar_coefficient_property is not solar-power, a different locale will be used to show total energy production of solar panels: `description.solar-panel-power-X` where X is the surface property name.
