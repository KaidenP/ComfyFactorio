---
title: IconData
tags: [factorio-api, prototype, type]
---
# IconData

One layer of an icon. Icon layering follows the following rules:

- The rendering order of the individual icon layers follows the array order: Later added icon layers (higher index) are drawn on top of previously added icon layers (lower index).

- By default the first icon layer will draw an outline (or shadow in GUI), other layers will draw it only if they have `draw_background` explicitly set to `true`. There are caveats to this though. See [[IconData#draw_background|the doc]].

- When the final icon is displayed with transparency (e.g. a faded out alert), the icon layer overlap may look [undesirable](https://forums.factorio.com/viewtopic.php?p=575844#p575844).

- When the final icon is displayed with a shadow (e.g. an item on the ground or on a belt when item shadows are turned on), each icon layer will [cast a shadow](https://forums.factorio.com/84888) and the shadow is cast on the layer below it.

- The final icon will always be resized and centered in GUI so that all its layers (except the [[IconData#floating|floating]] ones) fit the target slot, but won't be resized when displayed on machines in alt-mode. For example: recipe first icon layer is size 128, scale 1, the icon group will be displayed at resolution /4 to fit the 32px GUI boxes, but will be displayed 4 times as large on buildings.

- Shift values are based on [[IconData#scale]].

The game automatically generates [icon mipmaps](https://factorio.com/blog/post/fff-291) for all icons. However, icons can have custom mipmaps defined. Custom mipmaps may help to achieve clearer icons at reduced size (e.g. when zooming out) than auto-generated mipmaps. If an icon file contains mipmaps then the game will automatically infer the icon's mipmap count. Icon files for custom mipmaps must contain half-size images with a geometric-ratio, for each mipmap level. Each next level is aligned to the upper-left corner, with no extra padding. Example sequence: `128x128@(0,0)`, `64x64@(128,0)`, `32x32@(192,0)` is three mipmaps.

## Properties

### icon
- **Type:** [[FileName]]
Path to the icon file.

### icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

### tint
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{r=1, g=1, b=1, a=1}`
The tint to apply to the icon.

### shift
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0, 0}`
Used to offset the icon "layer" from the overall icon. The shift is applied from the center (so negative shifts are left and up, respectively). Shift values are "in pixels" where the overall icon is assumed to be `expected_icon_size / 2` pixels in width and height, meaning shift `{0, expected_icon_size/2}` will shift it by entire icon height down.

### scale
- **Type:** [[double (type)]]
- **Optional**
Defaults to `(expected_icon_size / 2) / icon_size`.

Specifies the scale of the icon on the GUI scale. A scale of `2` means that the icon will be two times bigger on screen (and thus more pixelated).

Expected icon sizes:

- `512` for [[SpaceLocationPrototype#starmap_icon|SpaceLocationPrototype::starmap_icon]].

- `256` for [[TechnologyPrototype]].

- `128` for [[AchievementPrototype]] and [[ItemGroup]].

- `32` for [[ShortcutPrototype#icons|ShortcutPrototype::icons]] and `24` for [[ShortcutPrototype#small_icons|ShortcutPrototype::small_icons]].

- `64` for the rest of the prototypes that use icons.

### draw_background
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true` for the first layer, `false` otherwise
Outline is drawn using signed distance field generated on load. One icon image will have only one SDF generated. That means if the image is used in multiple icons with different scales, the outline width won't match the desired width in all the scales except the largest one.

### floating
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When `true` the layer is not considered for calculating bounds of the icon, so it can go out of bounds of rectangle into which the icon is drawn in GUI.

## Examples

```
-- one icon layer
{
  icon = "__base__/graphics/icons/fluid/heavy-oil.png",
  icon_size = 64,
  scale = 0.5,
  shift = {4, -8}
}
```

```
-- Layered icon, with size defined per layer
icons =
{
  {
    icon = "__base__/graphics/icons/fluid/barreling/barrel-empty.png",
    icon_size = 32
  },
  {
    icon = "__base__/graphics/icons/fluid/barreling/barrel-empty-side-mask.png",
    icon_size = 32,
    tint = { a = 0.75, b = 0, g = 0, r = 0 }
  },
  {
    icon = "__base__/graphics/icons/fluid/barreling/barrel-empty-top-mask.png",
    icon_size = 32,
    tint = { a = 0.75, b = 0.5, g = 0.5, r = 0.5 }
  },
  {
    icon = "__base__/graphics/icons/fluid/crude-oil.png",
    icon_size = 32,
    scale = 0.5,
    shift = {7, 8}
  }
}
```
