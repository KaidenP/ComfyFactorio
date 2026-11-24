---
title: CargoHatchDefinition
tags: [factorio-api, prototype, type]
---
# CargoHatchDefinition

*Note: `CargoHatchDefinition (type)`.*

## Properties

### hatch_graphics
- **Type:** [[Animation]]
- **Optional**

### hatch_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"cargo-hatch"`
render layer for the hatch itself.

### entering_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"cargo-hatch"`
render layer for objects entering the hatch.

### offset
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0, 0}`

### pod_shadow_offset
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0, 0}`

### sky_slice_height
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `-1.0`
y height relative to hatch position where the pod art gets clipped from sky to regular sorting layer.

### slice_height
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
y height relative to hatch position where the pod art gets cut off.

### travel_height
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`
y height relative to hatch position where the pod travels to during preparing and parking.

### busy_timeout_ticks
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `120`

### hatch_opening_ticks
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `80`

### opening_sound
- **Type:** [[InterruptibleSound]]
- **Optional**
Cannot use `fade_ticks`.

### closing_sound
- **Type:** [[InterruptibleSound]]
- **Optional**
Cannot use `fade_ticks`.

### cargo_unit_entity_to_spawn
- **Type:** [[EntityID (type)]]
- **Optional**
The [[CargoPodPrototype|cargo pod]] that this cargo hatch spawns when sending cargo.

### illumination_graphic_index
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** MAX_UINT32
[[ProcessionGraphic]] index pointing to the [[ProcessionGraphicCatalogue]] inside the current [[SpaceLocationPrototype]].

### receiving_cargo_units
- **Type:** array<[[EntityID (type)]]>
- **Optional**
The [[CargoPodPrototype|cargo pods]] that this cargo hatch can receive.
