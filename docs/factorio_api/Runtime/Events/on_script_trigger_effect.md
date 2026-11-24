---
title: on_script_trigger_effect
tags: [factorio-api, runtime, event]
---
# on_script_trigger_effect

Called when a script trigger effect is triggered.

## Data

### effect_id
- **Type:** [[string]]
The effect_id specified in the trigger effect.

### surface_index
- **Type:** [[uint32]]
The surface the effect happened on.

### source_position
- **Type:** [[MapPosition]]
- **Optional**

### source_entity
- **Type:** [[LuaEntity]]
- **Optional**

### target_position
- **Type:** [[MapPosition]]
- **Optional**

### target_entity
- **Type:** [[LuaEntity]]
- **Optional**

### cause_entity
- **Type:** [[LuaEntity]]
- **Optional**
The entity that originally caused the sequence of triggers

### quality
- **Type:** [[string]]
- **Optional**

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
