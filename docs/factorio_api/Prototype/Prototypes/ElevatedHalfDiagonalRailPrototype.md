---
title: ElevatedHalfDiagonalRailPrototype
tags: [factorio-api, prototype]
---
# ElevatedHalfDiagonalRailPrototype

> **Parent:** [[HalfDiagonalRailPrototype]] · **Type name:** `elevated-half-diagonal-rail`

An elevated half diagonal rail.

## Properties

### name
- **Type:** [[string (type)]]
- **Overrides parent**
Unique textual identification of the prototype. May only contain alphanumeric characters, dashes and underscores. May not exceed a length of 200 characters.

Requires Space Age to create prototypes with name not starting with `dummy-`. Dummy prototypes cannot be built.

### tall
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
When this is true, this entity prototype will be translucent and unselectable when "Hide tall entities" mode is active.

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `55`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.
