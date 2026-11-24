---
title: ThrusterPrototype
tags: [factorio-api, prototype]
---
# ThrusterPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `thruster` · **Requires:** `space_age`

Consumes two fluids as fuel to produce thrust for a space platform.

## Properties

### min_performance
- **Type:** [[ThrusterPerformancePoint (type)]]

### max_performance
- **Type:** [[ThrusterPerformancePoint (type)]]
`max_performance.fluid_volume` must not be smaller than `min_performance.fluid_volume`.

### fuel_fluid_box
- **Type:** [[FluidBox]]
If a [[FluidBox#filter|filter]] is set for this fluidbox it determines what the thruster considers the first fuel.

### oxidizer_fluid_box
- **Type:** [[FluidBox]]
If a [[FluidBox#filter|filter]] is set for this fluidbox it determines what the thruster considers the second fuel.

### minimum_fuel_temperature
- **Type:** [[float (type)]]
- **Optional**
If specified, fuel fluid below this temperature will cause the thruster to stop working.

### maximum_fuel_temperature
- **Type:** [[float (type)]]
- **Optional**
If specified, fuel fluid above this temperature will cause the thruster to stop working.

### minimum_oxidizer_temperature
- **Type:** [[float (type)]]
- **Optional**
If specified, oxidizer fluid below this temperature will cause the thruster to stop working.

### maximum_oxidizer_temperature
- **Type:** [[float (type)]]
- **Optional**
If specified, oxidizer fluid above this temperature will cause the thruster to stop working.

### graphics_set
- **Type:** [[ThrusterGraphicsSet]]
- **Optional**

### plumes
- **Type:** [[PlumesSpecification]]
- **Optional**
