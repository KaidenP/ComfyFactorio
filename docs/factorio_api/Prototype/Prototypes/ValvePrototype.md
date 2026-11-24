---
title: ValvePrototype
tags: [factorio-api, prototype]
---
# ValvePrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `valve`

A passive device that provides limited control of fluid flow between pipelines.

## Properties

### mode
- **Type:** [[ValveMode (type)]]

### threshold
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Ignored if [[ValvePrototype#mode|ValvePrototype::mode]] is `"one-way"`. Must be between `0` and `1` inclusive.

### fluid_box
- **Type:** [[FluidBox]]
Must have at least one `"output"` [[FluidFlowDirection (type)|FluidFlowDirection]] and at least one `"input-output"` [[FluidFlowDirection (type)|FluidFlowDirection]].

### flow_rate
- **Type:** [[FluidAmount (type)]]
The max flow rate through the valve per tick.

### animations
- **Type:** [[Animation4Way]]
- **Optional**

### frozen_patch
- **Type:** [[Sprite4Way]]
- **Optional**
