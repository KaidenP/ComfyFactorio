---
title: LuaBurner
tags: [factorio-api, runtime, class]
---
# LuaBurner

A reference to the burner energy source owned by a specific [[LuaEntity]] or [[LuaEquipment]].

## Attributes

### owner
- **Type:** [[LuaEntity]] | [[LuaEquipment]]
The owner of this burner energy source

### inventory
- **Type:** [[LuaInventory]]
The fuel inventory.

### burnt_result_inventory
- **Type:** [[LuaInventory]]
The burnt result inventory.

### heat
- **Type:** [[double]]
- **Writable:** [[double]]
The current heat (energy) stored in this burner.

### heat_capacity
- **Type:** [[double]]
The maximum heat (maximum energy) that this burner can store.

### remaining_burning_fuel
- **Type:** [[double]]
- **Writable:** [[double]]
The amount of energy left in the currently-burning fuel item.

Writing to this will silently do nothing if there's no [[LuaBurner#currently_burning|LuaBurner::currently_burning]] set.

### currently_burning
- **Type:** [[ItemIDAndQualityIDPair]]
- **Writable:** [[ItemWithQualityID]]
- **Optional**
The currently burning item. Writing `nil` will void the currently burning item without producing a [[LuaBurner#burnt_result|LuaBurner::burnt_result]].

Writing to this automatically handles correcting [[LuaBurner#remaining_burning_fuel|LuaBurner::remaining_burning_fuel]].

When writing, any item with a [[LuaItemPrototype#fuel_value|fuel value]] is considered valid fuel; the fuel category does not have to match.

### fuel_categories
- **Type:** dictionary<[[string]] → `true`>
The fuel categories this burner uses.

The value in the dictionary is meaningless and exists just to allow for easy lookup.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
