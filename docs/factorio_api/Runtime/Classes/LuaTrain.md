---
title: LuaTrain
tags: [factorio-api, runtime, class]
---
# LuaTrain

A train. Trains are a sequence of connected rolling stocks -- locomotives and wagons.

## Attributes

### manual_mode
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
When `true`, the train is explicitly controlled by the player or script. When `false`, the train moves autonomously according to its schedule.

### speed
- **Type:** [[double]]
- **Writable:** [[double]]
Current speed.

Changing the speed of the train is potentially an unsafe operation because train uses the speed for its internal calculations of break distances, etc.

### max_forward_speed
- **Type:** [[double]]
Current max speed when moving forward, depends on locomotive prototype and fuel.

### max_backward_speed
- **Type:** [[double]]
Current max speed when moving backwards, depends on locomotive prototype and fuel.

### weight
- **Type:** [[double]]
The weight of this train.

### carriages
- **Type:** array<[[LuaEntity]]>
The rolling stocks this train is composed of, with the numbering starting at the [[LuaTrain#front_stock|front]] of the train.

### locomotives
- **Type:** table
Locomotives of the train.
**Examples:**

```
-- called on a LuaTrain with 3 locomotives, it returns 3 LuaEntities:
train.locomotives -- => {front_movers = {loco1, loco2}, back_movers = {loco3}}
```

### cargo_wagons
- **Type:** array<[[LuaEntity]]>
The cargo carriages the train contains.

### fluid_wagons
- **Type:** array<[[LuaEntity]]>
The fluid carriages the train contains.

### schedule
- **Type:** [[TrainSchedule]]
- **Writable:** [[TrainSchedule]]
- **Optional**
This train's current schedule, if any. Set to `nil` to clear.

The schedule can't be changed by modifying the returned table. Instead, changes must be made by assigning a new table to this attribute.

This is a simplified schedule that does **not** include train groups and interrupts. See [[LuaTrain#get_schedule|LuaTrain::get_schedule]] for full access to the train schedule, including interrupts and train groups.

### state
- **Type:** [[defines.train_state]]
This train's current state.

### front_stock
- **Type:** [[LuaEntity]]
- **Optional**
The front stock of this train, if any. The front of the train is in the direction that a majority of locomotives are pointing in. If it's a tie, the North and West directions take precedence.

### back_stock
- **Type:** [[LuaEntity]]
- **Optional**
The back stock of this train, if any. The back of the train is at the opposite end of the [[LuaTrain#front_stock|front]].

### station
- **Type:** [[LuaEntity]]
- **Optional**
The train stop this train is stopped at, if any.

### has_path
- **Type:** [[boolean]]
If this train has a path.

### path_end_rail
- **Type:** [[LuaEntity]]
- **Optional**
The destination rail this train is currently pathing to, if any.

### path_end_stop
- **Type:** [[LuaEntity]]
- **Optional**
The destination train stop this train is currently pathing to, if any.

### id
- **Type:** [[uint32]]
The unique train ID.

### passengers
- **Type:** array<[[LuaPlayer]]>
The player passengers on the train

This does *not* index using player index. See [[LuaPlayer#index|LuaPlayer::index]] on each player instance for the player index.

### riding_state
- **Type:** [[RidingState]]
The riding state of this train.

### killed_players
- **Type:** dictionary<[[uint32]] → [[uint32]]>
The players killed by this train.

The keys are the player indices, the values are how often this train killed that player.

### kill_count
- **Type:** [[uint32]]
The total number of kills by this train.

### path
- **Type:** [[LuaRailPath]]
- **Optional**
The path this train is using, if any.

### signal
- **Type:** [[LuaEntity]]
- **Optional**
The signal this train is arriving or waiting at, if any.

### group
- **Type:** [[string]]
- **Writable:** [[string]]
The group this train belongs to.

Setting the group will apply the schedule of the group to this train.

### front_end
- **Type:** [[LuaRailEnd]]
Front end of the train: Rail and direction on that rail where the train will go when moving forward

### back_end
- **Type:** [[LuaRailEnd]]
Back end of the train: Rail and direction on that rail where the train will go when moving backward

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### get_item_count
Get the amount of a particular item stored in the train.

**Parameters:**
- **`item`** — [[ItemFilter]] *(optional)*: If not given, counts all items.

**Returns:**
- [[uint32]]

### get_contents
Get a mapping of the train's inventory.

**Returns:**
- array<[[ItemWithQualityCount]]>: List of all items in the train.

### remove_item
Remove some items from the train.

**Parameters:**
- **`stack`** — [[ItemStackIdentification]]: The amount and type of items to remove

**Returns:**
- [[uint32]]: Number of items actually removed.

### insert
Insert a stack into the train.

**Parameters:**
- **`stack`** — [[ItemStackIdentification]]

### clear_items_inside
Clear all items in this train.

### recalculate_path
Checks if the path is invalid and tries to re-path if it isn't.

**Parameters:**
- **`force`** — [[boolean]] *(optional)*: Forces the train to re-path regardless of the current path being valid or not.

**Returns:**
- [[boolean]]: If the train has a path after the repath attempt.

### get_fluid_count
Get the amount of a particular fluid stored in the train.

**Parameters:**
- **`fluid`** — [[string]] *(optional)*: Fluid name to count. If not given, counts all fluids.

**Returns:**
- [[double]]

### get_fluid_contents
Gets a mapping of the train's fluid inventory.

**Returns:**
- dictionary<[[string]] → [[FluidAmount]]>: The counts, indexed by fluid names.

### remove_fluid
Remove some fluid from the train.

**Parameters:**
- **`fluid`** — [[Fluid]]

**Returns:**
- [[double]]: The amount of fluid actually removed.

### insert_fluid
Inserts the given fluid into the first available location in this train.

**Parameters:**
- **`fluid`** — [[Fluid]]

**Returns:**
- [[double]]: The amount inserted.

### clear_fluids_inside
Clears all fluids in this train.

### go_to_station
Go to the station specified by the index in the train's schedule.

**Parameters:**
- **`index`** — [[uint32]]

### get_rails
Gets all rails under the train.

**Returns:**
- array<[[LuaEntity]]>

### get_rail_end
Gets a LuaRailEnd object pointing away from the train at specified end of the train

**Parameters:**
- **`direction`** — [[defines.rail_direction]]

**Returns:**
- [[LuaRailEnd]]

### get_schedule
This allows full access to the train schedule, including modifying the schedule records, the train group and the interrupts.

**Returns:**
- [[LuaSchedule]]
