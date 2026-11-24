---
title: PipeConnectionDefinition
tags: [factorio-api, runtime, concept]
---
# PipeConnectionDefinition

## Fields

### connection_type
- **Type:** [[PipeConnectionType]]

### positions
- **Type:** array<[[MapPosition]]>
The 4 cardinal direction connection points for this pipe.

### max_underground_distance
- **Type:** [[uint32]]
- **Optional**
The maximum tile distance this underground connection can connect.

### flow_direction
- **Type:** [[FluidFlowDirection]]

### direction
- **Type:** [[defines.direction]]

### connection_category
- **Type:** array<[[string]]>

### hide_connection_info
- **Type:** [[boolean]]

### linked_connection_id
- **Type:** [[uint32]]
- **Optional**
Only provided if `connection_type` is `"linked"`.

### alt_direction
- **Type:** [[defines.direction]]
- **Optional**
Only provided if different from `direction`.

### alt_position
- **Type:** [[MapPosition]]
- **Optional**
Only provided if different from first position inside of `positions`.
