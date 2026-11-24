---
title: FluidEnergySource
tags: [factorio-api, prototype, type]
---
# FluidEnergySource

> **Parent:** [[BaseEnergySource]]

## Properties

### type
- **Type:** `"fluid"`

### fluid_box
- **Type:** [[FluidBox]]
All standard fluid box configurations are acceptable, but the type must be `"input"` or `"input-output"` to function correctly. `scale_fluid_usage = true`, `fluid_usage_per_tick`, or a filter on the fluidbox must be set to be able to calculate the fluid usage of the energy source.

### output_fluid_box
- **Type:** [[FluidBox]]
- **Optional**

### smoke
- **Type:** array<[[SmokeSource (type)]]>
- **Optional**

### light_flicker
- **Type:** [[LightFlickeringDefinition]]
- **Optional**

### effectivity
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
`1` means 100% effectivity. Must be greater than `0`.

How much energy the fluid energy source produces compared to how much energy it consumes. For example, an effectivity of 0.5

### burns_fluid
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If set to `true`, the available power output is based on the [[FluidPrototype#fuel_value|FluidPrototype::fuel_value]]. Otherwise, the available power output will be based on the fluid temperature and [[FluidPrototype#heat_capacity|FluidPrototype::heat_capacity]]: `energy = fluid_amount * (fluid_temperature - fluid_default_temperature) * fluid_heat_capacity * effectivity`

### scale_fluid_usage
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Scales the energy source's fluid usage to its maximum power output.

If this is `false` the energy source will overconsume fluid. For example when higher than `maximum_temperature` fluid is fed to the energy source, it will consume the full `fluid_usage_per_tick` and any of the extra energy in the fluid (in the form of higher temperature) is wasted. Setting scale_fluid_usage to `true` prevents this behavior.

### destroy_non_fuel_fluid
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Property is only used when `burns_fluid` is `true` and the fluid has a [[FluidPrototype#fuel_value|fuel_value]] of `0`, or when `burns_fluid` is `false` and the fluid is at its `default_temperature`.

In those cases, this property determines whether the fluid should be destroyed, meaning that the fluid is consumed at the rate of `fluid_usage_per_tick`, without producing any power.

### hide_from_stats
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When set, fluids consumed and produced by this energy source will not appear in fluid production statistics.

### fluid_usage_per_tick
- **Type:** [[FluidAmount (type)]]
- **Optional**
- **Default:** `0`
The number of fluid units the energy source uses per tick. If used with `scale_fluid_usage`, this specifies the maximum. If this value is not set, `scale_energy_usage` is `false` and a fluid box filter is set, the game will attempt to calculate this value from the fluid box filter's fluid's `fuel_value` or `heat_capacity` and the entity's `energy_usage`. If `burns_fluid` is `false`, `maximum_temperature` will also be used. If the attempt of the game to calculate this value fails (`scale_energy_usage` is `false` and a fluid box filter is set), then `scale_energy_usage` will be forced to `true`, to prevent the energy source from being an infinite fluid sink. More context [on the forums](https://forums.factorio.com/90613).

### maximum_temperature
- **Type:** [[float (type)]]
- **Optional**
If this is specified while `scale_fluid_usage` is `false` and `fluid_usage_per_tick` is not specified, the game will use this value to calculate `fluid_usage_per_tick`. To do that, the filter on the `fluid_box` must be set.

Only loaded if `burns_fluid` is `false`.

### minimum_input_temperature
- **Type:** [[float (type)]]
- **Optional**
If specified, an input fluid below this temperature will cause the fluid energy source to stop working.

### maximum_input_temperature
- **Type:** [[float (type)]]
- **Optional**
If specified, an input fluid above this temperature will cause the fluid energy source to stop working.

### spent_fluid
- **Type:** [[SpentFluidSpecification (type)]]
- **Optional**
Fluid and amount produced per 1 unit of fluid consumed. Only used when `output_fluid_box` is defined. If this value is not provided, [[FluidPrototype#spent_fluid|FluidPrototype::spent_fluid]] will be used based on the input fluid being consumed.
