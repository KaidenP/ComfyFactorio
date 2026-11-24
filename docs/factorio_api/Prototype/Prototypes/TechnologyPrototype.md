---
title: TechnologyPrototype
tags: [factorio-api, prototype]
---
# TechnologyPrototype

> **Parent:** [[Prototype]] · **Type name:** `technology`

A [technology](https://wiki.factorio.com/Technologies).

## Properties

### name
- **Type:** [[string (type)]]
- **Overrides parent**
If this name ends with `-<number>`, that number is ignored for localization purposes. E.g. if the name is `technology-3`, the game looks for the `technology-name.technology` localization. The technology tree will also show the number on the technology icon.

The number is considered the level of the technology. There can't be technologies with noncontiguous levels, e.g. `technology-1` and `technology-3` without `technology-2` will cause a startup error.

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

The base game uses 256px icons for technologies.

Only loaded if `icons` is not defined.

### upgrade
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When set to true, and the technology contains several levels, only the relevant one is displayed in the technology screen.
**Examples:**

```
{
  type = "technology",
  name = "physical-projectile-damage-2",
  [...]
  upgrade = true
}
```

### enabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
This can be `false` to disable the technology at the start of the game, or `true` to leave it enabled.

Changes to this property do not affect existing save files, as the enabled state is saved in the save file and not reloaded from the prototype.

### essential
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether the technology should be shown in the technology tree GUI when "Show only essential technologies" is enabled.

### visible_when_disabled
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Controls whether the technology is shown in the tech GUI when it is not `enabled`.

Changes to this property do not affect existing save files, as the visible_when_disabled state is saved in the save file and not reloaded from the prototype.

### ignore_tech_cost_multiplier
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Controls whether the technology cost ignores the tech cost multiplier set in the [[DifficultySettings]]. E.g. `4` for the default expensive difficulty.

### allows_productivity
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### research_trigger
- **Type:** [[TechnologyTrigger]]
- **Optional**
Mandatory if `unit` is not defined.

### unit
- **Type:** [[TechnologyUnit]]
- **Optional**
Determines the cost in items and time of the technology.

Mandatory if `research_trigger` is not defined.

### max_level
- **Type:** [[uint32 (type)]] | `"infinite"`
- **Optional**
`"infinite"` for infinite technologies, otherwise `uint32`.

Defaults to the same level as the technology, which is `0` for non-upgrades, and the level of the upgrade for upgrades.

### prerequisites
- **Type:** array<[[TechnologyID (type)]]>
- **Optional**
List of technologies needed to be researched before this one can be researched.
**Examples:**

```
prerequisites = {"explosives", "military-2"}
```

### show_levels_info
- **Type:** [[boolean (type)]]
- **Optional**
Can be used to enable or disable showing levels info in technology slot.

### effects
- **Type:** array<[[Modifier]]>
- **Optional**
List of effects of the technology (applied when the technology is researched).
**Examples:**

```
{
  {
    type  = "unlock-recipe",
    recipe = "land-mine"
  }
}
```

### hidden
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**
Hides the technology from the tech screen.

## Example

```
{
  type = "technology",
  name = "steel-processing",
  icon_size = 256,
  icon = "__base__/graphics/technology/steel-processing.png",
  effects =
  {
    {
      type = "unlock-recipe",
      recipe = "steel-plate"
    },
    {
      type = "unlock-recipe",
      recipe = "steel-chest"
    }
  },
  unit =
  {
    count = 50,
    ingredients = {{"automation-science-pack", 1}},
    time = 5
  },
  order = "c-a"
}
```
