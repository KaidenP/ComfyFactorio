---
title: UnitAISettings
tags: [factorio-api, runtime, concept]
---
# UnitAISettings

## Fields

### destroy_when_commands_fail
- **Type:** [[boolean]]
If enabled, units that repeatedly fail to succeed at commands will be destroyed.

### allow_try_return_to_spawner
- **Type:** [[boolean]]
If enabled, units that have nothing else to do will attempt to return to a spawner.

### do_separation
- **Type:** [[boolean]]
If enabled, units will try to separate themselves from nearby friendly units.

### path_resolution_modifier
- **Type:** [[int8]]
Must be between -8 and 8.

### strafe_settings
- **Type:** [[PrototypeStrafeSettings]]
- **Optional**

### size_in_group
- **Type:** [[float]]
The amount of slots in a unit group this unit takes up. For example, a unit with `groupingSize` of 2 will count as 2 normal-sized units when filling up a unit group. Must be greater than 0.

### join_attacks
- **Type:** [[boolean]]
If enabled, the unit is permitted to join attack groups.
