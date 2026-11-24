---
title: RailSupportPrototype
tags: [factorio-api, prototype]
---
# RailSupportPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `rail-support`

## Properties

### graphics_set
- **Type:** [[RailSupportGraphicsSet]]

### support_range
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `15.0`
Must be lower than 500 and at least 1.

### not_buildable_if_no_rails
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### snap_to_spots_distance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### collision_mask_allow_on_deep_oil_ocean
- **Type:** [[CollisionMaskConnector]]
- **Optional**
Defaults to the mask from [[UtilityConstants (prototype)#default_collision_masks|UtilityConstants::default_collision_masks]] when indexed by `"rail-support/allow_on_deep_oil_ocean"`.

### elevated_selection_boxes
- **Type:** array<[[BoundingBox (type)]]>
- **Optional**
Array must contain 8 items.

### build_grid_size
- **Type:** `2`
- **Optional**
- **Default:** `2`
- **Overrides parent**
Has to be 2 for 2x2 grid.

### name
- **Type:** [[string (type)]]
- **Overrides parent**
Unique textual identification of the prototype. May only contain alphanumeric characters, dashes and underscores. May not exceed a length of 200 characters.

Requires Space Age to create prototypes with name not starting with `dummy-`. Dummy prototypes cannot be built.
