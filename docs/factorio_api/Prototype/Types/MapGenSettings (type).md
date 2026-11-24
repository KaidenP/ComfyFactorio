---
title: MapGenSettings
tags: [factorio-api, prototype, type]
---
# MapGenSettings

*Note: `MapGenSettings (type)`.*

## Properties

### default_enable_all_autoplace_controls
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether undefined `autoplace_controls` should fall back to the default controls or not.

### autoplace_controls
- **Type:** dictionary<[[AutoplaceControlID]] → [[FrequencySizeRichness]]>
- **Optional**

### autoplace_settings
- **Type:** dictionary<`"entity"` | `"tile"` | `"decorative"` → [[AutoplaceSettings (type)]]>
- **Optional**
Each setting in this table maps the string type to the settings for that type.

### property_expression_names
- **Type:** dictionary<[[string (type)]] → [[string (type)]] | [[boolean (type)]] | [[double (type)]]>
- **Optional**
Map of property name (`"elevation"`, etc) to name of noise expression that will provide it. Entries may be omitted. A notable usage is changing autoplace behavior of an entity based on the preset, which cannot be read from a noise expression.

### starting_points
- **Type:** array<[[MapPosition (type)]]>
- **Optional**
Array of the positions of the starting areas.

### seed
- **Type:** [[uint32 (type)]]
- **Optional**
Read by the game, but not used or set in the GUI.

### width
- **Type:** [[uint32 (type)]]
- **Optional**
Width of the map in tiles. Silently limited to 2 000 000, ie. +/- 1 million tiles from the center in both directions.

### height
- **Type:** [[uint32 (type)]]
- **Optional**
Height of the map in tiles. Silently limited to 2 000 000, ie. +/- 1 million tiles from the center in both directions.

### starting_area
- **Type:** [[MapGenSize (type)]]
- **Optional**
- **Default:** `1`
Size of the starting area. The starting area only effects enemy placement, and has no effect on resources.

### peaceful_mode
- **Type:** [[boolean (type)]]
- **Optional**
If true, enemy creatures will not attack unless the player first attacks them.

### no_enemies_mode
- **Type:** [[boolean (type)]]
- **Optional**
If true, enemy creatures will not naturally spawn from spawners, map gen, or trigger effects.

### cliff_settings
- **Type:** [[CliffPlacementSettings (type)]]
- **Optional**

### territory_settings
- **Type:** [[TerritorySettings (type)]]
- **Optional**
