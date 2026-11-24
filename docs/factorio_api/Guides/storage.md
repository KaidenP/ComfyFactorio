---
title: storage
tags: [factorio-api, guide]
---
## Storage

During the lifetime of a mod, it will frequently want to save mutable data. Although mods are free to store such data in any variable, the game will not persist these through the save/load cycle.

To address this, Factorio provides the `storage` table: a Lua global variable that is serialized and persisted between saving and loading of a map. Each mod has access to its own instance of this table, so there is no need to worry about namespacing. Circular references are handled properly as well.

Before 2.0, the `storage` table was called `global`.

------------------------------------------------------------------------

The [[data-lifecycle|Data Lifecycle]] lays out some restrictions to accessing the `storage` table. Importantly, the table is not yet restored during the `control.lua` step, and will be overwritten just before `on_load`. Additionally, it is disallowed to write to `storage` during `on_load`, as doing so will lead to an error to prevent desyncs.

Only specific data can be stored in `storage`:

- Basic data: `nil`, strings, numbers, booleans.
- Tables, with limited metatables:
  - The metatable itself will not be saved.
  - Metatables that are registered with [[LuaBootstrap#register_metatable|LuaBootstrap::register_metatable]] will be recorded by name and automatically relinked to the registered table on loading.
  - Any other metatables will be removed; tables with unregistered metatables become plain tables when saved and loaded.
- References to Factorio's LuaObjects.

Functions are not allowed in `storage` and will throw an error when saving.

