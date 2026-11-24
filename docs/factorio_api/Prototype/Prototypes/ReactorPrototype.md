---
title: ReactorPrototype
tags: [factorio-api, prototype]
---
# ReactorPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `reactor`

A [reactor](https://wiki.factorio.com/Reactor).

## Properties

### working_light_picture
- **Type:** [[Animation]]
- **Optional**

### heat_buffer
- **Type:** [[HeatBuffer]]
The energy output as heat.

### heating_radius
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Must be >= 0.

### energy_source
- **Type:** [[EnergySource]]
May not be a heat energy source.

The input energy source, in vanilla it is a burner energy source.

### consumption
- **Type:** [[Energy]]
How much energy this reactor can consume (from the input energy source) and then output as heat.

### connection_patches_connected
- **Type:** [[SpriteVariations]]
- **Optional**
If defined, number of variations must be at least equal to count of [[HeatBuffer#connections|connections]] defined in `heat_buffer`. Each variation represents connected heat buffer connection of corresponding index.

### connection_patches_disconnected
- **Type:** [[SpriteVariations]]
- **Optional**
If defined, number of variations must be at least equal to count of [[HeatBuffer#connections|connections]] defined in `heat_buffer`. Each variation represents unconnected heat buffer connection of corresponding index.

### heat_connection_patches_connected
- **Type:** [[SpriteVariations]]
- **Optional**
If defined, number of variations must be at least equal to count of [[HeatBuffer#connections|connections]] defined in `heat_buffer`. When reactor is heated, corresponding variations are drawn over `connection_patches_connected`.

### heat_connection_patches_disconnected
- **Type:** [[SpriteVariations]]
- **Optional**
If defined, number of variations must be at least equal to count of [[HeatBuffer#connections|connections]] defined in `heat_buffer`. When reactor is heated, corresponding variations are drawn over `connection_patches_disconnected`.

### lower_layer_picture
- **Type:** [[Sprite]]
- **Optional**

### heat_lower_layer_picture
- **Type:** [[Sprite]]
- **Optional**

### picture
- **Type:** [[Sprite]]
- **Optional**

### light
- **Type:** [[LightDefinition]]
- **Optional**

### meltdown_action
- **Type:** [[Trigger]]
- **Optional**
The action is triggered when the reactor dies (is destroyed) at over 90% of max temperature.

### neighbour_bonus
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### scale_energy_usage
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When this is true, the reactor will stop consuming fuel/energy when the temperature has reached the maximum.

### use_fuel_glow_color
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether the reactor should use [[ItemPrototype#fuel_glow_color|fuel_glow_color]] from the fuel item prototype as light color and tint for `working_light_picture`. [Forum post.](https://forums.factorio.com/71121)

### default_fuel_glow_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{1, 1, 1, 1} (white)`
When `use_fuel_glow_color` is true, this is the color used as `working_light_picture` tint for fuels that don't have glow color defined.

### temperature_to_suppress_energy_icons
- **Type:** [[double (type)]]
- **Optional**
The temperature above which energy icons are suppressed. Defaults to maximum double value.

### neighbour_connectable
- **Type:** [[NeighbourConnectable (type)]]
- **Optional**
Defines connection points to neighbours used to compute neighbour bonus.

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
- **Type:** [[CircuitConnectorDefinition]]
- **Optional**

### default_temperature_signal
- **Type:** [[SignalIDConnector]]
- **Optional**
