---
title: EquipmentPosition
tags: [factorio-api, runtime, concept]
---
# EquipmentPosition

Position inside an equipment grid. This uses the same format as [[MapPosition]], meaning it can be specified either with or without explicit keys.

## Type

table | ([[int32]], [[int32]])

## Examples

```
-- Explicit definition
{x = 5, y = 2}
{y = 2, x = 5}
```

```
-- Shorthand
{1, 2}
```
