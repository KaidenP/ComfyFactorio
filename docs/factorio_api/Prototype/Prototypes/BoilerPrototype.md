---
title: BoilerPrototype
tags: [factorio-api, prototype]
---
# BoilerPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `boiler`

A [boiler](https://wiki.factorio.com/Boiler). It heats fluid and optionally outputs it as a different fluid.

## Properties

### pictures
- **Type:** [[BoilerPictureSet]]
- **Optional**

### energy_source
- **Type:** [[EnergySource]]

### fluid_box
- **Type:** [[FluidBox]]
The input fluid box.

If `mode` is `"heat-fluid-inside"`, the fluid is heated up directly in this fluidbox.

### output_fluid_box
- **Type:** [[FluidBox]]
The output fluid box.

If `mode` is `"output-to-separate-pipe"` and this has a [[FluidBox#filter|filter]], the heated input fluid is converted to the output fluid that is set in the filter. The conversion ratio is based on the [[FluidPrototype#heat_capacity|heat capacity]] of the fluids: `output_fluid_amount = input_fluid_amount * (input_fluid_heat_capacity / output_fluid_heat_capacity)`

If `mode` is `"heat-fluid-inside"`, this fluidbox is unused.

### energy_consumption
- **Type:** [[Energy]]

### burning_cooldown
- **Type:** [[uint16 (type)]]
Controls for how many ticks the boiler will show the fire and fire_glow after the energy source runs out of energy.

Note that `fire` and `fire_glow` alpha is set to the light intensity of the energy source, so 0 light intensity means the fire is invisible. For burner energy sources, the light intensity will reach zero rather quickly after the boiler runs out of fuel, effectively capping the time that `fire` and `fire_glow` will be shown after the boiler runs out of fuel.

### target_temperature
- **Type:** [[float (type)]]
- **Optional**
Only loaded, and mandatory if `mode` is `"output-to-separate-pipe"`. The boiler heats the input fluid to exactly this temperature and moves the fluid to the output fluid box. An input fluid above this temperature will cause the boiler to stop working.

### minimum_input_temperature
- **Type:** [[float (type)]]
- **Optional**
If specified, an input fluid below this temperature will cause the boiler to stop working.

### maximum_input_temperature
- **Type:** [[float (type)]]
- **Optional**
If specified, an input fluid above this temperature will cause the boiler to stop working. This can be lower than the `target_temperature` for heating the fluid.

### fire_glow_flicker_enabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this is set to false, `fire_glow` alpha is always 1 instead of being controlled by the light intensity of the energy source.

### fire_flicker_enabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this is set to false, `fire` alpha is always 1 instead of being controlled by the light intensity of the energy source.

### mode
- **Type:** `"heat-fluid-inside"` | `"output-to-separate-pipe"`
- **Optional**
- **Default:** `"heat-fluid-inside"`
In the `"output-to-separate-pipe"` mode, fluid is transferred from the `fluid_box` to the `output_fluid_box` when enough energy is available to [[FluidPrototype#heat_capacity|heat]] the input fluid to the `target_temperature`. Setting a filter on the `output_fluid_box` means that instead of the heated input fluid getting moved to the output, it is converted to the filtered fluid in a ratio based on the heat capacity of the fluids: `output_fluid_amount = input_fluid_amount * (input_fluid_heat_capacity / output_fluid_heat_capacity)`

In the `"heat-fluid-inside"` mode, fluid in the `fluid_box` is continuously heated from the input temperature up to its [[FluidPrototype#max_temperature|FluidPrototype::max_temperature]].

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
