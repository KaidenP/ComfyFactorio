---
title: ScriptRenderTarget
tags: [factorio-api, runtime, concept]
---
# ScriptRenderTarget

When writing it is possible to give LuaEntity or MapPosition directly. However, reading always returns the full ScriptRenderTargetTable.

The full ScriptRenderTargetTable allows specifying cursor targets and an offset for entity targets.

If an entity target of an object (except its `orientation_target`) is destroyed or changes surface, then the object is also destroyed.

## Type

[[LuaEntity]] | [[MapPosition]] | [[ScriptRenderTargetTable]]

## Examples

```
target = some_lua_entity
```

```
target = {1, 4}
```

```
target = {type = "entity", entity = another_lua_entity, offset = {-0.5, 1}}
```

```
target = {type = "position", position = {2.5, 3}}
```

```
target = {type = "cursor", offset = {6, 7}}
```

```
target = {type = "build-cursor", offset = {3.2, -4.5}}
```
