---
title: Mountain Fortress v3 — Overview
aliases:
  - mountain fortress
  - mtn
  - mountain_fortress
tags:
  - factorio
  - mountain-fortress
  - scenario
---

# Mountain Fortress v3 — Overview

> [!abstract] The pitch
> "Diggy diggy choo choo with Space Age!" — a team escorts a **train** through
> procedurally generated terrain zones while **wave defense** biters attack and a
> **collapse** (void wall) chases from behind. The train's health is the shared
> win/loss condition.

Maintained by **Gerkiz**, hosted by **Comfy**.

## Core gameplay loop

1. The team spawns around a **locomotive + cargo wagon** (their mobile base).
2. A procedurally generated map extends ahead in one direction (south by
   default, [[#orientation|reversible]]), divided into **zones** (each
   `zone_depth = 704` tiles deep, `zone_width = 510` wide).
3. [[mountain_fortress/dependencies#wave-defense|Wave Defense]] spawns escalating
   waves of biters that target the train.
4. A **collapse** (void wall) advances toward the train; players must keep the
   train moving forward or be consumed.
5. Players mine resources, buy upgrades at the [[mountain_fortress/systems#markets|train
   market]], complete objectives, and push deeper into harder zones.
6. **Win** by surviving to the final battle and completing the stateful
   objectives; **lose** when the locomotive is destroyed.

## Where the code lives

```text
maps/mountain_fortress_v3/
├── main.lua                 # entry point + wiring
├── core.lua                 # module aggregator (attaches everything to Public)
├── table.lua                # the central state table (the "one table to rule them all")
├── functions.lua            # shared helper functions
├── orientation.lua          # map direction / coordinate math
├── terrain.lua              # biome/zone generation (~6k lines)
├── generate.lua             # chunk generation driver
├── get_perlin.lua           # multi-octave noise templates
├── surface.lua              # surface creation / clearing
├── tasks.lua                # scenario task state machine (map reset/init)
├── entities.lua             # mining events, loot, game-over
├── balance.lua              # enemy weapon damage scaling
├── commands.lua             # admin commands
├── gui.lua                  # main HUD + spectate UI
├── mining.lua               # mining output replacement
├── loot.lua / loot_raffle.lua
├── resource_generator.lua   # "magic crafting" wild buildings
├── mystical_chest.lua       # team requester-chest objective
├── basic_markets.lua        # wild market entities
├── biters_yield_coins.lua   # coins on biter kills
├── breached_wall.lua        # map progression / wall breaches
├── buried_enemies.lua       # "dug up" enemy spawner
├── traps.lua                # tick-tack traps
├── flag_mission.lua / flag_rewards.lua   # capture-the-flag side missions
├── relay_station.lua        # abandoned relay stations
├── charging_station.lua     # armor charging button (local copy)
├── rocks_yield_ore_veins.lua
├── highscore.lua / season_highscore.lua / mvp_history.lua
├── soft_reset.lua           # soft-reset implementation
├── ic/                      # in-car vehicle interiors
├── icw/                     # immersive cargo wagon interiors + linked chests
├── locomotive/              # train systems (market, defense, pet, permissions, spawn)
└── stateful/                # persistent progression across resets/seasons
```

## Bootstrap order

1. `main.lua` fails hard if `MtnFortressAddons` is missing, then `require`s a few
   modules and `maps.mountain_fortress_v3.ic.main`.
2. `core.lua` `require`s `table.lua` first, then attaches every subsystem onto
   the single shared `Public` table.
3. `Event.on_init` runs `Public.init_mtn()` (configures wave defense, RPG,
   collapse, explosives, autostash, difficulty GUI, destructible tiles), then
   builds the minerals/enemies lookup tables.
4. The [[mountain_fortress/systems#tasks-the-scenario-task-state-machine|tasks.lua
   state machine]] drives map reset → surface creation → locomotive spawn →
   teleport players → announce.

## The central state table

`table.lua` holds **one table to rule them all**. Its API:

| Function | Purpose |
| --- | --- |
| `Public.get(key)` / `Public.set(key, value)` | Read/write main state (whole table if no key). |
| `Public.get_stateful_settings(key)` / `set_stateful_settings(key, value)` | Cross-run settings (direction, reversed, current_planet, darkness). |
| `Public.get_stateful(key)` / `set_stateful(key, value)` | Stateful meta-progression (added by `stateful/table.lua`). |
| `Public.set_task(task, surface_name)` / `is_task_done()` | Drive the scenario task state machine. |
| `Public.teleport_player(player, pos, surface)` | Safe teleport (handles remote view). |
| `Public.reset_main_table()` | Reset the entire runtime state (the canonical field inventory). |
| `Public.save_stateful_settings()` | Persist stateful settings to backend. |

Key constants:

- `Public.zone_settings = { zone_depth = 704, zone_width = 510 }`
- `Public.all_planets` / `planets` — `fortress, fulgora, gleba, vulcanus, nauvis`
  (`aquilo` commented out).
- `Public.is_modded` / `is_modded_pt2` — detects `MtnFortressAddons` /
  `MtnFortressAddonsPt2`.
- `Public.pickaxe_upgrades` — ~60 ordered pickaxe tiers.
- `Public.quality_per_level` / `quality_per_level_objectives` — quality tiers per
  RPG/objective level.

## Orientation

`orientation.lua` lets the map be authored once in a **logical vertical layout**
(progression along Y, lateral along X) and played in any of four directions.

- `Orient.get_direction()` → `north|south|east|west`.
- `Orient.is_horizontal()` → true for `east`/`west` (endless ribbon).
- `Orient.is_reversed()` → true for `north`/`west`.
- `Orient.progression(pos)` → the forward axis; `Orient.lateral(pos)` → the side
  axis.
- `Orient.zone_width()` / `Orient.spawn_len(n)` — scale lateral dimensions for
  horizontal (16:9) maps.

Everything position-sensitive (collapse axis, spawn positions, map-width clamps,
zone indexing, entity facing) goes through `Orient.*` to stay direction-agnostic.

## Currencies & counters

| Currency | What it is | Earned | Spent |
| --- | --- | --- | --- |
| **Coins** | Physical `coin` item | Biter kills, loot, flags, mystical chest, market sales | Wild markets, train market upgrades |
| **XP** | RPG global pool | Kills, flags, mystical chest, breaches | RPG levels, spells |
| **VMG (magicka)** | RPG spell mana | RPG regen | Casting spells |
| **Minerals** | Mined mineral entity counter | Mining | Objectives only |
| **Ore veins** | Statistic | Mining-triggered patches | — |

See [[mountain_fortress/systems#economy]] for the full flow.

## Related

- [[mountain_fortress/systems]] — per-file deep dive.
- [[mountain_fortress/submodules]] — `ic`, `icw`, `locomotive`, `stateful`.
- [[mountain_fortress/dependencies]] — the `modules/` this scenario builds on.
- [[hosting]]
