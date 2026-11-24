---
title: on_permission_group_deleted
tags: [factorio-api, runtime, event]
---
# on_permission_group_deleted

Called directly after a permission group is deleted.

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**
The player doing the deletion or `nil` if by a mod.

### group_name
- **Type:** [[string]]
The group that was deleted.

### id
- **Type:** [[uint32]]
The group id that was deleted.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
