---
title: FrameStyleSpecification
tags: [factorio-api, prototype, type]
---
# FrameStyleSpecification

> **Parent:** [[BaseStyleSpecification]]

Root style: `"frame"`

## Properties

### type
- **Type:** `"frame_style"`

### graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
Required on the root style.

### horizontal_flow_style
- **Type:** [[HorizontalFlowStyleSpecification]]
- **Optional**
Required on the root style.

### vertical_flow_style
- **Type:** [[VerticalFlowStyleSpecification]]
- **Optional**
Required on the root style.

### header_flow_style
- **Type:** [[HorizontalFlowStyleSpecification]]
- **Optional**
Required on the root style.

### header_filler_style
- **Type:** [[EmptyWidgetStyleSpecification]]
- **Optional**
Required on the root style.

### title_style
- **Type:** [[LabelStyleSpecification]]
- **Optional**
Required on the root style.

### use_header_filler
- **Type:** [[boolean (type)]]
- **Optional**
Required on the root style.

### drag_by_title
- **Type:** [[boolean (type)]]
- **Optional**
Required on the root style.

### header_background
- **Type:** [[ElementImageSet]]
- **Optional**
- **Default:** not drawn

### background_graphical_set
- **Type:** [[ElementImageSet]]
- **Optional**
- **Default:** not drawn

### border
- **Type:** [[BorderImageSet]]
- **Optional**
Required on the root style.
