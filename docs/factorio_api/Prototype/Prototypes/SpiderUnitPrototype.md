---
title: SpiderUnitPrototype
tags: [factorio-api, prototype]
---
# SpiderUnitPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `spider-unit`

## Properties

### spider_engine
- **Type:** [[SpiderEngineSpecification (type)]]

### height
- **Type:** [[float (type)]]
The height of the spider affects the shooting height and the drawing of the graphics and lights.

### torso_bob_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Cannot be negative.

### torso_rotation_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
The orientation of the torso of the spider affects the shooting direction and the drawing of the graphics and lights.

### graphics_set
- **Type:** [[SpiderTorsoGraphicsSet]]
- **Optional**

### absorptions_to_join_attack
- **Type:** dictionary<[[AirbornePollutantID]] → [[float (type)]]>
- **Optional**

### spawning_time_modifier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### buildable_entities
- **Type:** array<[[EntityID (type)]]>
- **Optional**
A list of entity prototypes that this spider unit can build when given the build base command.

If empty or not specified, the spider unit cannot build anything.

### radar_range
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
In chunks. The radius of how many chunks this spider unit charts around itself.

### steering
- **Type:** [[SteeringSettings (type)]]
- **Optional**

### attack_parameters
- **Type:** [[AttackParameters (type)]]

### dying_sound
- **Type:** [[Sound]]
- **Optional**

### warcry
- **Type:** [[Sound]]
- **Optional**
A sound the spider unit makes when it sets out to attack.

### vision_distance
- **Type:** [[double (type)]]
Must be less than or equal to 100.

### distraction_cooldown
- **Type:** [[uint32 (type)]]

### min_pursue_time
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `600`

### max_pursue_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `50`

### ai_settings
- **Type:** [[UnitAISettings (type)]]
- **Optional**
