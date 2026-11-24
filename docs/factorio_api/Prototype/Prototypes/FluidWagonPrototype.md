---
title: FluidWagonPrototype
tags: [factorio-api, prototype]
---
# FluidWagonPrototype

> **Parent:** [[RollingStockPrototype]] · **Type name:** `fluid-wagon`

A [fluid wagon](https://wiki.factorio.com/Fluid_wagon).

## Properties

### capacity
- **Type:** [[FluidAmount (type)]]

### quality_affects_capacity
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### tank_count
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `3`
Must be positive.

### tank_spacing
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `2.0`
Must be > 0.1.

### base_valve_z_offset_projected_when_horizontal
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `-1.375`
Projected height of valves when the wagon is oriented east/west.

### base_valve_z_offset_projected_when_vertical
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `-0.65`
Projected height of valves when the wagon is oriented north/south.

### connection_category
- **Type:** [[string (type)]] | array<[[string (type)]]>
- **Optional**
- **Default:** `"default"`
Pumps are only allowed to connect to this fluid wagon if the pump's [[PipeConnectionDefinition (type)|fluid box connection]] and this fluid wagon share a connection category. Pump may have different connection categories on the input and output side, connection categories will be taken from the connection that is facing towards fluid wagon.

### valve_to_valve_offset_when_horizontal
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{2, 0}`
Projected offset between valves when the wagon is oriented east/west.

For all directions, the elliptical interpolation for the offset is performed based on both `valve_to_valve_offset_when_horizontal` and `valve_to_valve_offset_when_vertical` and the tangential and normal are calculated separately.

The tangential component of the offset is interpolated from values `valve_to_valve_offset_when_horizontal.x` and `valve_to_valve_offset_when_vertical.y`. The normal component of the offset is interpolated from values `valve_to_valve_offset_when_vertical.x` and `valve_to_valve_offset_when_horizontal.y`.

Interpolating the components with one value non-zero and the other zero would produce undesirable behaviour and is therefore not allowed.

### valve_to_valve_offset_when_vertical
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0, 1.775}`
Projected offset between valves when the wagon is oriented north/south.

See `valve_to_valve_offset_when_horizontal` for how this value is used in the offset calculation.

### base_valve_xy_offset_when_horizontal
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0, 0}`
Horizontal (xy) offset of the central valve from the wagon position when it is oriented east/west.

For all directions, the elliptical interpolation for the offset is performed based on both `base_valve_xy_offset_when_horizontal` and `base_valve_xy_offset_when_vertical` and the tangential and normal are calculated separately.

The tangential component of the offset is interpolated from values `base_valve_xy_offset_when_horizontal.x` and `base_valve_xy_offset_when_vertical.y`. The normal component of the offset is interpolated from values `base_valve_xy_offset_when_vertical.x` and `base_valve_xy_offset_when_horizontal.y`.

Interpolating the components with one value non-zero and the other zero would produce undesirable behaviour and is therefore not allowed.

### base_valve_xy_offset_when_vertical
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0, 0}`
Horizontal (xy) offset of the central valve from the wagon position when it is oriented north/south.

See `base_valve_xy_offset_when_horizontal` for how this value is used in the offset calculation.
