---
title: NamedNoiseFunction
tags: [factorio-api, prototype]
---
# NamedNoiseFunction

> **Parent:** [[Prototype]] · **Type name:** `noise-function`

Named noise functions are defined in the same way as [[NamedNoiseExpression]] except that they also have parameters.

Named noise functions are available to be used in [[NoiseExpression|NoiseExpressions]].

## Properties

### parameters
- **Type:** array<[[string (type)]]>
The order of the parameters matters because functions can also be called with positional arguments.

A function can't have more than 255 parameters.

### expression
- **Type:** [[NoiseExpression]]

### local_expressions
- **Type:** dictionary<[[string (type)]] → [[NoiseExpression]]>
- **Optional**
A map of expression name to expression.

Local expressions are meant to store data locally similar to local variables in Lua. Their purpose is to hold noise expressions used multiple times in the named noise expression, or just to tell the reader that the local expression has a specific purpose. Local expressions can access other local definitions and also function parameters, but recursive definitions aren't supported.

### local_functions
- **Type:** dictionary<[[string (type)]] → [[NoiseFunction]]>
- **Optional**
A map of function name to function.

Local functions serve the same purpose as local expressions - they aren't visible outside of the specific prototype and they have access to other local definitions.

## Example

```
{
  type = "noise-function",
  name = "random_between",
  parameters = {"from", "to"},
  expression = "random_penalty{x = x, y = y, source = to, amplitude = to - from}"
}
```

```
{
  type = "noise-function",
  name = "finish_elevation",
  parameters = {"elevation", "segmentation_multiplier"},
  expression = "min((elevation - water_level) / segmentation_multiplier, <more stuff>, starting_lake_distance / 16 + starting_lake_noise / 2)",
  local_expressions =
  {
    starting_lake_distance = "distance_from_nearest_point{x = x, y = y, points = starting_lake_positions, maximum_distance = 1024}",
    starting_lake_noise = "quick_multioctave_noise_persistence{<more stuff>}"
  }
}
```
