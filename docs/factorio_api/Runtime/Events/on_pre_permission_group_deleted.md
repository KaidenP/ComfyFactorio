---
title: on_pre_permission_group_deleted
tags: [factorio-api, runtime, event]
---
# on_pre_permission_group_deleted

Called directly before a permission group is deleted.

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**
The player doing the deletion or `nil` if by a mod.

### group
- **Type:** [[LuaPermissionGroup]]
The group to be deleted.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
