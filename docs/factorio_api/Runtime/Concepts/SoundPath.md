---
title: SoundPath
tags: [factorio-api, runtime, concept]
---
# SoundPath

It can be either the name of a [[SoundPrototype]] defined in the data stage, or a path in the form `"type/name"`. The latter option can be sorted into four categories.

The validity of a SoundPath can be verified at runtime using [[LuaHelpers#is_valid_sound_path|LuaHelpers::is_valid_sound_path]].

## Type

[[string]]

The utility and ambient types each contain general use sound prototypes defined by the game itself.

- `"utility"` - Uses [[UtilitySounds]]. Example: `"utility/wire_connect_pole"`
- `"ambient"` - Uses [[AmbientSound#sound|AmbientSound::sound]]. Variable sounds cannot be used. Example: `"ambient/resource-deficiency"`

The following types can be combined with any tile name as long as its prototype defines the corresponding sound.

- `"tile-walking"` - Uses [[TilePrototype#walking_sound|TilePrototype::walking_sound]]. Example: `"tile-walking/concrete"`
- `"tile-mined"` - Uses [[TilePrototype#mined_sound|TilePrototype::mined_sound]]
- `"tile-build-small"` - Uses [[TilePrototype#build_sound|TilePrototype::build_sound]]. Example: `"tile-build-small/concrete"`
- `"tile-build-medium"` - Uses [[TilePrototype#build_sound|TilePrototype::build_sound]]
- `"tile-build-large"` - Uses [[TilePrototype#build_sound|TilePrototype::build_sound]]

The following types can be combined with any entity name as long as its prototype defines the corresponding sound.

- `"entity-build"` - Uses [[EntityPrototype#build_sound|EntityPrototype::build_sound]]. Example: `"entity-build/wooden-chest"`
- `"entity-mined"` - Uses [[EntityPrototype#mined_sound|EntityPrototype::mined_sound]]
- `"entity-mining"` - Uses [[EntityPrototype#mining_sound|EntityPrototype::mining_sound]]
- `"entity-rotated"` - Uses [[EntityPrototype#rotated_sound|EntityPrototype::rotated_sound]]
- `"entity-open"` - Uses [[EntityPrototype#open_sound|EntityPrototype::open_sound]]
- `"entity-close"` - Uses [[EntityPrototype#close_sound|EntityPrototype::close_sound]]

The following types can be combined with any item name as long as its prototype defines the corresponding sound.

- `"item-open"` - Uses [[ItemPrototype#open_sound|ItemPrototype::open_sound]]. Example: `"item-open/modular-armor"`
- `"item-close"` - Uses [[ItemPrototype#close_sound|ItemPrototype::close_sound]]
- `"item-pick"` - Uses [[ItemPrototype#pick_sound|ItemPrototype::pick_sound]]. Example: `"item-pick/transport-belt"`
- `"item-drop"` - Uses [[ItemPrototype#drop_sound|ItemPrototype::drop_sound]]
- `"item-move"` - Uses [[ItemPrototype#inventory_move_sound|ItemPrototype::inventory_move_sound]]
