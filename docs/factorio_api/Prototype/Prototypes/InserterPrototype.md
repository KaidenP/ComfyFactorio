---
title: InserterPrototype
tags: [factorio-api, prototype]
---
# InserterPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `inserter`

An [inserter](https://wiki.factorio.com/Inserter).

## Properties

### extension_speed
- **Type:** [[double (type)]]

### rotation_speed
- **Type:** [[double (type)]]

### starting_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.7`

### insert_position
- **Type:** [[Vector (type)]]

### pickup_position
- **Type:** [[Vector (type)]]

### platform_picture
- **Type:** [[Sprite4Way]]
- **Optional**

### platform_frozen
- **Type:** [[Sprite4Way]]
- **Optional**

### platform_picture_flipped
- **Type:** [[Sprite4Way]]
- **Optional**

### platform_frozen_flipped
- **Type:** [[Sprite4Way]]
- **Optional**

### hand_base_picture
- **Type:** [[Sprite]]
- **Optional**

### hand_open_picture
- **Type:** [[Sprite]]
- **Optional**

### hand_closed_picture
- **Type:** [[Sprite]]
- **Optional**

### hand_base_frozen
- **Type:** [[Sprite]]
- **Optional**

### hand_open_frozen
- **Type:** [[Sprite]]
- **Optional**

### hand_closed_frozen
- **Type:** [[Sprite]]
- **Optional**

### hand_base_shadow
- **Type:** [[Sprite]]
- **Optional**

### hand_open_shadow
- **Type:** [[Sprite]]
- **Optional**

### hand_closed_shadow
- **Type:** [[Sprite]]
- **Optional**

### energy_source
- **Type:** [[EnergySource]]
Defines how this inserter gets energy. The emissions set on the energy source are ignored so inserters cannot produce pollution.

### energy_per_movement
- **Type:** [[Energy]]
- **Optional**
- **Default:** `0`

### energy_per_rotation
- **Type:** [[Energy]]
- **Optional**
- **Default:** `0`

### bulk
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether this inserter is considered a bulk inserter. Relevant for determining how [inserter capacity bonus (research)](https://wiki.factorio.com/Inserter_capacity_bonus_(research)) applies to the inserter.

### uses_inserter_stack_size_bonus
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
When set to false, then relevant value of inserter stack size bonus ([[LuaForce#inserter_stack_size_bonus|LuaForce::inserter_stack_size_bonus]] or [[LuaForce#bulk_inserter_capacity_bonus|LuaForce::bulk_inserter_capacity_bonus]]) will not affect inserter stack size.

### allow_custom_vectors
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether pickup and insert position can be set run-time.

### allow_burner_leech
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether this burner inserter can fuel itself from the fuel inventory of the entity it is picking up items from.

### draw_held_item
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the item that the inserter is holding should be drawn.

### use_easter_egg
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the inserter should be able to fish [fish](https://wiki.factorio.com/Raw_fish).

### grab_less_to_match_belt_stack
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If drop target is belt, inserter may grab less so that it does not drop partial stacks unless it is forced to drop partial.

### wait_for_full_hand
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Inserter will wait until its hand is full.

### enter_drop_mode_if_held_stack_spoiled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If inserter waits for full hand it could become stuck when item in hand changed because of spoiling. If this flag is set then inserter will start dropping held stack even if it was waiting for full hand.

### use_mirroring
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### max_belt_stack_size
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `1`
- **Requires:** `space_age`
This inserter will not create stacks on belt with more than this amount of items. Must be >= 1.

### filter_count
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
How many filters this inserter has. Maximum count of filtered items in inserter is 5.

### hand_size
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.75`
Used to determine how long the arm of the inserter is when drawing it. Does not affect gameplay. The lower the value, the straighter the arm. Increasing the value will give the inserter a bigger bend due to its longer parts.

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

### default_stack_control_input_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### draw_inserter_arrow
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the yellow arrow that indicates the drop point of the inserter and the line that indicates the pickup position should be drawn.

### chases_belt_items
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the inserter hand should move to the items it picks up from belts, leading to item chasing behaviour. If this is off, the inserter hand will stay in the center of the belt and any items picked up from the edges of the belt "teleport" to the inserter hand.

### stack_size_bonus
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
Stack size bonus that is inherent to the prototype without having to be researched.

### circuit_connector
- **Type:** ([[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]])
- **Optional**

### circuit_connector_flipped
- **Type:** ([[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]])
- **Optional**
