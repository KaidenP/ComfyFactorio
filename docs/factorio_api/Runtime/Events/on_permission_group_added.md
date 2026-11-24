---
title: on_permission_group_added
tags: [factorio-api, runtime, event]
---
# on_permission_group_added

Called directly after a permission group is added.

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**
The player that added the group or `nil` if by a mod.

### group
- **Type:** [[LuaPermissionGroup]]
The group added.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
