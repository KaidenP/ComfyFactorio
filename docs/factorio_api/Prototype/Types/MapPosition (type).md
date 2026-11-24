---
title: MapPosition
tags: [factorio-api, prototype, type]
---
# MapPosition

*Note: `MapPosition (type)`.*

Coordinates of a tile in a map. Positive x goes towards east, positive y goes towards south, and x is the first dimension in the array format.

The coordinates are stored as a fixed-size 32 bit integer, with 8 bits reserved for decimal precision, meaning the smallest value step is `1/2^8 = 0.00390625` tiles.

## Type

struct | ([[double (type)]], [[double (type)]])

## Properties

### x
- **Type:** [[double (type)]]

### y
- **Type:** [[double (type)]]

## Examples

```
-- Explicit definition
{x = 5.5, y = 2}
{y = 2.25, x = 5.125}
```

```
-- Shorthand
{1.625, 2.375}
```
