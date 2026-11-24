---
title: ContainerPrototype
tags: [factorio-api, prototype]
---
# ContainerPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `container`

A generic container, such as a chest.

## Properties

### inventory_size
- **Type:** [[ItemStackIndex (type)]]
The number of slots in this container.

### quality_affects_inventory_size
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### direction_count
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `1`
Amount of directions this container should have. Allowed values are 1, 2 and 4.

### picture
- **Type:** [[Sprite4Way]]
- **Optional**
The picture displayed for this entity.

### inventory_type
- **Type:** `"normal"` | `"with_bar"` | `"with_filters_and_bar"` | `"with_custom_stack_size"` | `"with_weight_limit"`
- **Optional**
- **Default:** `"with_bar"`
Determines the type of inventory that this container has. Whether the inventory has a limiter bar, can be filtered (like cargo wagons), uses a custom stack size for contained item stacks (like artillery wagon), or uses a weight limit (like space age rocket silo).

### inventory_properties
- **Type:** [[InventoryWithCustomStackSizeSpecification (type)]]
- **Optional**
Only used when `inventory_type` is `"with_custom_stack_size"`.

### inventory_weight_limit
- **Type:** [[Weight (type)]]
- **Optional**
- **Default:** `0`
Only used when `inventory_type` is `"with_weight_limit"`.

### circuit_wire_max_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The maximum circuit wire distance for this container.

### draw_copper_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_circuit_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### circuit_connector
- **Type:** array<[[CircuitConnectorDefinition]]>
- **Optional**
If given, there must be exactly `direction_count` elements in the table.

### default_status
- **Type:** [[EntityStatus]]
- **Optional**
- **Default:** `"normal"`

### default_empty_slots_signal
- **Type:** [[SignalIDConnector]]
- **Optional**
