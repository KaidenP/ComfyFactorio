---
title: RollingStockPrototype
tags: [factorio-api, prototype]
---
# RollingStockPrototype

> **Parent:** [[VehiclePrototype]] · **Abstract**

The abstract base of all rolling stock.

## Properties

### max_speed
- **Type:** [[double (type)]]
- **Optional**
Maximum speed of the rolling stock in tiles/tick.

In-game, the max speed of a train is `average(all_rolling_stock_max_speeds) × average(all_fuel_modifiers_in_all_locomotives)`. If this value is not provided it is ignored for the average(all_rolling_stock_max_speed) calculation. This calculated train speed is then silently capped to 7386.3km/h.

### air_resistance
- **Type:** [[double (type)]]

### joint_distance
- **Type:** [[double (type)]]
The length between this rolling stocks front and rear joints. Joints are the point where connection_distance is measured from when rolling stock are connected to one another. Wheels sprite are placed based on the joint position.

Maximum joint distance is 15.

Note: There needs to be border at least 0.2 between the [[EntityPrototype#collision_box|bounding box]] edge and joint. This means that the collision_box must be at least `{{-0,-0.2},{0,0.2}}`.

### connection_distance
- **Type:** [[double (type)]]
The distance between the joint of this rolling stock and its connected rolling stocks joint.

Maximum connection distance is 15.

### pictures
- **Type:** [[RollingStockRotatedSlopedGraphics]]
- **Optional**

### wheels
- **Type:** [[RollingStockRotatedSlopedGraphics]]
- **Optional**

### vertical_selection_shift
- **Type:** [[double (type)]]

### drive_over_tie_trigger
- **Type:** [[TriggerEffect]]
- **Optional**
Usually a sound to play when the rolling stock drives over a tie. The rolling stock is considered to be driving over a tie every `tie_distance` tiles.

### drive_over_tie_trigger_minimal_speed
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.0`

### tie_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `10.0`
In tiles. Used to determine how often `drive_over_tie_trigger` is triggered.

### back_light
- **Type:** [[LightDefinition]]
- **Optional**

### stand_by_light
- **Type:** [[LightDefinition]]
- **Optional**

### horizontal_doors
- **Type:** [[Animation]]
- **Optional**

### vertical_doors
- **Type:** [[Animation]]
- **Optional**

### color
- **Type:** [[Color (type)]]
- **Optional**

### allow_manual_color
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### allow_robot_dispatch_in_automatic_mode
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### default_copy_color_from_train_stop
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### quality_affects_max_speed
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### transition_collision_mask
- **Type:** [[CollisionMaskConnector]]
- **Optional**
Defaults to the mask from [[UtilityConstants (prototype)#default_collision_masks|UtilityConstants::default_collision_masks]] when indexed by  `type .. "/transition"`.

### elevated_collision_mask
- **Type:** [[CollisionMaskConnector]]
- **Optional**
Defaults to the mask from [[UtilityConstants (prototype)#default_collision_masks|UtilityConstants::default_collision_masks]] when indexed by  `type .. "/elevated"`.

### elevated_selection_priority
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `56`

### elevated_rail_sound
- **Type:** [[MainSound]]
- **Optional**

### drive_over_elevated_tie_trigger
- **Type:** [[TriggerEffect]]
- **Optional**

### door_opening_sound
- **Type:** [[InterruptibleSound]]
- **Optional**
Cannot use `fade_ticks`.

### door_closing_sound
- **Type:** [[InterruptibleSound]]
- **Optional**
Cannot use `fade_ticks`.
