---
title: LuaControlBehavior
tags: [factorio-api, runtime, class]
---
# LuaControlBehavior

> **Abstract class** — not directly instantiable.

The control behavior for an entity. Inserters have logistic network and circuit network behavior logic, lamps have circuit logic and so on. This is an abstract base class that concrete control behaviors inherit.

An control reference becomes invalid once the control behavior is removed or the entity (see [[LuaEntity]]) it resides in is destroyed.

## Attributes

### input_networks
- **Type:** [[CircuitNetworkSelection]]
- **Writable:** [[CircuitNetworkSelection]]
- **Optional**
Which circuit networks (red/green) to read signals from. Defaults to both wire colors.

`nil` if this control behavior does not allow selecting the input networks.

### output_networks
- **Type:** [[CircuitNetworkSelection]]
- **Writable:** [[CircuitNetworkSelection]]
- **Optional**
Which circuit networks (red/green) to send signals to. Defaults to both wire colors.

`nil` if this control behavior does not allow selecting the output networks.

### type
- **Type:** [[defines.control_behavior#type]]
The concrete type of this control behavior.

### entity
- **Type:** [[LuaEntity]]
The entity this control behavior belongs to.

## Methods

### get_circuit_network

**Parameters:**
- **`wire_connector_id`** — [[defines.wire_connector_id]]: Wire connector to get circuit network for.

**Returns:**
- [[LuaCircuitNetwork]] *(optional)*: The circuit network or nil.
