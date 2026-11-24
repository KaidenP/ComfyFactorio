---
title: GeneratorPrototype
tags: [factorio-api, prototype]
---
# GeneratorPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `generator`

An entity that produces power from fluids, for example a [steam engine](https://wiki.factorio.com/Steam_engine).

## Properties

### energy_source
- **Type:** [[ElectricEnergySource]]

### fluid_box
- **Type:** [[FluidBox]]
This must have a filter if `max_power_output` is not defined.

### output_fluid_box
- **Type:** [[FluidBox]]
- **Optional**

### pictures
- **Type:** [[GeneratorPictureSet]]
- **Optional**

### effectivity
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
How much energy the generator produces compared to how much energy it consumes. For example, an effectivity of 0.5 means that half of the consumed energy is output as power.

### fluid_usage_per_tick
- **Type:** [[FluidAmount (type)]]
The number of fluid units the generator uses per tick.

### maximum_temperature
- **Type:** [[float (type)]]
The maximum temperature to which the efficiency can increase. At this temperature the generator will run at 100% efficiency. Note: Higher temperature fluid can still be consumed.

Used to calculate the `max_power_output` if it is not defined and `burns_fluid` is false. Then, the max power output is `(min(fluid_max_temp, maximum_temperature) - fluid_default_temp) × fluid_usage_per_tick × fluid_heat_capacity × effectivity`, the fluid is the filter specified on the `fluid_box`.

### minimum_input_temperature
- **Type:** [[float (type)]]
- **Optional**
If specified, an input fluid below this temperature will cause the generator to stop working.

### maximum_input_temperature
- **Type:** [[float (type)]]
- **Optional**
If specified, an input fluid above this temperature will cause the generator to stop working.

### smoke
- **Type:** array<[[SmokeSource (type)]]>
- **Optional**

### burns_fluid
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If set to `true`, the available power output is based on the [[FluidPrototype#fuel_value|FluidPrototype::fuel_value]]. Otherwise, the available power output will be based on the fluid temperature and [[FluidPrototype#heat_capacity|FluidPrototype::heat_capacity]]: `energy = fluid_amount * (fluid_temperature - fluid_default_temperature) * fluid_heat_capacity * effectivity`

### scale_fluid_usage
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Scales the generator's fluid usage to its maximum power output.

Setting this to `true` prevents the generator from overconsuming fluid, for example when higher than `maximum_temperature` fluid is fed to the generator.

If scale_fluid_usage is false, the generator consumes the full `fluid_usage_per_tick` and any of the extra energy in the fluid (in the form of higher temperature) is wasted. The [steam engine](https://wiki.factorio.com/Steam_engine) exhibits this behavior when fed steam from [heat exchangers](https://wiki.factorio.com/Heat_exchanger).

### destroy_non_fuel_fluid
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
This property is used when `burns_fluid` is true and the fluid has a [[FluidPrototype#fuel_value|fuel_value]] of 0.

This property is also used when `burns_fluid` is false and the fluid is at default temperature.

In these cases, this property determines whether the fluid should be destroyed, meaning that the fluid is consumed at the rate of `fluid_usage_per_tick`, without producing any power.

### two_direction_only
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### perceived_performance
- **Type:** [[PerceivedPerformance (type)]]
- **Optional**
Affects animation speed and working sound.

### max_power_output
- **Type:** [[Energy]]
- **Optional**
The power production of the generator is capped to this value. This is also the value that is shown as the maximum power output in the tooltip of the generator.

`fluid_box` must have a filter if this is not defined.

### spent_fluid
- **Type:** [[SpentFluidSpecification (type)]]
- **Optional**
Fluid and amount produced per 1 unit of fluid consumed. Only used when `output_fluid_box` is defined. If this value is not provided, [[FluidPrototype#spent_fluid|FluidPrototype::spent_fluid]] will be used based on the input fluid being consumed.
