---
title: TableStyleSpecification
tags: [factorio-api, prototype, type]
---
# TableStyleSpecification

> **Parent:** [[BaseStyleSpecification]]

Root style: `"table"`

## Properties

### type
- **Type:** `"table_style"`

### horizontal_spacing
- **Type:** [[int32 (type)]] | array<[[SpacingItem]]>
- **Optional**
Required on the root style.

### vertical_spacing
- **Type:** [[int32 (type)]] | array<[[SpacingItem]]>
- **Optional**
Required on the root style.

### cell_padding
- **Type:** [[int16 (type)]]
- **Optional**
Sets `top_cell_padding`, `right_cell_padding`, `bottom_cell_padding` and `left_cell_padding` to the same value.

### top_cell_padding
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** `0`

### right_cell_padding
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** `0`

### bottom_cell_padding
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** `0`

### left_cell_padding
- **Type:** [[int16 (type)]]
- **Optional**
- **Default:** `0`

### apply_row_graphical_set_per_column
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### wide_as_column_count
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### column_graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
- **Default:** Not drawn

### default_row_graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
- **Default:** Not drawn

### even_row_graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
- **Default:** Not drawn

### odd_row_graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
- **Default:** Not drawn

### hovered_graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
- **Default:** Not drawn

### clicked_graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
- **Default:** Not drawn

### selected_graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
- **Default:** Not drawn

### selected_hovered_graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
- **Default:** Not drawn

### selected_clicked_graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
- **Default:** Not drawn

### background_graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
- **Default:** Not drawn

### column_alignments
- **Type:** array<[[ColumnAlignment]]>
- **Optional**

### column_widths
- **Type:** [[ColumnWidthItem]] | array<[[ColumnWidth]]>
- **Optional**

### hovered_row_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{0, 0, 0, 0}`

### selected_row_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{110, 110, 110}`

### vertical_line_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{110, 110, 110}`

### horizontal_line_color
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** `{0, 0, 0, 0}`

### column_ordering_ascending_button_style
- **Type:** [[ButtonStyleSpecification]]
- **Optional**

### column_ordering_descending_button_style
- **Type:** [[ButtonStyleSpecification]]
- **Optional**

### inactive_column_ordering_ascending_button_style
- **Type:** [[ButtonStyleSpecification]]
- **Optional**

### inactive_column_ordering_descending_button_style
- **Type:** [[ButtonStyleSpecification]]
- **Optional**

### border
- **Type:** [[BorderImageSet]]
- **Optional**
Required on the root style.
