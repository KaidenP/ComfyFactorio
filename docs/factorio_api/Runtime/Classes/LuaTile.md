---
title: LuaTile
tags: [factorio-api, runtime, class]
---
# LuaTile

A single "square" on the map.

## Attributes

### name
- **Type:** [[string]]
Prototype name of this tile. E.g. `"sand-3"` or `"grass-2"`.

### prototype
- **Type:** [[LuaTilePrototype]]

### position
- **Type:** [[TilePosition]]
The position this tile references.

### hidden_tile
- **Type:** [[string]]
- **Optional**
The name of the [[LuaTilePrototype]] hidden under this tile, if any.

During normal gameplay, only [[LuaTilePrototype#mineable_properties|non-mineable]] or [[LuaTilePrototype#is_foundation|foundation]] tiles can become hidden. This can however be circumvented with [[LuaSurface#set_hidden_tile|LuaSurface::set_hidden_tile]].

### double_hidden_tile
- **Type:** [[string]]
- **Optional**
The name of the [[LuaTilePrototype]] double hidden under this tile or `nil` if there is no double hidden tile.

During normal gameplay, only [[LuaTilePrototype#mineable_properties|non-mineable]] tiles can become double hidden. This can however be circumvented with [[LuaSurface#set_double_hidden_tile|LuaSurface::set_double_hidden_tile]].

### surface
- **Type:** [[LuaSurface]]
The surface this tile is on.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### collides_with
What type of things can collide with this tile?

**Parameters:**
- **`layer`** — [[CollisionLayerID]]

**Returns:**
- [[boolean]]

**Examples:**

```
-- Check if the character would collide with a tile
game.player.print(tostring(game.player.surface.get_tile(1, 1).collides_with("player")))
```

### to_be_deconstructed
Is this tile marked for deconstruction?

**Parameters:**
- **`force`** — [[ForceID]] *(optional)*: The force whose robots are supposed to do the deconstruction. If not given, checks if to be deconstructed by any force.

**Returns:**
- [[boolean]]

### order_deconstruction
Orders deconstruction of this tile by the given force.

**Parameters:**
- **`force`** — [[ForceID]]: The force whose robots are supposed to do the deconstruction.
- **`player`** — [[PlayerIdentification]] *(optional)*: The player to set the last_user to if any.

**Returns:**
- [[LuaEntity]] *(optional)*: The deconstructible tile proxy created, if any.

**Raises:**
- [[on_marked_for_deconstruction]] *(timeframe: instantly)*: Raised if the tile was successfully marked for deconstruction.

### cancel_deconstruction
Cancels deconstruction if it is scheduled, does nothing otherwise.

**Parameters:**
- **`force`** — [[ForceID]]: The force who did the deconstruction order.
- **`player`** — [[PlayerIdentification]] *(optional)*: The player to set the last_user to if any.

**Raises:**
- [[on_cancelled_deconstruction]] *(timeframe: instantly)*: Raised if the tile's deconstruction was successfully cancelled.

### has_tile_ghost
Does this tile have any tile ghosts on it.

**Parameters:**
- **`force`** — [[ForceID]] *(optional)*: Check for tile ghosts of this force.

**Returns:**
- [[boolean]]

### get_tile_ghosts
Gets all tile ghosts on this tile.

**Parameters:**
- **`force`** — [[ForceID]] *(optional)*: Get tile ghosts of this force.

**Returns:**
- array<[[LuaEntity]]>: The tile ghosts.
