---
title: LoaderPrototype
tags: [factorio-api, prototype]
---
# LoaderPrototype

> **Parent:** [[TransportBeltConnectablePrototype]] · **Abstract**

Continuously loads and unloads machines, as an alternative to inserters.

## Properties

### structure
- **Type:** [[LoaderStructure]]
- **Optional**

### filter_count
- **Type:** [[uint8 (type)]]
How many item filters this loader has. Maximum count of filtered items in loader is 5.

### structure_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### container_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1.5`
The distance between the position of this loader and the tile of the loader's container target.

### allow_rail_interaction
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether this loader can load and unload [[RollingStockPrototype]].

### allow_container_interaction
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether this loader can load and unload stationary inventories such as containers and crafting machines.

### per_lane_filters
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If filters are per lane. Can only be set to true if filter_count is equal to 2.

### max_belt_stack_size
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `1`
- **Requires:** `space_age`
Loader will not create stacks on belt that are larger than this value. Must be >= 1.

### adjustable_belt_stack_size
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Requires:** `space_age`
Loader belt stack size can be adjusted at runtime. Requires [[LoaderPrototype#max_belt_stack_size|LoaderPrototype::max_belt_stack_size]] to be > 1.

### wait_for_full_stack
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When set, this loader will ignore items for which there is not enough to create a full belt stack. Relevant only when loader can create belt stacks.

### respect_insert_limits
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When set, this loader will respect the same automated insertion limits as inserters do, instead of inserting up to the full ingredient stack capacity.

### belt_length
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.5`
How long this loader's belt is. Should be the same as belt_distance, which is hardcoded to `0.5` for [[Loader1x2Prototype]] and to 0 for [[Loader1x1Prototype]]. See the linked prototypes for an explanation of belt_distance.

### energy_source
- **Type:** [[ElectricEnergySource]] | [[HeatEnergySource]] | [[FluidEnergySource]] | [[VoidEnergySource]]
- **Optional**

### energy_per_item
- **Type:** [[Energy]]
- **Optional**
- **Default:** `0`
Energy in Joules. Can't be negative.

### circuit_wire_max_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The maximum circuit wire distance for this entity.

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
First the four cardinal directions for `direction_out`, followed by the four directions for `direction_in`.
