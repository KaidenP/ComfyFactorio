---
title: Repository Architecture
aliases:
  - architecture
tags:
  - factorio
  - architecture
  - framework
---

# Repository architecture

This note describes how the ComfyFactorio codebase is organized and how the
shared framework works. Read it before diving into
[[mountain_fortress/overview|Mountain Fortress v3]].

## Top-level layout

```text
control.lua          # scenario entry point (loaded by Factorio)
map_loader.lua       # panel hook; empty no-op when not launched from the panel
info.json            # scenario metadata (empty object here)
description.json     # scenario ordering / multiplayer flags
readme.md
image.png
locale/              # localised strings (en, ru, de, zh-CN)
maps/                # one directory (or file) per scenario
modules/             # reusable, opt-in gameplay modules
utils/               # the shared framework every map builds on
utils/templates/     # per-scenario server templates (map_loader + server_settings.json)
.github/workflows/   # CI (lint, map checks, auto-release)
```

## How a scenario boots

Factorio loads `control.lua`. It first sets up the shared framework, then
**exactly one map is enabled** by un-commenting a single `require` line.

```lua
-- control.lua (abridged)
require 'utils.data_stages'       -- sets _STAGE.control, _DEBUG, etc.
require 'utils.server_commands'
require 'utils.gui.init'
-- ... more utils + always-on modules ...

---------------- ENABLE MAPS HERE ----------------
--require 'maps.mountain_fortress_v3.main'
```

Each map is a Lua module that wires itself up via the [[#the-event-system-utils-event|event
system]]. Only one map may be enabled at a time.

### The runtime `require` wrapper

At the bottom of `control.lua`, `require` is redefined:

```lua
local loaded = _G.package.loaded
function require(path)
    return loaded[ServerCommands.normalize_path(path)]
        or error('Can only require files at runtime that have been required in the control stage.', 2)
end
```

> [!warning] Every file must be loaded during the control stage
> You cannot `require` a brand-new path at runtime. The scenario deliberately
> restricts dynamic loading so the release pipeline can statically discover all
> code and avoid desyncs. **Add new files by `require`ing them from an
> already-loaded module — never on-demand.**

### Data stages

`utils/data_stages.lua` defines the global `_STAGE` lifecycle constants
(`control=4`, `init=5`, `load=6`, `config_change=7`, `runtime=8`). `control.lua`
sets `_LIFECYCLE = _STAGE.control`; scenario code always runs in the control
stage.

## The `utils/` framework

These are the building blocks every map uses.

| Module | Purpose |
| --- | --- |
| `utils.event` | Event system: `Event.add`, `Event.on_nth_tick`, `Event.on_init`, custom event names. |
| `utils.global` | Desync-safe persisted global state via `Global.register(tbl, on_load)`. |
| `utils.gui` | GUI framework: `Gui.uid_name()`, frames, buttons, bottom-frame/config panels. |
| `utils.server` | Server control + Discord: `start_scenario`, `stop_scenario`, `set_data`/`try_get_data`, `output_script_data`, `to_discord_*`. |
| `utils.commands` | Command builder: `Commands.new(name, help):require_admin():add_parameter(...):callback(fn)`. |
| `utils.datastore` | Server-side persistence (survives scenario restarts). Includes `session_data`, `rpg_prestige_data`, etc. |
| `utils.task` / `utils.task_token` | Deferred work: `Task.register`, `Task.set_timeout_in_ticks`, `Task.queue_task`. |
| `utils.alert` | Player notifications with per-player preference filters. |
| `utils.antigrief` | Grief protection: capsule warnings, jail, decon filters, damage thresholds. |
| `utils.color_presets` | Named color tables (`Color.green`, etc.). |
| `utils.math` | Math helpers (`clamp`, `floor`, `random`, …) + noise implementations. |
| `utils.surface` | Surface creation helpers. |
| `utils.remote_chunks` | Record/apply chunk data across surfaces. |
| `utils.table` / `utils.extended_table` | Table utilities (`deep_copy`, `shuffle_table`, `map`, `filter`, …). |
| `utils.freeplay` | Freeplay-mode toggles. |
| `utils.player_modifiers` | Character/force modifiers (used for RPG buffs). |

### The event system (`utils.event`)

The backbone of every map. `event_core.lua` is the low-level dispatcher that
allows **multiple handlers per event** (vanilla Factorio only allows one);
`event.lua` is the safe, public wrapper.

```lua
Event.add(defines.events.on_entity_died, function(event) ... end)
Event.on_nth_tick(40, function() ... end)   -- every 40 ticks
Event.on_init(function() ... end)
```

Custom cross-module events use `Event.generate_event_name('some_name')`.

### Global state (`utils.global`)

```lua
local this = { field = 1 }
Global.register(this, function(tbl) this = tbl end)
```

`this` is persisted into the save's `storage` and restored on load — this is how
every scenario stores mutable state.

## The `modules/` directory

Modules are self-contained, opt-in gameplay features. A map `require`s the ones
it wants and configures them through their public functions. See
[[mountain_fortress/dependencies]] for Mountain Fortress v3's full module list.

## The `maps/` directory

Each map is a directory (or single file) that `require`s its own files plus the
`modules/` it needs. Mountain Fortress v3 is in `maps/mountain_fortress_v3/` —
see [[mountain_fortress/overview]].

## Templates and hosting

`utils/templates/<Scenario>/` contains per scenario:

- `map_loader.lua` — usually `return require 'maps.<scenario>.main'`.
- `server_settings.json` — name, description, scenario folder, and **ModPack**.

See [[hosting]] for details.

## Related

- [[hosting]]
- [[mountain_fortress/overview]]
- [[mountain_fortress/dependencies]]
