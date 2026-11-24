---
title: on_permission_group_edited
tags: [factorio-api, runtime, event]
---
# on_permission_group_edited

Called directly after a permission group is edited in some way.

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**
The player that did the editing or `nil` if by a mod.

### group
- **Type:** [[LuaPermissionGroup]]
The group being edited.

### type
- **Type:** `"add-permission"` | `"remove-permission"` | `"enable-all"` | `"disable-all"` | `"add-player"` | `"remove-player"` | `"rename"`
The edit type.

### action
- **Type:** [[defines.input_action]]
The action when the `type` is `"add-permission"` or `"remove-permission"`.

### other_player_index
- **Type:** [[uint32]]
The other player when the `type` is `"add-player"` or `"remove-player"`.

### old_name
- **Type:** [[string]]
The old group name when the `type` is `"rename"`.

### new_name
- **Type:** [[string]]
The new group name when the `type` is `"rename"`.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
