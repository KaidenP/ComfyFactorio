---
title: NamedNoiseExpression
tags: [factorio-api, prototype]
---
# NamedNoiseExpression

> **Parent:** [[Prototype]] · **Type name:** `noise-expression`

A [[NoiseExpression]] with a name. The base game uses named noise expressions to specify functions for many map properties to be used in map generation; e.g. the "elevation" expression is used to calculate elevation for every point on a map. For a list of the built-in named noise expressions, see [data.raw](https://wiki.factorio.com/Data.raw#noise-expression).

Named noise expressions can be used by [[MapGenSettings (type)|MapGenSettings]] and [[MapGenPreset (type)|MapGenPreset]] to override which named expression is used to calculate a given property by having an entry in `property_expression_names`, e.g. `elevation = "elevation_island"`.

Alternate expressions can be made available in the map generator GUI by setting their `intended_property` to the name of the property they should override.

Named noise expressions can also be used as [[noise-expressions|noise variables]] e.g. `var("my-noise-expression")`.

## Properties

### expression
- **Type:** [[NoiseExpression]]
The noise expression itself. This is where most of the noise magic happens.

### local_expressions
- **Type:** dictionary<[[string (type)]] → [[NoiseExpression]]>
- **Optional**
A map of expression name to expression.

Local expressions are meant to store data locally similar to local variables in Lua. Their purpose is to hold noise expressions used multiple times in the named noise expression, or just to tell the reader that the local expression has a specific purpose. Local expressions can access other local definitions, but recursive definitions aren't supported.

### local_functions
- **Type:** dictionary<[[string (type)]] → [[NoiseFunction]]>
- **Optional**
A map of function name to function.

Local functions serve the same purpose as local expressions - they aren't visible outside of the specific prototype and they have access to other local definitions.

### intended_property
- **Type:** [[string (type)]]
- **Optional**
Names the property that this expression is intended to provide a value for, if any. This will make the expression show up as an option in the map generator GUI, unless it is the only expression with that intended property, in which case it will be hidden and selected by default.

For example if a noise expression is intended to be used as an alternative temperature generator, `intended_property` should be "temperature".

### order
- **Type:** [[Order]]
- **Optional**
- **Overrides parent**
Used to order alternative expressions in the map generator GUI. For a given property (e.g. 'temperature'), the NamedNoiseExpression with that property's name as its `intended_property` with the lowest order will be chosen as the default in the GUI.

If no order is specified, it defaults to "2000" if the property name matches the expression name (making it the 'technical default' generator for the property if none is specified in MapGenSettings), or "3000" otherwise. A generator defined with an order less than "2000" but with a unique name can thereby override the default generator used when creating a new map through the GUI without automatically overriding the 'technical default' generator, which is probably used by existing maps.

## Example

```
{
  type = "noise-expression",
  name = "distance",
  expression = "distance_from_nearest_point{x = x, y = y, points = starting_positions}"
}
```
