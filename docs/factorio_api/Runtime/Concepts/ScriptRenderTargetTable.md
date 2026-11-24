---
title: ScriptRenderTargetTable
tags: [factorio-api, runtime, concept]
---
# ScriptRenderTargetTable

If an entity target of an object (except its `orientation_target`) is destroyed or changes surface, then the object is also destroyed.

Targets of type `"cursor"` draw at the position of the player's cursor.

Targets of type `"build-cursor"` draw at the position of the player's build cursor, including snapping to the build position. The offset is rotated by the entity's direction and mirrored if the entity to be built is mirrored. Recommended to be combined with [[ScriptRenderMode#build-cursor|ScriptRenderMode::build-cursor]].

## Fields

### type
- **Type:** `"entity"` | `"position"` | `"cursor"` | `"build-cursor"`
- **Optional**
Defaults to `"entity"` if `entity` is given. Defaults to `"position"` if `position` is given.

### entity
- **Type:** [[LuaEntity]]
- **Optional**
Only used, and mandatory if `type` is `entity`.

### offset
- **Type:** [[Vector]]
- **Optional**
Only used if `type` is `entity`, `cursor` or `build-cursor`. Defaults to `{0, 0}`.

### position
- **Type:** [[MapPosition]]
- **Optional**
Only used, and mandatory if `type` is `position`.

## Examples

```
{type = "entity", entity = some_lua_entity, offset = {-0.5, 1}}
```

```
{entity = some_lua_entity, offset = {-0.5, 1}} -- same target as previous example
```

```
{type = "position", position = {2.5, 3}}
```

```
{position = {2.5, 3}} -- same target as previous example
```

```
{type = "cursor", offset = {6, 7}}
```

```
{type = "build-cursor", offset = {3.2, -4.5}}
```
