---
title: ArrowPrototype
tags: [factorio-api, prototype]
---
# ArrowPrototype

> **Parent:** [[EntityPrototype]] · **Type name:** `arrow`

The arrows used for example in the campaign, they are literally just arrows.

## Properties

### arrow_picture
- **Type:** [[Sprite]]

### circle_picture
- **Type:** [[Sprite]]
- **Optional**

### blinking
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `20`
- **Overrides parent**
The entity with the higher number is selectable before the entity with the lower number.

The value `0` will be treated the same as `nil`.

## Example

```
{
  type = "arrow",
  name = "orange-arrow-with-circle",
  flags = { "placeable-off-grid", "not-on-map" },
  blinking = true,
  arrow_picture =
  {
    filename = "__core__/graphics/arrows/gui-arrow-medium.png",
    priority = "low",
    width = 58,
    height = 62
  },
  circle_picture =
  {
    filename = "__core__/graphics/arrows/gui-arrow-circle.png",
    priority = "low",
    width = 50,
    height = 50
  }
}
```
