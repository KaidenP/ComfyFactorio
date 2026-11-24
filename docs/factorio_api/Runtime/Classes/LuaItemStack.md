---
title: LuaItemStack
tags: [factorio-api, runtime, class]
---
# LuaItemStack

> **Extends:** [[LuaItemCommon]]

A reference to an item and count owned by some external entity.

In most instances this is a simple reference as in: it points at a specific slot in an inventory and not the item in the slot.

In the instance this references an item on a [[LuaTransportLine]] the reference is only guaranteed to stay valid (and refer to the same item) as long as nothing changes the transport line.

## Attributes

### valid_for_read
- **Type:** [[boolean]]
Is this valid for reading? Differs from the usual `valid` in that `valid` will be `true` even if the item stack is blank but the entity that holds it is still valid.

### prototype
- **Type:** [[LuaItemPrototype]]
Prototype of the item held in this stack.

### name
- **Type:** [[string]]
Prototype name of the item held in this stack.

### type
- **Type:** [[string]]
Type of the item prototype.

### count
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
Number of items in this stack.

### health
- **Type:** [[float]]
- **Writable:** [[float]]
How much health the item has, as a number in range `[0, 1]`.

### quality
- **Type:** [[LuaQualityPrototype]]
The quality of this item.

### spoil_tick
- **Type:** [[MapTick]]
- **Writable:** [[MapTick]]
The tick this item spoils, or `0` if it does not spoil. When writing, setting to anything < the current game tick will spoil the item instantly.

### spoil_percent
- **Type:** [[double]]
- **Writable:** [[double]]
The percent spoiled this item is if it spoils. `0` in the case of the item not spoiling.

### item
- **Type:** [[LuaItem]]
- **Optional**
If the item has additional data, returns LuaItem pointing at the extra data, otherwise returns nil.

### is_module
- **Type:** [[boolean]]
If this is a module

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### add_ammo
Add ammo to this ammo item.
*Only available on:* `AmmoItem`

**Parameters:**
- **`amount`** — [[float]]: Amount of ammo to add.

### drain_ammo
Remove ammo from this ammo item.
*Only available on:* `AmmoItem`

**Parameters:**
- **`amount`** — [[float]]: Amount of ammo to remove.

### add_durability
Add durability to this tool item.
*Only available on:* `ToolItem`

**Parameters:**
- **`amount`** — [[double]]: Amount of durability to add.

### drain_durability
Remove durability from this tool item.
*Only available on:* `ToolItem`

**Parameters:**
- **`amount`** — [[double]]: Amount of durability to remove.

### use_capsule
Use the capsule item with the entity as the source, targeting the given position.

**Parameters:**
- **`entity`** — [[LuaEntity]]: The entity to use the capsule item with.
- **`target_position`** — [[MapPosition]]: The position to use the capsule item with.

**Returns:**
- array<[[LuaEntity]]>: Array of the entities that were created by the capsule action.

### can_set_stack
Would a call to [[LuaItemStack#set_stack|LuaItemStack::set_stack]] succeed?

**Parameters:**
- **`stack`** — [[ItemStackIdentification]] *(optional)*: Stack that would be set, possibly `nil`.

**Returns:**
- [[boolean]]

### set_stack
Set this item stack to another item stack.

**Parameters:**
- **`stack`** — [[ItemStackIdentification]] *(optional)*: Item stack to set it to. Omitting this parameter or passing `nil` will clear this item stack, as if [[LuaItemStack#clear|LuaItemStack::clear]] was called.

**Returns:**
- [[boolean]]: Whether the stack was set successfully. Returns `false` if this stack was not [[LuaItemStack#can_set_stack|valid for write]].

### transfer_stack
Transfers the given item stack into this item stack.

**Parameters:**
- **`stack`** — [[ItemStackIdentification]]
- **`amount`** — [[uint32]] *(optional)*

**Returns:**
- [[boolean]]: `true` if the full stack (or requested amount) was transferred.

### export_stack
Export a supported item (blueprint, blueprint-book, deconstruction-planner, upgrade-planner, item-with-tags) to a string.

**Returns:**
- [[string]]: The exported string

### import_stack
Import a supported item (blueprint, blueprint-book, deconstruction-planner, upgrade-planner, item-with-tags) from a string.

**Parameters:**
- **`data`** — [[string]]: The string to import

**Returns:**
- [[int32]]: 0 if the import succeeded with no errors. -1 if the import succeeded with errors. 1 if the import failed.

### swap_stack
Swaps this item stack with the given item stack if allowed.

**Parameters:**
- **`stack`** — [[LuaItemStack]]

**Returns:**
- [[boolean]]: Whether the 2 stacks were swapped successfully.

### clear
Clear this item stack.

### create_grid
Creates the equipment grid for this item if it doesn't exist and this is an item-with-entity-data that supports equipment grids.
*Only available on:* `ItemWithEntityData`

**Returns:**
- [[LuaEquipmentGrid]]

### spoil
Spoils this item if the item can spoil.
