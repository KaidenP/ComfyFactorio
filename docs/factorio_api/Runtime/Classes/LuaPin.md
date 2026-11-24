---
title: LuaPin
tags: [factorio-api, runtime, class]
---
# LuaPin

A map pin owned by a player.

## Attributes

### index
- **Type:** [[uint32]]
The index of this pin. The index is unique to this player.

Note that this index has no correlation to the position of the pin within [[LuaPlayer#get_pins|LuaPlayer::get_pins]].

### owner
- **Type:** [[LuaPlayer]]
The player that this pin belongs to.

### player
- **Type:** [[LuaPlayer]]
- **Writable:** [[PlayerIdentification]]
- **Optional**
The player that this pin targets, if any.

### targets
- **Type:** array<[[LuaEntity]]>
- **Writable:** array<[[LuaEntity]]>
The entities that this pin targets, if any.

### surface_index
- **Type:** [[uint32]]
- **Writable:** [[uint32]]
- **Optional**
The surface index if this pin specifically targets a surface and position.

When writing, and this pin was not bound to a specific surface and position, the default position of `{0, 0}` is used.

### position
- **Type:** [[MapPosition]]
- **Writable:** [[MapPosition]]
- **Optional**
The position if this pin specifically targets a surface and position.

When writing, and this pin was not bound to a specific surface and position, the default surface of nauvis is used.

### chart_tag
- **Type:** [[LuaCustomChartTag]]
- **Writable:** [[LuaCustomChartTag]]
- **Optional**
The custom chart tag, if this pin specifically targets a chart tag.

The chart tag must be on the same force as the [[LuaPin#owner|owning player]].

### label
- **Type:** [[string]]
- **Writable:** [[string]]
The label for this pin, if any. This will be an empty string if there is no label set.

### always_visible
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### preview_distance
- **Type:** [[uint16]]
- **Writable:** [[uint16]]
The radius (in tiles) that is shown in the tooltip for this pin.

### alert_type
- **Type:** [[defines.alert_type]]
- **Writable:** [[defines.alert_type]]
- **Optional**
The type of alert this pin is for, if this pin targets an alert.

### alert_positions
- **Type:** array<[[MapPosition]]>
- **Writable:** array<[[MapPosition]]>
The alert positions, if this pin targets an alert.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### destroy
Destroys this pin.

### get_pin_center
The center of this pin if it can be computed.

**Returns:**
- [[MapPosition]] *(optional)*
