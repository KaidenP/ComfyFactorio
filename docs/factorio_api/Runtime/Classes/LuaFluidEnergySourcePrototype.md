---
title: LuaFluidEnergySourcePrototype
tags: [factorio-api, runtime, class]
---
# LuaFluidEnergySourcePrototype

Prototype of a fluid energy source.

## Attributes

### emissions_per_joule
- **Type:** dictionary<[[string]] → [[double]]>
The table of emissions of this energy source in `pollution/Joule`, indexed by pollutant type. Multiplying it by energy consumption in `Watt` gives `pollution/second`.

### render_no_network_icon
- **Type:** [[boolean]]

### render_no_power_icon
- **Type:** [[boolean]]

### effectivity
- **Type:** [[double]]

### burns_fluid
- **Type:** [[boolean]]

### scale_fluid_usage
- **Type:** [[boolean]]

### destroy_non_fuel_fluid
- **Type:** [[boolean]]

### hide_from_stats
- **Type:** [[boolean]]

### fluid_usage_per_tick
- **Type:** [[double]]

### smoke
- **Type:** array<[[SmokeSource]]>
The smoke sources for this prototype, if any.

### maximum_temperature
- **Type:** [[float]]
- **Optional**

### minimum_input_temperature
- **Type:** [[float]]
- **Optional**
The minimum input temperature that this energy source accepts, if specified. An input fluid below this temperature will cause the energy source to stop working.

### maximum_input_temperature
- **Type:** [[float]]
- **Optional**
The maximum input temperature that this energy source accepts, if specified. An input fluid above this temperature will cause the energy source to stop working.

### fluid_box
- **Type:** [[LuaFluidBoxPrototype]]
The fluid box for this energy source.

### output_fluid_box
- **Type:** [[LuaFluidBoxPrototype]]
- **Optional**

### spent_fluid
- **Type:** [[SpentFluidSpecification]]
- **Optional**

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
