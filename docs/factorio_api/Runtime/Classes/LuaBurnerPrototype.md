---
title: LuaBurnerPrototype
tags: [factorio-api, runtime, class]
---
# LuaBurnerPrototype

Prototype of a burner energy source.

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

### fuel_inventory_size
- **Type:** [[uint32]]

### burnt_inventory_size
- **Type:** [[uint32]]

### smoke
- **Type:** array<[[SmokeSource]]>
- **Optional**
The smoke sources for this burner prototype.

### light_flicker
- **Type:** table
- **Optional**
The light flicker definition for this burner prototype.

### fuel_categories
- **Type:** dictionary<[[string]] → `true`>
The value in the dictionary is meaningless and exists just to allow for easy lookup.

### initial_fuel
- **Type:** [[LuaItemPrototype]]
- **Optional**

### initial_fuel_percent
- **Type:** [[double]]

### auto_refuel
- **Type:** [[boolean]]

### burner_usage
- **Type:** [[LuaBurnerUsagePrototype]]

### hide_from_stats
- **Type:** [[boolean]]

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
