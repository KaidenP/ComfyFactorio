---
title: LuaStyle
tags: [factorio-api, runtime, class]
---
# LuaStyle

Style of a GUI element. All of the attributes listed here may be `nil` if not available for a particular GUI element.

## Attributes

### gui
- **Type:** [[LuaGui]]
GUI of the [[LuaGuiElement]] of this style.

### name
- **Type:** [[string]]
- **Writable:** [[string]]
Name of this style.

### minimal_width
- **Type:** [[int32]]
- **Writable:** [[int32]]
Minimal width ensures, that the widget will never be smaller than than that size. It can't be squashed to be smaller.

### maximal_width
- **Type:** [[int32]]
- **Writable:** [[int32]]
Maximal width ensures, that the widget will never be bigger than than that size. It can't be stretched to be bigger.

### minimal_height
- **Type:** [[int32]]
- **Writable:** [[int32]]
Minimal height ensures, that the widget will never be smaller than than that size. It can't be squashed to be smaller.

### maximal_height
- **Type:** [[int32]]
- **Writable:** [[int32]]
Maximal height ensures, that the widget will never be bigger than than that size. It can't be stretched to be bigger.

### natural_width
- **Type:** [[int32]]
- **Writable:** [[int32]]
Natural width specifies the width of the element tries to have, but it can still be squashed/stretched to have a smaller or bigger size.

### natural_height
- **Type:** [[int32]]
- **Writable:** [[int32]]
Natural height specifies the height of the element tries to have, but it can still be squashed/stretched to have a smaller or bigger size.

### top_padding
- **Type:** [[int16]]
- **Writable:** [[int16]]

### right_padding
- **Type:** [[int16]]
- **Writable:** [[int16]]

### bottom_padding
- **Type:** [[int16]]
- **Writable:** [[int16]]

### left_padding
- **Type:** [[int16]]
- **Writable:** [[int16]]

### top_margin
- **Type:** [[int16]]
- **Writable:** [[int16]]

### right_margin
- **Type:** [[int16]]
- **Writable:** [[int16]]

### bottom_margin
- **Type:** [[int16]]
- **Writable:** [[int16]]

### left_margin
- **Type:** [[int16]]
- **Writable:** [[int16]]

### horizontal_align
- **Type:** `"left"` | `"center"` | `"right"`
- **Writable:** `"left"` | `"center"` | `"right"`
- **Optional**
Horizontal align of the inner content of the widget, if any.

### vertical_align
- **Type:** `"top"` | `"center"` | `"bottom"`
- **Writable:** `"top"` | `"center"` | `"bottom"`
- **Optional**
Vertical align of the inner content of the widget, if any.

### font_color
- **Type:** [[Color]]
- **Writable:** [[Color]]

### font
- **Type:** [[string]]
- **Writable:** [[string]]

### top_cell_padding
- **Type:** [[int16]]
- **Writable:** [[int16]]
Space between the table cell contents top and border.

### right_cell_padding
- **Type:** [[int16]]
- **Writable:** [[int16]]
Space between the table cell contents right and border.

### bottom_cell_padding
- **Type:** [[int16]]
- **Writable:** [[int16]]
Space between the table cell contents bottom and border.

### left_cell_padding
- **Type:** [[int16]]
- **Writable:** [[int16]]
Space between the table cell contents left and border.

### horizontally_stretchable
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
- **Optional**
Whether the GUI element stretches its size horizontally to other elements. `nil` if this element does not support stretching.

### vertically_stretchable
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
- **Optional**
Whether the GUI element stretches its size vertically to other elements. `nil` if this element does not support stretching.

### horizontally_squashable
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
- **Optional**
Whether the GUI element can be squashed (by maximal width of some parent element) horizontally. `nil` if this element does not support squashing.

This is mainly meant to be used for scroll-pane. The default value is false.

### vertically_squashable
- **Type:** [[boolean]]
- **Writable:** [[boolean]]
- **Optional**
Whether the GUI element can be squashed (by maximal height of some parent element) vertically. `nil` if this element does not support squashing.

This is mainly meant to be used for scroll-pane. The default (parent) value for scroll pane is true, false otherwise.

### rich_text_setting
- **Type:** [[defines.rich_text_setting]]
- **Writable:** [[defines.rich_text_setting]]
How this GUI element handles rich text.

### hovered_font_color
- **Type:** [[Color]]
- **Writable:** [[Color]]

### clicked_font_color
- **Type:** [[Color]]
- **Writable:** [[Color]]

### disabled_font_color
- **Type:** [[Color]]
- **Writable:** [[Color]]

### pie_progress_color
- **Type:** [[Color]]
- **Writable:** [[Color]]

### clicked_vertical_offset
- **Type:** [[uint32]]
- **Writable:** [[uint32]]

### selected_font_color
- **Type:** [[Color]]
- **Writable:** [[Color]]

### selected_hovered_font_color
- **Type:** [[Color]]
- **Writable:** [[Color]]

### selected_clicked_font_color
- **Type:** [[Color]]
- **Writable:** [[Color]]

### strikethrough_color
- **Type:** [[Color]]
- **Writable:** [[Color]]

### draw_grayscale_picture
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### horizontal_spacing
- **Type:** [[int32]]
- **Writable:** [[int32]]
Horizontal space between individual cells.

### vertical_spacing
- **Type:** [[int32]]
- **Writable:** [[int32]]
Vertical space between individual cells.

### use_header_filler
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### bar_width
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
The thickness of the bar, not the horizontal width.

### color
- **Type:** [[Color]]
- **Writable:** [[Color]]

### column_alignments
- **Type:** LuaCustomTable<[[uint32]] → [[Alignment]]>
Array containing the alignment for every column of this table element. Even though this property is marked as read-only, the alignment can be changed by indexing the LuaCustomTable, like so:
**Examples:**

```
table_element.style.column_alignments[1] = "center"
```

### single_line
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### extra_top_padding_when_activated
- **Type:** [[int32]]
- **Writable:** [[int32]]

### extra_bottom_padding_when_activated
- **Type:** [[int32]]
- **Writable:** [[int32]]

### extra_left_padding_when_activated
- **Type:** [[int32]]
- **Writable:** [[int32]]

### extra_right_padding_when_activated
- **Type:** [[int32]]
- **Writable:** [[int32]]

### extra_top_margin_when_activated
- **Type:** [[int32]]
- **Writable:** [[int32]]

### extra_bottom_margin_when_activated
- **Type:** [[int32]]
- **Writable:** [[int32]]

### extra_left_margin_when_activated
- **Type:** [[int32]]
- **Writable:** [[int32]]

### extra_right_margin_when_activated
- **Type:** [[int32]]
- **Writable:** [[int32]]

### extra_padding_when_activated
- **Writable:** [[int32]] | array<[[int32]]>
Sets `extra_top/right/bottom/left_padding_when_activated` to this value.

An array with two values sets top/bottom padding to the first value and left/right padding to the second value. An array with four values sets top, right, bottom, left padding respectively.

### extra_margin_when_activated
- **Writable:** [[int32]] | array<[[int32]]>
Sets `extra_top/right/bottom/left_margin_when_activated` to this value.

An array with two values sets top/bottom margin to the first value and left/right margin to the second value. An array with four values sets top, right, bottom, left margin respectively.

### stretch_image_to_widget_size
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### badge_font
- **Type:** [[string]]
- **Writable:** [[string]]

### badge_horizontal_spacing
- **Type:** [[int32]]
- **Writable:** [[int32]]

### default_badge_font_color
- **Type:** [[Color]]
- **Writable:** [[Color]]

### selected_badge_font_color
- **Type:** [[Color]]
- **Writable:** [[Color]]

### disabled_badge_font_color
- **Type:** [[Color]]
- **Writable:** [[Color]]

### width
- **Writable:** [[int32]]
Sets both minimal and maximal width to the given value.

### height
- **Writable:** [[int32]]
Sets both minimal and maximal height to the given value.

### size
- **Writable:** [[int32]] | array<[[int32]]>
Sets both width and height to the given value. Also accepts an array with two values, setting width to the first and height to the second one.

### padding
- **Writable:** [[int16]] | array<[[int16]]>
Sets top/right/bottom/left paddings to this value.

An array with two values sets top/bottom padding to the first value and left/right padding to the second value. An array with four values sets top, right, bottom, left padding respectively.

### margin
- **Writable:** [[int16]] | array<[[int16]]>
Sets top/right/bottom/left margins to this value.

An array with two values sets top/bottom margin to the first value and left/right margin to the second value. An array with four values sets top, right, bottom, left margin respectively.

### cell_padding
- **Writable:** [[int16]]
Space between the table cell contents and border. Sets top/right/bottom/left cell paddings to this value.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### get_style
Gets the given sub-style of this style if it exists. See [[StyleSpecification]] types for what sub styles are usable.

Note: when creating sub-styles they have no set values and have the parent set to the styles top-level default.

Note: when the parent [[LuaGuiElement#style|LuaGuiElement::style]] is directly changed (element.style = "new_style") any sub-styles will be invalidated.

**Parameters:**
- **`style_name`** — [[string]]: The style to get.
- **`create`** — [[boolean]] *(optional)*: If true, and the given sub-style is valid - it will be created if it does not exist. Defaults to `false`.

**Returns:**
- [[LuaStyle]] *(optional)*
