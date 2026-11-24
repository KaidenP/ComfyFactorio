---
title: Hosting & Running Mountain Fortress v3
aliases:
  - hosting
tags:
  - factorio
  - hosting
  - mountain-fortress
---

# Hosting & running Mountain Fortress v3

## What you need

- A Factorio server running a **stable** release (the repo targets latest stable).
- The **MtnFortressAddons** mod enabled. The scenario refuses to start without it:

  ```lua
  -- maps/mountain_fortress_v3/main.lua
  if not script.active_mods['MtnFortressAddons'] then
      error('Mtn Fortress Addons mod is not enabled! Please download it from the mod website.')
  end
  ```

- The scenario installed and launched through the **Comfy panel** (which reads
  the template files), or manually via `control.lua`.

## Enabling the map

In [[architecture|control.lua]], exactly one map is enabled by un-commenting its
`require`:

```lua
--![[Guide a Train through rough terrain, while defending it from the biters]]--
--require 'utils.templates.Mountain_Fortress_v3_BP.map_loader'
--require 'maps.mountain_fortress_v3.main'
```

> [!tip] Two entry points
> - `require 'maps.mountain_fortress_v3.main'` — the **normal game**.
> - `require 'utils.templates.Mountain_Fortress_v3_BP.map_loader'` — a
>   **creative blueprint server** (peaceful, no enemies, cheat mode).

## Template files

`utils/templates/` contains one folder per scenario, used by the Comfy backend:

- `utils/templates/Mountain_Fortress_v3/map_loader.lua`

  ```lua
  return require 'maps.mountain_fortress_v3.main'
  ```

- `utils/templates/Mountain_Fortress_v3/server_settings.json`

  ```json
  {
      "Name": "Mountain Fortress v3",
      "Description": "diggy diggy choo choo with Space Age!",
      "Scenario": "Mountain_Fortress_v3",
      "ModPack": "Mtn"
  }
  ```

  `ModPack: "Mtn"` tells the launcher to enable the Mountain Fortress mod set
  (including `MtnFortressAddons`).

### The `Mountain_Fortress_v3_BP` variant

`utils/templates/Mountain_Fortress_v3_BP/` (`ModPack: "Mtn-BP"`) is a
**blueprint server**: a peaceful, no-enemies Nauvis where the community keeps
blueprints. It loads the same `ic`/`icw` systems but overrides map generation
with creative freeplay settings and enables `cheat_mode` for players.

## Admin commands

Admins use the `/scenario` command (registered in `commands.lua`). See
[[mountain_fortress/systems#commands|the systems reference]] for the full list;
the main lifecycle actions are:

- `/scenario restart` — arm a **soft-reset** (progression carries over).
- `/scenario shutdown` — stop the server at the next reset point.
- `/scenario reset` — arm a hard reset.
- `/scenario restartnow` — restart the scenario immediately.

## Server lifecycle

- `main.lua` registers `Server.on_scenario_changed('Mountain_Fortress_v3', ...)`
  to react when the backend pushes a new scenario payload.
- Soft-resets are driven by `table.lua` (`soft_reset` / `restart` / `shutdown`
  flags plus a `game_reset_tick` countdown) and `soft_reset.lua`.
- Stateful progression (rounds survived, streaks, buffs) is persisted across
  soft-resets via `utils.datastore` / `utils.server` (`scenario_settings` →
  `mtn_v3_table`). See [[mountain_fortress/submodules#stateful-persistent-progression-across-soft-resets-and-seasons]].

## CI (`.github/workflows/`)

| Workflow | Purpose |
| --- | --- |
| `CI.yml` | Runs **luacheck** against the repo (`.luacheckrc`). |
| `CheckMaps.yml` | Verifies only one map is enabled in `control.lua`. |
| `AutoRelease.yml` | On push to `develop`, auto-bumps the version and creates a GitHub release. |

All three trigger on `push`/`pull_request` to `develop`.

## Mods vs scenario

The whole repository is a **scenario**, not a mod. `info.json` is empty (`{}`)
and `description.json` only sets ordering + `multiplayer-compatible` flags. The
actual mod content (ore minerals, Space Age planets, etc.) comes from the
external `MtnFortressAddons` / `MtnFortressAddonsPt2` mods.

## Related

- [[architecture]]
- [[mountain_fortress/overview]]
- [[mountain_fortress/systems]]
