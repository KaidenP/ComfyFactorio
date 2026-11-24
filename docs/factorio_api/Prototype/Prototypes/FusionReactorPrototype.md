---
title: FusionReactorPrototype
tags: [factorio-api, prototype]
---
# FusionReactorPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `fusion-reactor`

Fusion reactor. Consumes fluid, fuel and additional energy to produce other fluid. Kind of advanced boiler. Can also have neighbour bonus.

## Properties

### energy_source
- **Type:** [[ElectricEnergySource]]
First energy source for the process: provides energy

### burner
- **Type:** [[BurnerEnergySource]]
Second energy source for the process: provides fuel

### graphics_set
- **Type:** [[FusionReactorGraphicsSet]]

### input_fluid_box
- **Type:** [[FluidBox]]
The input fluid box.

[[FluidBox#filter|filter]] is mandatory.

### output_fluid_box
- **Type:** [[FluidBox]]
The output fluid box.

[[FluidBox#filter|filter]] is mandatory.

### neighbour_connectable
- **Type:** [[NeighbourConnectable (type)]]
- **Optional**
Defines connection points to neighbours used to compute neighbour bonus.

### two_direction_only
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If set to true, only North and East direction will be buildable.

### neighbour_bonus
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### power_input
- **Type:** [[Energy]]
Power input consumed from first energy source at full performance.

Cannot be negative.

### max_fluid_usage
- **Type:** [[FluidAmount (type)]]
Maximum amount of fluid converted from `input_fluid_box` to `output_fluid_box` within a single tick.

Must be positive.

### minimum_input_temperature
- **Type:** [[float (type)]]
- **Optional**
If specified, an input fluid below this temperature will cause the fusion reactor to stop working.

### maximum_input_temperature
- **Type:** [[float (type)]]
- **Optional**
If specified, an input fluid above this temperature will cause the fusion reactor to stop working.

### target_temperature
- **Type:** [[float (type)]]
- **Optional**
The temperature of the fluid to output. If not defined, the default temperature of the output fluid will be used.

### perceived_performance
- **Type:** [[PerceivedPerformance (type)]]
- **Optional**
Affects working sound.
