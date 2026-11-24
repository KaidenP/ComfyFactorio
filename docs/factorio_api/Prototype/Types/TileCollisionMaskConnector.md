---
title: TileCollisionMaskConnector
tags: [factorio-api, prototype, type]
---
# TileCollisionMaskConnector

The base game provides common collision mask functions in a Lua file in the core [lualib](https://github.com/wube/factorio-data/blob/master/core/lualib/collision-mask-util.lua).

## Properties

### layers
- **Type:** dictionary<[[CollisionLayerID (type)]] → `true`>
Every key in the dictionary is the name of one [[CollisionLayerPrototype|layer]] the object collides with. The value is meaningless and always `true`. An empty table means that no layers are set.
