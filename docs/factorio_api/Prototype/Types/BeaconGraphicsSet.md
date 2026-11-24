---
title: BeaconGraphicsSet
tags: [factorio-api, prototype, type]
---
# BeaconGraphicsSet

## Properties

### draw_animation_when_idle
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_light_when_idle
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### random_animation_offset
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### module_icons_suppressed
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### reset_animation_when_frozen
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### base_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### animation_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### top_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### animation_progress
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### apply_module_tint
- **Type:** [[ModuleTint]]
- **Optional**
- **Default:** `"none"`
Which tint set in [[ModulePrototype#beacon_tint|ModulePrototype::beacon_tint]] should be applied to elements of the `animation_list`, if any.

### no_modules_tint
- **Type:** [[Color (type)]]
- **Optional**
- **Default:** no color

### animation_list
- **Type:** array<[[AnimationElement]]>
- **Optional**

### frozen_patch
- **Type:** [[Sprite]]
- **Optional**

### light
- **Type:** [[LightDefinition]]
- **Optional**

### module_visualisations
- **Type:** array<[[BeaconModuleVisualizations]]>
- **Optional**
The visualisations available for displaying the modules in the beacon. The visualisation is chosen based on art style, see [[BeaconModuleVisualizations#art_style|BeaconModuleVisualizations::art_style]] and [[ModulePrototype#art_style|ModulePrototype::art_style]].

### module_tint_mode
- **Type:** `"single-module"` | `"mix"`
- **Optional**
- **Default:** `"single-module"`

### water_reflection
- **Type:** [[WaterReflectionDefinition]]
- **Optional**
Refer to [[EntityPrototype#water_reflection|EntityPrototype::water_reflection]].
