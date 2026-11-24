---
title: instrument
tags: [factorio-api, guide]
---
## Instrument Mode

Instrument Mode gives a mod the ability to inject extra code very early on in all Lua states. At most one mod may be enabled in Instrument Mode, using the command line argument `--instrument-mod modname`. This is intended to be used to provide mod development tools and other instrumentation, in combination with the Lua and the [[LuaProfiler]]. Multiplayer is disabled while an Instrument Mode mod is in use, as it is not desync-safe. The following additions to the usual [[data-lifecycle|Data Lifecycle]] apply:

### 1. The settings stage

If the Instrument Mode mod has an `instrument-settings.lua` file, it is loaded *before* all other mods. The settings stage then proceeds as normal.

### 2. The data stage

If the Instrument Mode mod has an `instrument-data.lua` file, it is loaded *before* all other mods. The data stage then proceeds as normal. If the Instrument Mode mod has an `instrument-after-data.lua` file, it is loaded *after* all other mods have completed their `data-final-fixes.lua` stage.

### 3. control.lua initialization

If the Instrument Mode mod has an `instrument-control.lua` file, it is loaded in *every* mod's Lua state before their own `control.lua` file. The control stage then proceeds as normal.

------------------------------------------------------------------------

#### Additional API members

When instrument mode is enabled, [[LuaGuiElement]] offers an additional attribute: `actual_size`. It returns the size that a GUI element actually is on screen, after any stretching and squashing was applied. Since this is only available in instrument mode, it's intended for development-related use only, not for user-facing mods.

This functionality is not normally available because the size of GUI elements is not part of game state, which means that reading it would desync.

