---
title: IconSequencePositioning
tags: [factorio-api, prototype, type]
---
# IconSequencePositioning

*Note: `IconSequencePositioning (type)`.*

Specification of where and how should be the icons of individual inventories be drawn.

## Properties

### inventory_index
- **Type:** [[defines.inventory]]

### max_icons_per_row
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** width of entity selection box / 0.75

### max_icon_rows
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** width of entity selection box / 1.5

### shift
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** {0, 0.7}

### scale
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.5`

### separation_multiplier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.1`

### multi_row_initial_height_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `-0.1`
