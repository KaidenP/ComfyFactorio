---
title: LuaEquipment
tags: [factorio-api, runtime, class]
---
# LuaEquipment

An item in a [[LuaEquipmentGrid]], for example a fusion reactor placed in one's power armor.

An equipment reference becomes invalid once the equipment is removed or the equipment grid it resides in is destroyed.

## Attributes

### name
- **Type:** [[string]]
Name of this equipment.

### ghost_name
- **Type:** [[string]]
Name of the equipment contained in this ghost

### type
- **Type:** [[string]]
Type of this equipment.

### ghost_type
- **Type:** [[string]]
Type of the equipment contained in this ghost.

### quality
- **Type:** [[LuaQualityPrototype]]
Quality of this equipment.

### position
- **Type:** [[EquipmentPosition]]
Position of this equipment in the equipment grid.

### shape
- **Type:** table
Shape of this equipment.

### shield
- **Type:** [[double]]
- **Writable:** [[double]]
Current shield value of the equipment. Can't be set higher than [[LuaEquipment#max_shield|LuaEquipment::max_shield]].

Trying to write this value on non-shield equipment will throw an error.

### max_shield
- **Type:** [[double]]
Maximum shield value. `0` if this equipment doesn't have a shield.

### max_solar_power
- **Type:** [[double]]
Maximum energy per tick crated by this equipment on the current surface. Actual generated energy varies depending on the daylight levels.

### inventory_bonus
- **Type:** [[uint32]]
Inventory size bonus.

### movement_bonus
- **Type:** [[double]]
Movement speed bonus.

### generator_power
- **Type:** [[double]]
Energy generated per tick.

### energy
- **Type:** [[double]]
- **Writable:** [[double]]
Current available energy.

### max_energy
- **Type:** [[double]]
Maximum amount of energy that can be stored in this equipment.

### prototype
- **Type:** [[LuaEquipmentPrototype]]

### ghost_prototype
- **Type:** [[LuaEquipmentPrototype]]
The prototype of the equipment contained in this ghost.

### burner
- **Type:** [[LuaBurner]]
- **Optional**
The burner energy source for this equipment, if any.

### to_be_removed
- **Type:** [[boolean]]
If this equipment is marked to be removed.

### power_production
- **Type:** [[double]]
- **Writable:** [[double]]
The power production specific to the ElectricEnergyInterfaceEquipment type.

### power_usage
- **Type:** [[double]]
- **Writable:** [[double]]
The power usage specific to the ElectricEnergyInterfaceEquipment type.

### electric_buffer_size
- **Type:** [[double]]
- **Writable:** [[double]]
The power buffer size of this ElectricEnergyInterfaceEquipment.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
