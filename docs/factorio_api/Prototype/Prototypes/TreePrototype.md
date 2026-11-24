---
title: TreePrototype
tags: [factorio-api, prototype]
---
# TreePrototype

> **Parent:** [[EntityWithHealthPrototype]] · **Type name:** `tree`

A [tree](https://wiki.factorio.com/Tree).

## Properties

### variation_weights
- **Type:** array<[[float (type)]]>
- **Optional**

### darkness_of_burnt_tree
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.5`

### pictures
- **Type:** [[SpriteVariations]]
- **Optional**
Mandatory if `variations` is not defined.

### variations
- **Type:** array<[[TreeVariation]]>
- **Optional**
If defined, it can't be empty.

### colors
- **Type:** array<[[Color (type)]]>
- **Optional**
Mandatory if `variations` is defined. Can't be empty.

### stateless_visualisation_variations
- **Type:** array<[[StatelessVisualisation]] | array<[[StatelessVisualisation]]>>
- **Optional**

### healing_per_tick
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.001666`
- **Overrides parent**
The amount of health automatically regenerated.
**Examples:**

```
healing_per_tick = 0.01
```
