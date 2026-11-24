---
title: LinkedContainerPrototype
tags: [factorio-api, prototype]
---
# LinkedContainerPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `linked-container`

A container that shares its inventory with containers with the same [[LuaEntity#link_id|link_id]], which can be set via the GUI. The link IDs are per prototype and force, so only containers with the **same ID**, **same prototype name** and **same force** will share inventories.

## Properties

### inventory_size
- **Type:** [[ItemStackIndex (type)]]
Must be > 0.

### picture
- **Type:** [[Sprite]]
- **Optional**

### inventory_type
- **Type:** `"normal"` | `"with_bar"` | `"with_filters_and_bar"` | `"with_custom_stack_size"` | `"with_weight_limit"`
- **Optional**
- **Default:** `"with_bar"`
Determines the type of inventory that this linked container has. Whether the inventory has a limiter bar, can be filtered (like cargo wagons), uses a custom stack size for contained item stacks (like artillery wagon), or uses a weight limit (like space age rocket silo).

### inventory_properties
- **Type:** [[InventoryWithCustomStackSizeSpecification (type)]]
- **Optional**
Only used when `inventory_type` is `"with_custom_stack_size"`.

### inventory_weight_limit
- **Type:** [[Weight (type)]]
- **Optional**
- **Default:** `0`
Only used when `inventory_type` is `"with_weight_limit"`.

### gui_mode
- **Type:** `"all"` | `"none"` | `"admins"`
- **Optional**
- **Default:** `"all"`
Players that can access the GUI to change the link ID.

### circuit_wire_max_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The maximum circuit wire distance for this linked container.

### draw_copper_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_circuit_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### circuit_connector
- **Type:** [[CircuitConnectorDefinition]]
- **Optional**

### default_empty_slots_signal
- **Type:** [[SignalIDConnector]]
- **Optional**
