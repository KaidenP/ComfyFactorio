---
title: SpritePath
tags: [factorio-api, runtime, concept]
---
# SpritePath

It can be either the name of a [[SpritePrototype]] defined in the data stage, or a path in form "type/name" or "type.name".

The validity of a SpritePath can be verified at runtime using [[LuaHelpers#is_valid_sprite_path|LuaHelpers::is_valid_sprite_path]].

## Type

[[string]]

The supported types are:

- `"item"` - for example "item/iron-plate" is the icon sprite of iron plate
- `"entity"` - for example "entity/small-biter" is the icon sprite of the small biter
- `"technology"`
- `"recipe"`
- `"fluid"`
- `"tile"`
- `"item-group"`
- `"virtual-signal"`
- `"shortcut"`
- `"achievement"`
- `"equipment"`
- `"ammo-category"`
- `"decorative"`
- `"space-connection"`
- `"space-location"`
- `"surface"`
- `"airborne-pollutant"`
- `"asteroid-chunk"`
- `"quality"`
- `"file"` - path to an image file located inside the current scenario. This file is not preloaded so it will be slower; for frequently used sprites, it is better to define sprite prototype and use it instead.
- `"utility"` - sprite defined in the utility-sprites object, these are the pictures used by the game internally for the UI.
