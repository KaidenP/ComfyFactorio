---
title: PipeConnection
tags: [factorio-api, runtime, concept]
---
# PipeConnection

A single pipe connection for a given fluidbox.

## Fields

### flow_direction
- **Type:** [[FluidFlowDirection]]

### connection_type
- **Type:** [[PipeConnectionType]]

### position
- **Type:** [[MapPosition]]
The absolute position of this connection within the entity.

### target_position
- **Type:** [[MapPosition]]
The absolute position of the connection's intended target.

### target
- **Type:** [[LuaEntity]]
- **Optional**
The connected fluidbox, if any.

### target_fluidbox_index
- **Type:** [[uint32]]
- **Optional**
The index of the target fluidbox, if any.

### target_pipe_connection_index
- **Type:** [[uint32]]
- **Optional**
The index of the target fluidbox pipe connection, if any.
