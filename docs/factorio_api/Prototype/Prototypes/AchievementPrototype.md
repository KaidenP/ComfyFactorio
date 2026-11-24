---
title: AchievementPrototype
tags: [factorio-api, prototype]
---
# AchievementPrototype

> **Parent:** [[Prototype]] · **Type name:** `achievement`

This prototype definition is used for the in-game achievements.

## Properties

### icons
- **Type:** array<[[IconData]]>
- **Optional**
Can't be an empty array.

### icon
- **Type:** [[FileName]]
- **Optional**
Path to the icon file.

Only loaded, and mandatory if `icons` is not defined.

### icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

The base game uses 128px icons for achievements.

Only loaded if `icons` is not defined.

### steam_stats_name
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `""`
Unusable by mods, as this refers to unlocking the achievement through Steam.

### allowed_without_fight
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If this is set to `false`, it is not possible to complete the achievement on the peaceful difficulty setting or when the enemy base generation settings have been changed.

## Example

```
{
  type = "achievement",
  name = "so-long-and-thanks-for-all-the-fish",
  order = "g[secret]-a[so-long-and-thanks-for-all-the-fish]",
  icon = "__base__/graphics/achievement/so-long-and-thanks-for-all-the-fish.png",
  icon_size = 128
}
```
