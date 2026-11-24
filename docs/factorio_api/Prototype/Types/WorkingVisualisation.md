---
title: WorkingVisualisation
tags: [factorio-api, prototype, type]
---
# WorkingVisualisation

Used by crafting machines to display different graphics when the machine is running.

## Properties

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### fadeout
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### synced_fadeout
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### constant_speed
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether the animations are always played at the same speed, not adjusted to the machine speed.

### always_draw
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### animated_shift
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### align_to_waypoint
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### mining_drill_scorch_mark
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### secondary_draw_order
- **Type:** [[int8 (type)]]
- **Optional**
Used to determine render order for sprites with the same `render_layer` in the same position. Sprites with a higher `secondary_draw_order` are drawn on top.

### light
- **Type:** [[LightDefinition]]
- **Optional**

### effect
- **Type:** `"flicker"` | `"uranium-glow"` | `"none"`
- **Optional**

### apply_recipe_tint
- **Type:** `"primary"` | `"secondary"` | `"tertiary"` | `"quaternary"` | `"none"`
- **Optional**
Used by [[CraftingMachinePrototype]]. Has precedence over `apply_tint`.

### apply_tint
- **Type:** `"resource-color"` | `"input-fluid-base-color"` | `"input-fluid-flow-color"` | `"status"` | `"none"` | `"visual-state-color"`
- **Optional**
Used by [[CraftingMachinePrototype]] ("status" and "visual-state-color" only) and [[MiningDrillPrototype]].

For "status" on CraftingMachine and MiningDrill, the colors are specified via [[WorkingVisualisations#status_colors|WorkingVisualisations::status_colors]]. For "resource-color", the colors are specified via [[ResourceEntityPrototype#mining_visualisation_tint|ResourceEntityPrototype::mining_visualisation_tint]].

### north_animation
- **Type:** [[Animation]]
- **Optional**

### east_animation
- **Type:** [[Animation]]
- **Optional**

### south_animation
- **Type:** [[Animation]]
- **Optional**

### west_animation
- **Type:** [[Animation]]
- **Optional**

### north_position
- **Type:** [[Vector (type)]]
- **Optional**

### east_position
- **Type:** [[Vector (type)]]
- **Optional**

### south_position
- **Type:** [[Vector (type)]]
- **Optional**

### west_position
- **Type:** [[Vector (type)]]
- **Optional**

### north_secondary_draw_order
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** Value of `secondary_draw_order`

### east_secondary_draw_order
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** Value of `secondary_draw_order`

### south_secondary_draw_order
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** Value of `secondary_draw_order`

### west_secondary_draw_order
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** Value of `secondary_draw_order`

### north_fog_mask
- **Type:** [[FogMaskShapeDefinition]]
- **Optional**
If defined, animation in this visualisation layer will be used only as mask for fog effect and will not render in world.

### east_fog_mask
- **Type:** [[FogMaskShapeDefinition]]
- **Optional**
If defined, animation in this visualisation layer will be used only as mask for fog effect and will not render in world.

### south_fog_mask
- **Type:** [[FogMaskShapeDefinition]]
- **Optional**
If defined, animation in this visualisation layer will be used only as mask for fog effect and will not render in world.

### west_fog_mask
- **Type:** [[FogMaskShapeDefinition]]
- **Optional**
If defined, animation in this visualisation layer will be used only as mask for fog effect and will not render in world.

### fog_mask
- **Type:** [[FogMaskShapeDefinition]]
- **Optional**
Loaded only if at least one of north_fog_mask, east_fog_mask, south_fog_mask, west_fog_mask is not specified.

If defined, animation in this visualisation layer will be used only as mask for fog effect and will not render in world.

### animation
- **Type:** [[Animation]]
- **Optional**

### draw_in_states
- **Type:** array<[[string (type)]]>
- **Optional**
Only loaded if [[WorkingVisualisations#states|WorkingVisualisations::states]] is defined in the WorkingVisualisations that loads this.

### draw_when_state_filter_matches
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Only loaded if [[WorkingVisualisations#states|WorkingVisualisations::states]] is defined in the WorkingVisualisations that loads this.

### enabled_by_name
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### name
- **Type:** [[string (type)]]
- **Optional**
- **Default:** `""`
Used by [[MainSound#play_for_working_visualisations|MainSound::play_for_working_visualisations]], [[SoundAccent#play_for_working_visualisation|SoundAccent::play_for_working_visualisation]], [[FluidBox#enable_working_visualisations|FluidBox::enable_working_visualisations]], and [[PipeConnectionDefinition (type)#enable_working_visualisations|PipeConnectionDefinition::enable_working_visualisations]].

### enabled_in_animated_shift_during_waypoint_stop
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### enabled_in_animated_shift_during_transition
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### frame_based_on_shift_animation_progress
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### scorch_mark_fade_out_duration
- **Type:** [[uint16 (type)]]
- **Optional**
Only loaded, and mandatory if `mining_drill_scorch_mark` is `true`. Cannot be larger than `scorch_mark_lifetime`.

### scorch_mark_lifetime
- **Type:** [[uint16 (type)]]
- **Optional**
Only loaded, and mandatory if `mining_drill_scorch_mark` is `true`.

### scorch_mark_fade_in_frames
- **Type:** [[uint8 (type)]]
- **Optional**
Only loaded, and mandatory if `mining_drill_scorch_mark` is `true`.
