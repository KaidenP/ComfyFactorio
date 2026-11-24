---
title: PropertyExpressionNames
tags: [factorio-api, runtime, concept]
---
# PropertyExpressionNames

All other MapGenSettings feed into named noise expressions, and therefore placement can be overridden by including the name of a property in this dictionary. The probability and richness functions for placing specific tiles, entities, and decoratives can be overridden by including an entry named `{tile|entity|decorative}:(prototype name):{probability|richness}`.

## Type

dictionary<[[string]] → [[string]]>

Values either name a NamedNoiseExpression or can be literal numbers, stored as strings (e.g. `5`). All other controls can be overridden by a property expression names. Notable properties:

- `moisture` - a value between 0 and 1 that determines whether a tile becomes sandy (low moisture) or grassy (high moisture).
- `aux` - a value between 0 and 1 that determines whether low-moisture tiles become sand or red desert.
- `temperature` - provides a value (vaguely representing degrees Celsius, varying between -20 and 50) that is used (together with moisture and aux) as part of tree and decorative placement.
- `elevation` - tiles values less than zero become water. Cliffs are placed along certain contours according to [[CliffPlacementSettings]].
- `cliffiness` - determines whether (when >0.5) or not (when <0.5) a cliff will be placed at an otherwise suitable (according to [[CliffPlacementSettings]]) location.
- `enemy-base-intensity` - a number that is referenced by both `enemy-base-frequency` and `enemy-base-radius`. i.e. if this is overridden, enemy base frequency and size will both be affected and do something reasonable. By default, this expression returns a value proportional to distance from any starting point, clamped at about 7.
- `enemy-base-frequency` - a number representing average number of enemy bases per tile for a region, by default in terms of `enemy-base-intensity`.
- `enemy-base-radius` - a number representing the radius of an enemy base, if one were to be placed on the given tile, by default proportional to a constant plus `enemy-base-intensity`.

Climate controls ('Moisture' and 'Terrain type' at the bottom of the Terrain tab in the map generator GUI) don't have their own dedicated structures in MapGenSettings. Instead, their values are stored as property expression overrides with long names:

- `control:moisture:frequency` - frequency (inverse of scale) multiplier for moisture noise.  Default is 1.
- `control:moisture:bias` - global bias for moisture (which normally varies between 0 and 1). Default is 0.
- `control:aux:frequency` - frequency (inverse of scale) multiplier for aux (called 'terrain type' in the GUI) noise.  Default is 1.
- `control:aux:bias` - global bias for aux/terrain type (which normally varies between 0 and 1). Default is 0.
