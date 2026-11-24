---
title: TileCollisionMask
tags: [factorio-api, runtime, concept]
---
# TileCollisionMask

## Fields

### layers
- **Type:** dictionary<[[string]] → `true`>
Every key in the dictionary is the name of one [[LuaCollisionLayerPrototype|layer]] the object collides with. The value is meaningless and always `true`. An empty table means that no layers are set.
