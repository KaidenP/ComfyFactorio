---
title: RailRampPrototype
tags: [factorio-api, prototype]
---
# RailRampPrototype

> **Parent:** [[RailPrototype]] · **Type name:** `rail-ramp`

A rail ramp.

## Properties

### support_range
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `15.0`
Must be lower than 500 and at least 1.

### collision_mask_allow_on_deep_oil_ocean
- **Type:** [[CollisionMaskConnector]]
- **Optional**
Defaults to the mask from [[UtilityConstants (prototype)#default_collision_masks|UtilityConstants::default_collision_masks]] when indexed by `"rail-ramp/allow_on_deep_oil_ocean"`.

### collision_box
- **Type:** [[BoundingBox (type)]]
- **Optional**
- **Default:** `{{-1.6, -7.6}, {1.6, 7.6}}`
- **Overrides parent**
The [[EntityPrototype#collision_box|collision_box]] of straight rail is hardcoded to `{{-1.6, -7.6}, {1.6, 7.6}}`.

### name
- **Type:** [[string (type)]]
- **Overrides parent**
Unique textual identification of the prototype. May only contain alphanumeric characters, dashes and underscores. May not exceed a length of 200 characters.

Requires Space Age to create prototypes with name not starting with `dummy-`. Dummy prototypes cannot be built.

### tall
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
When this is true, this entity prototype will be translucent and unselectable when "Hide tall entities" mode is active.
