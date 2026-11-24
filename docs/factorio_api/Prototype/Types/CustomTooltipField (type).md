---
title: CustomTooltipField
tags: [factorio-api, prototype, type]
---
# CustomTooltipField

*Note: `CustomTooltipField (type)`.*

Allows to add extra description items to the tooltip.

## Properties

### name
- **Type:** [[LocalisedString (type)]]

### value
- **Type:** [[LocalisedString (type)]]

### quality_header
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `"quality-tooltip.increases"`

### quality_values
- **Type:** dictionary<[[QualityID (type)]] → [[LocalisedString (type)]]>
- **Optional**
Custom values per quality level. If a value is not provided for a specific quality, [[CustomTooltipField (type)#value|CustomTooltipField::value]] will be used instead.

### order
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `100`
Ordering within all description items (modded and un-modded). Items with smaller order values are shown above items with larger values.

### show_in_factoriopedia
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### show_in_tooltip
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
