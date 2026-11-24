---
title: TrainStopPrototype
tags: [factorio-api, prototype]
---
# TrainStopPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `train-stop`

A [train stop](https://wiki.factorio.com/Train_stop).

## Properties

### animation_ticks_per_frame
- **Type:** [[uint32 (type)]]

### rail_overlay_animations
- **Type:** [[Animation4Way]]
- **Optional**

### animations
- **Type:** [[Animation4Way]]
- **Optional**

### top_animations
- **Type:** [[Animation4Way]]
- **Optional**

### default_train_stopped_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### default_trains_count_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### default_trains_limit_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### default_priority_signal
- **Type:** [[SignalIDConnector]]
- **Optional**

### circuit_wire_max_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`

### draw_copper_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_circuit_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### color
- **Type:** [[Color (type)]]
- **Optional**

### chart_name
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### light1
- **Type:** [[TrainStopLight]]
- **Optional**

### light2
- **Type:** [[TrainStopLight]]
- **Optional**

### drawing_boxes
- **Type:** [[TrainStopDrawingBoxes]]
- **Optional**

### circuit_connector
- **Type:** ([[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]], [[CircuitConnectorDefinition]])
- **Optional**

### build_grid_size
- **Type:** `2`
- **Optional**
- **Default:** `2`
- **Overrides parent**
Has to be 2 for 2x2 grid.
