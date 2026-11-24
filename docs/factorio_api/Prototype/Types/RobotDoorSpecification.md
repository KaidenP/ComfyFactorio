---
title: RobotDoorSpecification
tags: [factorio-api, prototype, type]
---
# RobotDoorSpecification

## Properties

### animation
- **Type:** [[Animation]]
- **Optional**
Drawn when a robot brings/takes items from this entity.

### location_offset
- **Type:** [[Vector (type)]]
- **Optional**
The offset from the center of this entity where a robot visually brings/takes items.

### opened_duration
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`

### animation_sound
- **Type:** [[Sound]]
- **Optional**
Played when a robot brings/takes items from this entity. Only loaded if `animation` is defined.
