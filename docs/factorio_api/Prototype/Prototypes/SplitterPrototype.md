---
title: SplitterPrototype
tags: [factorio-api, prototype]
---
# SplitterPrototype

> **Parent:** [[TransportBeltConnectablePrototype]] · **Type name:** `splitter`

A [splitter](https://wiki.factorio.com/Splitter).

## Properties

### structure
- **Type:** [[Animation4Way]]
- **Optional**

### structure_patch
- **Type:** [[Animation4Way]]
- **Optional**
Drawn 1 tile north of `structure` when the splitter is facing east or west.

### frozen_patch
- **Type:** [[Sprite4Way]]
- **Optional**

### structure_animation_speed_coefficient
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### structure_animation_movement_cooldown
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `10`

### related_transport_belt
- **Type:** [[EntityID (type)]]
- **Optional**
The name of the [[TransportBeltPrototype]] which is used for the sound of the underlying belt.

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
- **Type:** ([[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]])
- **Optional**

### default_input_left_condition
- **Type:** [[CircuitConditionConnector]]
- **Optional**

### default_input_right_condition
- **Type:** [[CircuitConditionConnector]]
- **Optional**

### default_output_left_condition
- **Type:** [[CircuitConditionConnector]]
- **Optional**

### default_output_right_condition
- **Type:** [[CircuitConditionConnector]]
- **Optional**

### exchange_input_lines
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When set to true, right lane of left input belt is swapped with left lane of right input belt. This can be used to create a splitter which spreads both lanes of left input belt onto left lanes of both outputs, and both lanes of right input belt onto right lanes of both outputs.

### exchange_output_lines
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When set to true, right lane of left output belt is swapped with left lane of right output belt. This can be used to create a splitter which combines left lanes of both input lanes into left output belt and right lanes of both input lanes into right output belt.

When this option is used, a [[IconDrawSpecification (type)#scale_for_many|IconDrawSpecification::scale_for_many]] inside of [[EntityPrototype#icon_draw_specification|EntityPrototype::icon_draw_specification]] will need to be provided in case a filter is to be drawn as it will be rendered on respective sides of both output belts. Suggested value is `0.35`.
