---
title: on_runtime_mod_setting_changed
tags: [factorio-api, runtime, event]
---
# on_runtime_mod_setting_changed

Called when a runtime mod setting is changed by a player.

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**
If the `setting_type` is `"global"` and it was changed through the mod settings GUI, this is the index of the player that changed the global setting. If the `setting_type` is `"runtime-per-user"` and it changed a current setting of the player, this is the index of the player whose setting was changed. In all other cases, this is `nil`.

### setting
- **Type:** [[string]]
The prototype name of the setting that was changed.

### setting_type
- **Type:** `"runtime-global"` | `"runtime-per-user"`

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
