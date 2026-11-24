---
title: RailSignalBasePrototype
tags: [factorio-api, prototype]
---
# RailSignalBasePrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Abstract**

The abstract base entity for both rail signals.

## Properties

### ground_picture_set
- **Type:** [[RailSignalPictureSet]]

### elevated_picture_set
- **Type:** [[RailSignalPictureSet]]

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

### default_red_output_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### default_orange_output_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### default_green_output_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### default_blue_output_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### elevated_collision_mask
- **Type:** [[CollisionMaskConnector]]
- **Optional**
Defaults to the mask from [[UtilityConstants (prototype)#default_collision_masks|UtilityConstants::default_collision_masks]] when indexed by  `type .. "/elevated"`.

### elevated_selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `55`

### collision_box
- **Type:** [[BoundingBox (type)]]
- **Optional**
- **Default:** `{{-0.2, -0.2}, {0.2, 0.2}}`
- **Overrides parent**
The [[EntityPrototype#collision_box|collision_box]] of rail signals is hardcoded to `{{-0.2, -0.2}, {0.2, 0.2}}`.

### flags
- **Type:** [[EntityPrototypeFlags (type)]]
- **Optional**
- **Overrides parent**
The "placeable-off-grid" flag will be ignored for rail signals.

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `45`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
