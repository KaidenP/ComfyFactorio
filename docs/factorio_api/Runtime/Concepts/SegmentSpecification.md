---
title: SegmentSpecification
tags: [factorio-api, runtime, concept]
---
# SegmentSpecification

A runtime representation of [[SegmentSpecification (type)|SegmentSpecification]].

## Fields

### segment
- **Type:** [[LuaEntityPrototype]]
The [[SegmentPrototype]] at this position in the unit.

### distance_from_head
- **Type:** [[double]]
The distance (in tiles) along the unit's body between this segment's center and the head [[SegmentedUnitPrototype]]'s center. This value is automatically pre-calculated after the prototype phase.
