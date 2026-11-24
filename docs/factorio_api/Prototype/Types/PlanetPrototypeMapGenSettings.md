---
title: PlanetPrototypeMapGenSettings
tags: [factorio-api, prototype, type]
---
# PlanetPrototypeMapGenSettings

## Properties

### cliff_settings
- **Type:** [[CliffPlacementSettings (type)]]
- **Optional**

### territory_settings
- **Type:** [[TerritorySettings (type)]]
- **Optional**

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
Map of property name (e.g. "elevation") to name of noise expression that will provide it. Entries may be omitted. A notable usage is changing autoplace behavior of an entity based on the preset, which cannot be read from a noise expression.

### moisture_climate_control
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Used for showing the planet icon in map generator GUI next to moisture climate control.

### aux_climate_control
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Used for showing the planet icon in map generator GUI next to aux climate control.
