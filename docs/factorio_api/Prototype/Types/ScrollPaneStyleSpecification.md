---
title: ScrollPaneStyleSpecification
tags: [factorio-api, prototype, type]
---
# ScrollPaneStyleSpecification

> **Parent:** [[BaseStyleSpecification]]

Root style: `"scroll_pane"`

## Properties

### type
- **Type:** `"scroll_pane_style"`

### vertical_flow_style
- **Type:** [[VerticalFlowStyleSpecification]]
- **Optional**
Required on the root style.

### horizontal_scrollbar_style
- **Type:** [[HorizontalScrollBarStyleSpecification]]
- **Optional**
Required on the root style.

### vertical_scrollbar_style
- **Type:** [[VerticalScrollBarStyleSpecification]]
- **Optional**
Required on the root style.

### graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
Required on the root style.

### background_graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
Required on the root style.

### extra_padding_when_activated
- **Type:** [[int32 (type)]]
- **Optional**
Sets `extra_top_padding_when_activated`, `extra_bottom_padding_when_activated`, `extra_left_padding_when_activated` and `extra_right_padding_when_activated`.

### extra_top_padding_when_activated
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** `0`

### extra_bottom_padding_when_activated
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** `0`

### extra_left_padding_when_activated
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** `0`

### extra_right_padding_when_activated
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** `0`

### extra_margin_when_activated
- **Type:** [[int32 (type)]]
- **Optional**
Sets `extra_top_margin_when_activated`, `extra_bottom_margin_when_activated`, `extra_left_margin_when_activated` and `extra_right_margin_when_activated`.

### extra_top_margin_when_activated
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** `0`

### extra_bottom_margin_when_activated
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** `0`

### extra_left_margin_when_activated
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** `0`

### extra_right_margin_when_activated
- **Type:** [[int32 (type)]]
- **Optional**
- **Default:** `0`

### dont_force_clipping_rect_for_contents
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### always_draw_borders
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### scrollbars_go_outside
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
