---
title: SpiderVehicleGraphicsSet
tags: [factorio-api, prototype, type]
---
# SpiderVehicleGraphicsSet

> **Parent:** [[SpiderTorsoGraphicsSet]]

Used to specify the graphics for [[SpiderVehiclePrototype]].

## Properties

### autopilot_destination_visualisation_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### light
- **Type:** [[LightDefinition]]
- **Optional**

### eye_light
- **Type:** [[LightDefinition]]
- **Optional**
Placed in multiple positions, as determined by `light_positions`.

### autopilot_destination_on_map_visualisation
- **Type:** [[Animation]]
- **Optional**

### autopilot_destination_queue_on_map_visualisation
- **Type:** [[Animation]]
- **Optional**

### autopilot_destination_visualisation
- **Type:** [[Animation]]
- **Optional**

### autopilot_destination_queue_visualisation
- **Type:** [[Animation]]
- **Optional**

### autopilot_path_visualisation_line_width
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.125`

### autopilot_path_visualisation_on_map_line_width
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `2.0`

### light_positions
- **Type:** array<array<[[Vector (type)]]>>
- **Optional**
Defines where each `eye_light` is placed. One array per eye and each of those arrays should contain one position per body direction.

### default_color
- **Type:** [[float (type)]]
- **Optional**
The default mask color for the spider vehicle. Defaults to orange.
