---
title: MapGenPreset
tags: [factorio-api, prototype, type]
---
# MapGenPreset

*Note: `MapGenPreset (type)`.*

## Properties

### order
- **Type:** [[Order]]
Specifies the ordering in the [map generator GUI](https://wiki.factorio.com/Map_generator).

### default
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether this is the default preset. If `true`, this preset may not have any other properties besides this and order.

If no MapGenPreset has `default = true`, the preset selector will have a blank preset label, with default settings. The "blank" preset goes away when another preset is selected.

### basic_settings
- **Type:** [[MapGenSettings (type)]]
- **Optional**
If any setting is not set, it will use the default values.

### advanced_settings
- **Type:** [[AdvancedMapGenSettings (type)]]
- **Optional**
If any setting is not set, it will use the default values.
