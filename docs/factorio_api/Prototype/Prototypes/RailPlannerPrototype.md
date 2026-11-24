---
title: RailPlannerPrototype
tags: [factorio-api, prototype]
---
# RailPlannerPrototype

> **Parent:** [[ItemPrototype]] · **Type name:** `rail-planner`

A [rail planner](https://wiki.factorio.com/Rail_planner).

## Properties

### rails
- **Type:** array<[[EntityID (type)]]>
May not be an empty array. Entities must be rails.

### support
- **Type:** [[EntityID (type)]]
- **Optional**
Name of a rail support.

### manual_length_limit
- **Type:** [[double (type)]]
- **Optional**
- **Default:** 8 * 2 + 1.41 + 0.5
