---
title: FusionGeneratorPrototype
tags: [factorio-api, prototype]
---
# FusionGeneratorPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `fusion-generator`

Consumes a fluid to generate electricity and create another fluid.

## Properties

### energy_source
- **Type:** [[ElectricEnergySource]]
`output_flow_limit` is mandatory and must be positive. `output_flow_limit` is the maximum power output of the generator.

### graphics_set
- **Type:** [[FusionGeneratorGraphicsSet]]
- **Optional**

### input_fluid_box
- **Type:** [[FluidBox]]
[[FluidBox#filter|filter]] is mandatory. The temperature (or fuel value if `burns_fluid` is true) of this fluid is used to calculate the available power output.

### output_fluid_box
- **Type:** [[FluidBox]]
[[FluidBox#filter|filter]] is mandatory.

### max_fluid_usage
- **Type:** [[FluidAmount (type)]]
Must be positive.

### perceived_performance
- **Type:** [[PerceivedPerformance (type)]]
- **Optional**
Affects animation speed and working sound.

### burns_fluid
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If set to `true`, the available power output is based on the [[FluidPrototype#fuel_value|FluidPrototype::fuel_value]]. Otherwise, the available power output will be based on the fluid temperature and [[FluidPrototype#heat_capacity|FluidPrototype::heat_capacity]]: `energy = fluid_amount * fluid_temperature * fluid_heat_capacity * effectivity`

### effectivity
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
`1` means 100% effectivity. Must be greater than `0`. Multiplier of the energy output.

### minimum_input_temperature
- **Type:** [[float (type)]]
- **Optional**
If specified, an input fluid below this temperature will cause the fusion generator to stop working.

### maximum_input_temperature
- **Type:** [[float (type)]]
- **Optional**
If specified, an input fluid above this temperature will cause the fusion generator to stop working.
