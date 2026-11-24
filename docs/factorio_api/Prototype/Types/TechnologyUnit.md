---
title: TechnologyUnit
tags: [factorio-api, prototype, type]
---
# TechnologyUnit

Either `count` or `count_formula` must be defined, never both.

## Properties

### count
- **Type:** [[uint64 (type)]]
- **Optional**
How many units are needed. Must be `> 0`.

### count_formula
- **Type:** [[MathExpression (type)]]
- **Optional**
Formula that specifies how many units are needed per level of the technology.

If the last characters of the prototype name are `-<number>`, the level is taken to be the number, e.g. `physical-projectile-damage-2` implies a number of `2`. This defaults to `1`. There does not need to be lower-level technologies for a technology to be detected as having a level, meaning a technology or sequence of upgrade technologies can begin at any number.

For an infinite technology, the level begins at the given suffix (or `1` by default) and gains 1 level upon being researched, or if the `max_level` is reached, marked as completed. The initial level of a technology can not be greater than its `max_level`.

`l` and `L` are provided as variables in the expression, they represent the current level of the technology.

This formula can also be used at [[LuaHelpers#evaluate_expression|runtime]].
**Examples:**

```
count_formula = "2500*(L - 3)"
```

### time
- **Type:** [[double (type)]]
How much time one unit takes to research. In a lab with a crafting speed of `1`, it corresponds to the number of seconds.

### ingredients
- **Type:** array<[[ResearchIngredient (type)]]>
List of ingredients needed for one unit of research.

## Examples

```
unit =
{
  count_formula = "2^(L-6)*1000",
  ingredients =
  {
    {"automation-science-pack", 1},
    {"logistic-science-pack", 1},
    {"chemical-science-pack", 1},
    {"production-science-pack", 1},
    {"utility-science-pack", 1},
    {"space-science-pack", 1}
  },
  time = 60
}
```
