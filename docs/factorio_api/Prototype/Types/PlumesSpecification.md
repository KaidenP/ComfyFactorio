---
title: PlumesSpecification
tags: [factorio-api, prototype, type]
---
# PlumesSpecification

## Properties

### render_box
- **Type:** [[BoundingBox (type)]]
- **Optional**
If given, the plumes will only render if this area is on screen (relative to the thruster)

### min_probability
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### max_probability
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### min_y_offset
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### max_y_offset
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### stateless_visualisations
- **Type:** [[PlumeEffect]] | array<[[PlumeEffect]]>
- **Optional**
Array may not be empty and may at most have 255 elements.

Non-zero `period` needs to be provided. May not have `positions` or `particle_tick_offset`.
