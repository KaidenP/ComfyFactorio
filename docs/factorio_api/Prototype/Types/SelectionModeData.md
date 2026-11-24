---
title: SelectionModeData
tags: [factorio-api, prototype, type]
---
# SelectionModeData

## Properties

### border_color
- **Type:** [[Color (type)]]

### count_button_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** Value of border_color

### chart_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** Value of border_color

### cursor_box_type
- **Type:** [[CursorBoxType]]

### draw_selection_counts
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Whether the list of how many entities are selected should be shown.

### mode
- **Type:** [[SelectionModeFlags (type)]]

### entity_filters
- **Type:** array<[[EntityID (type)]]>
- **Optional**

### entity_type_filters
- **Type:** array<[[string (type)]]>
- **Optional**

### tile_filters
- **Type:** array<[[TileID (type)]]>
- **Optional**

### started_sound
- **Type:** [[Sound]]
- **Optional**

### ended_sound
- **Type:** [[Sound]]
- **Optional**

### play_ended_sound_when_nothing_selected
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### entity_filter_mode
- **Type:** `"whitelist"` | `"blacklist"`
- **Optional**
- **Default:** `"whitelist"`

### tile_filter_mode
- **Type:** `"whitelist"` | `"blacklist"`
- **Optional**
- **Default:** `"whitelist"`

### ignore_cannot_select_entities
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this is `false`, using any of the mode flags `"blueprint"`, `"deconstruct"`, `"cancel-deconstruct"`, `"upgrade"`, `"cancel-upgrade"` or `"downgrade"` without also specifying another flag that selects entities will result in an error, because the selection tool cannot select any entities and this is likely undesired behavior.

Setting this to `true` disables this error.

### ignore_cannot_select_tiles
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this is `false`, using any of the mode flags `"blueprint"` or `"deconstruct"` without also specifying any flag that selects tiles will result in an error, because the selection tool cannot select any tiles and this is likely undesired behavior.

Setting this to `true` disables this error.
