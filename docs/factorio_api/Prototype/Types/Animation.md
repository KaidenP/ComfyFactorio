---
title: Animation
tags: [factorio-api, prototype, type]
---
# Animation

> **Parent:** [[AnimationParameters]]

Specifies an animation that can be used in the game.

Note that if any frame of the animation is specified from the same source as any other [[Sprite]] or frame of other animation, it will be shared.

## Properties

### layers
- **Type:** array<[[Animation]]>
- **Optional**
If this property is present, all Animation definitions have to be placed as entries in the array, and they will all be loaded from there. `layers` may not be an empty table. Each definition in the array may also have the `layers` property.

`animation_speed` and `max_advance` of the first layer are used for all layers. All layers will run at the same speed.

If this property is present, all other properties, including those inherited from AnimationParameters, are ignored.

### filename
- **Type:** [[FileName]]
- **Optional**
- **Overrides parent**
Only loaded if `layers` is not defined. Mandatory if neither `stripes` nor `filenames` are defined.

The path to the sprite file to use.

### stripes
- **Type:** array<[[Stripe]]>
- **Optional**
Only loaded if `layers` is not defined.

### filenames
- **Type:** array<[[FileName]]>
- **Optional**
Only loaded if neither `layers` nor `stripes` are defined.

### slice
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** Value of `frame_count`
Only loaded if `layers` is not defined and if `filenames` is defined.

### lines_per_file
- **Type:** [[uint32 (type)]]
- **Optional**
Only loaded if `layers` is not defined. Mandatory if `filenames` is defined.

## Examples

```
-- simple animation
horizontal_animation =
{
  filename = "__base__/graphics/entity/steam-engine/steam-engine-H.png",
  width = 352,
  height = 257,
  frame_count = 32,
  line_length = 8,
  shift = {0.03125, -0.1484375}
}
```

```
-- animation with layers
horizontal_animation =
{
  layers =
  {
    {
      filename = "__base__/graphics/entity/steam-engine/steam-engine-H.png",
      width = 352,
      height = 257,
      frame_count = 32,
      line_length = 8,
      shift = {0.03125, -0.15625}
    },
    {
      filename = "__base__/graphics/entity/steam-engine/steam-engine-H-shadow.png",
      width = 508,
      height = 160,
      frame_count = 32,
      line_length = 8,
      draw_as_shadow = true,
      shift = {1.5, 0.75}
    }
  }
}
```
