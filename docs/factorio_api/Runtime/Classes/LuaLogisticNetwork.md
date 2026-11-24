---
title: LuaLogisticNetwork
tags: [factorio-api, runtime, class]
---
# LuaLogisticNetwork

A single logistic network of a given force on a given surface.

## Attributes

### network_id
- **Type:** [[uint32]]
The unique logistic network ID.

### custom_name
- **Type:** [[string]]
- **Writable:** [[string]]
- **Optional**
The custom logistic network name set by the player or by script, if any.

### force
- **Type:** [[LuaForce]]
The force this logistic network belongs to.

### available_logistic_robots
- **Type:** [[uint32]]
Number of logistic robots available for a job.

### all_logistic_robots
- **Type:** [[uint32]]
The total number of logistic robots in the network (idle and active + in roboports).

### available_construction_robots
- **Type:** [[uint32]]
Number of construction robots available for a job.

### all_construction_robots
- **Type:** [[uint32]]
The total number of construction robots in the network (idle and active + in roboports).

### robot_limit
- **Type:** [[uint32]]
Maximum number of robots the network can work with. Currently only used for the personal roboport.

### cells
- **Type:** array<[[LuaLogisticCell]]>
All cells in this network.

### providers
- **Type:** array<[[LuaEntity]]>
All entities that have logistic provider points in this network.

### empty_providers
- **Type:** array<[[LuaEntity]]>
All entities that have empty logistic provider points in this network.

### requesters
- **Type:** array<[[LuaEntity]]>
All entities that have logistic requester points in this network.

### storages
- **Type:** array<[[LuaEntity]]>
All entities that have logistic storage points in this network.

### logistic_members
- **Type:** array<[[LuaEntity]]>
All other entities that have logistic points in this network (inserters mostly).

### provider_points
- **Type:** array<[[LuaLogisticPoint]]>
All things that have provider points in this network.

### passive_provider_points
- **Type:** array<[[LuaLogisticPoint]]>
All passive provider points in this network.

### active_provider_points
- **Type:** array<[[LuaLogisticPoint]]>
All active provider points in this network.

### empty_provider_points
- **Type:** array<[[LuaLogisticPoint]]>
All things that have empty provider points in this network.

### requester_points
- **Type:** array<[[LuaLogisticPoint]]>
All things that have requester points in this network.

### storage_points
- **Type:** array<[[LuaLogisticPoint]]>
All things that have storage points in this network.

### robots
- **Type:** array<[[LuaEntity]]>
All currently deployed robots in this logistic network.

### construction_robots
- **Type:** array<[[LuaEntity]]>
All currently deployed construction robots in this logistic network.

### logistic_robots
- **Type:** array<[[LuaEntity]]>
All currently deployed logistic robots in this logistic network.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### get_item_count
Count given or all items in the network or given members.

**Parameters:**
- **`item`** — [[ItemWithQualityID]] *(optional)*: Item name to count. If not given, gives counts of all items in the network.
- **`member`** — `"storage"` | `"providers"` *(optional)*: Logistic members to check. If not given, gives count in the entire network.

**Returns:**
- [[int32]]

### get_contents
Get item counts for the entire network, similar to how [[LuaInventory#get_contents|LuaInventory::get_contents]] does.

**Parameters:**
- **`member`** — `"storage"` | `"providers"` *(optional)*: Logistic members to check. If not given, gives item counts for the entire network.

**Returns:**
- array<[[ItemWithQualityCount]]>: List of all items in the network.

### remove_item
Remove items from the logistic network. This will actually remove the items from some logistic chests.

**Parameters:**
- **`item`** — [[ItemStackIdentification]]: What to remove.
- **`members`** — `"active-provider"` | `"passive-provider"` | `"buffer"` | `"storage"` *(optional)*: Which logistic members to remove from. If not specified, removes from the network in the usual order.

**Returns:**
- [[uint32]]: Number of items removed.

### insert
Insert items into the logistic network. This will actually insert the items into some logistic chests.

**Parameters:**
- **`item`** — [[ItemStackIdentification]]: What to insert.
- **`members`** — `"storage"` | `"storage-empty"` | `"storage-empty-slot"` | `"requester"` *(optional)*: Which logistic members to insert the items to. `"storage-empty"` inserts into storage chests that are completely empty, `"storage-empty-slot"` inserts into storage chests that have an empty slot. If not specified, inserts items into the logistic network in the usual order.

**Returns:**
- [[uint32]]: Number of items actually inserted.

### find_cell_closest_to
Find logistic cell closest to a given position.

**Parameters:**
- **`position`** — [[MapPosition]]

**Returns:**
- [[LuaLogisticCell]] *(optional)*: `nil` if no cell was found.

### select_pickup_point
Find the 'best' logistic point with this item ID and from the given position or from given chest type.

Takes a table with the following fields:
- **`name`** — [[ItemWithQualityID]]: Name of the item to pick up.
- **`position`** — [[MapPosition]] *(optional)*: When given, it will find the storage 'best' storage point from this position.
- **`include_buffers`** — [[boolean]] *(optional)*: Whether to consider buffer chests or not. Defaults to false. Only considered if selecting with position.
- **`members`** — `"active-provider"` | `"passive-provider"` | `"buffer"` | `"storage"` *(optional)*: When given, it will find from only the specific type of member. If not specified, selects with normal priorities. Not considered if position is specified.

**Returns:**
- [[LuaLogisticPoint]] *(optional)*: `nil` if no point was found.

### select_drop_point
Find a logistic point to drop the specific item stack.

Takes a table with the following fields:
- **`stack`** — [[ItemStackIdentification]]: Name of the item to drop off.
- **`members`** — `"storage"` | `"storage-empty"` | `"storage-empty-slot"` | `"requester"` *(optional)*: When given, it will find from only the specific type of member. If not specified, selects with normal priorities.

**Returns:**
- [[LuaLogisticPoint]] *(optional)*: `nil` if no point was found.

### can_satisfy_request
Can the network satisfy a request for a given item and count.

**Parameters:**
- **`item`** — [[ItemWithQualityID]]: Item name to check.
- **`count`** — [[uint32]] *(optional)*: Count to check. Defaults to 1.
- **`include_buffers`** — [[boolean]] *(optional)*: Should buffers be considered? Defaults to false.

**Returns:**
- [[boolean]]: Whether the network can satisfy the request.

### get_supply_counts
Get the amount of items of the given type indexed by the storage member.

**Parameters:**
- **`item`** — [[ItemWithQualityID]]: Item name to check.

**Returns:**
- [[LogisticsNetworkSupplyCounts]]

### get_supply_points
Gets the logistic points with of the given type indexed by the storage member.

**Parameters:**
- **`item`** — [[ItemWithQualityID]]: Item name to check.

**Returns:**
- [[LogisticsNetworkSupplyPoints]]
