---
title: BoundingBox
tags: [factorio-api, prototype, type]
---
# BoundingBox

*Note: `BoundingBox (type)`.*

BoundingBoxes are typically centered around the position of an entity.

BoundingBoxes are usually specified with the short-hand notation of passing an array of exactly 2 or 3 items.

The first tuple item is left_top, the second tuple item is right_bottom. The third tuple item is a [[float (type)|float]] that represents the orientation.

Positive x goes towards east, positive y goes towards south. This means that the upper-left point is the least dimension in x and y, and lower-right is the greatest.

## Type

struct | ([[MapPosition (type)]], [[MapPosition (type)]]) | ([[MapPosition (type)]], [[MapPosition (type)]], [[RealOrientation (type)]])

## Properties

### left_top
- **Type:** [[MapPosition (type)]]

### right_bottom
- **Type:** [[MapPosition (type)]]

### orientation
- **Type:** [[RealOrientation (type)]]
- **Optional**

## Examples

```
{{-0.4, -0.4}, {0.4, 0.4}}
```

```
-- long definition
{left_top = {x = -2, y = -3}, right_bottom = {x = 5, y = 8}}
```
