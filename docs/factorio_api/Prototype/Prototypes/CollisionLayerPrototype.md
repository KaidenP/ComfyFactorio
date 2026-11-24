---
title: CollisionLayerPrototype
tags: [factorio-api, prototype]
---
# CollisionLayerPrototype

> **Parent:** [[Prototype]] · **Type name:** `collision-layer` · **Instance limit:** 256

A collision layer. Used for [[CollisionMaskConnector|collision masks]].

It's recommend to use underscores instead of dashes in `name` so that the name can easily be used as a table key when defining collision masks.

## Example

```
{
  type = "collision-layer",
  name = "is_lower_object"
}
```
