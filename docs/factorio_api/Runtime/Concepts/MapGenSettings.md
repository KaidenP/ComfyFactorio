---
title: MapGenSettings
tags: [factorio-api, runtime, concept]
---
# MapGenSettings

When reading MapGenSettings, all properties will always be present, but they can be omitted when writing.

## Fields

### autoplace_controls
- **Type:** dictionary<[[string]] → [[AutoplaceControl]]>
- **Optional**
Indexed by autoplace control prototype name.

### default_enable_all_autoplace_controls
- **Type:** [[boolean]]
- **Optional**
Whether undefined `autoplace_controls` should fall back to the default controls or not. Defaults to `true`.

### autoplace_settings
- **Type:** dictionary<`"entity"` | `"tile"` | `"decorative"` → [[AutoplaceSettings]]>
- **Optional**
Each setting in this dictionary maps the string type to the settings for that type.

### seed
- **Type:** [[uint32]]
- **Optional**
) The random seed used to generated this map.

### width
- **Type:** [[uint32]]
- **Optional**
) Width in tiles. If `0`, the map has 'infinite' width, with the actual limitation being one million tiles in each direction from the center.

### height
- **Type:** [[uint32]]
- **Optional**
Height in tiles. If `0`, the map has 'infinite' height, with the actual limitation being one million tiles in each direction from the center.

### starting_area
- **Type:** [[MapGenSize]]
- **Optional**
Size of the starting area. Defaults to `1`.

### starting_points
- **Type:** array<[[MapPosition]]>
- **Optional**
Positions of the starting areas.

### peaceful_mode
- **Type:** [[boolean]]
- **Optional**
Whether enemy creatures will not attack unless the player first attacks them.

### no_enemies_mode
- **Type:** [[boolean]]
- **Optional**
Whether enemy creatures will not naturally spawn from spawners, map gen, or trigger effects.

### property_expression_names
- **Type:** [[PropertyExpressionNames]]
- **Optional**
Overrides for tile property value generators.

### cliff_settings
- **Type:** [[CliffPlacementSettings]]
- **Optional**
Map generation settings for entities of the type "cliff".

### territory_settings
- **Type:** [[TerritorySettings]]
- **Optional**

## Examples

```
-- Assuming a NamedNoiseExpression with the name "my-alternate-grass1-probability" is defined...
local surface = game.player.surface
local mgs = surface.map_gen_settings
mgs.property_expression_names["tile:grass1:probability"] = "my-alternate-grass1-probability"
surface.map_gen_settings = mgs
-- ...would override the probability of grass1 being placed at any given point on the current surface.
```

```
-- To make there be no deep water on (newly generated chunks) a surface
local surface = game.player.surface
local mgs = surface.map_gen_settings
mgs.property_expression_names["tile:deepwater:probability"] = -1000
surface.map_gen_settings = mgs
-- This does not require a NamedNoiseExpression to be defined, since literal numbers (and strings naming literal
-- numbers, e.g. `"123"`) are understood to stand for constant value expressions.
```
