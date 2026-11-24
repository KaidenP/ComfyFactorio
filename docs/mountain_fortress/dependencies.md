---
title: Mountain Fortress v3 — Dependencies
aliases:
  - mtn dependencies
  - dependencies
tags:
  - factorio
  - mountain-fortress
  - modules
---

# Mountain Fortress v3 — Dependencies

This scenario builds on the reusable `modules/` directory. This note documents
each module it loads and **how Mountain Fortress configures it**.

## Module require sites

```lua
-- main.lua
require 'modules.shotgun_buff'                       -- line 13
require 'modules.no_deconstruction_of_neutral_entities' -- line 14
require 'maps.mountain_fortress_v3.ic.main'          -- line 15
require 'modules.wave_defense.main'                  -- line 17
require 'modules.melee_mode'                         -- line 18
Autostash        = require 'modules.autostash'       -- line 32
Explosives       = require 'modules.explosives'      -- line 35
WD               = require 'modules.wave_defense.table' -- line 36
RPG              = require 'modules.rpg.main'        -- line 38
Collapse         = require 'modules.collapse'        -- line 39
Difficulty       = require 'modules.difficulty_vote_by_amount' -- line 40
BiterHealthBooster = require 'modules.biter_health_booster_v2' -- line 47
RobotLimits      = require 'modules.robot_limits'    -- line 49
```

## `modules/wave_defense/` — the wave engine

The core enemy-spawning/wave engine. Maintains wave number, threat, spawn
position, unit-group limits, per-wave health/damage scaling, unit raffles, boss
waves, pathing recovery, and GUI.

Mountain Fortress configures it in `init_mtn()` (and repeats in `tasks.lua`):

```lua
WD.alert_boss_wave(true)
WD.enable_side_target(false)
WD.remove_entities(true)
WD.enable_threat_log(false)          -- "creates waaaay too many entries"
WD.check_collapse_position(true)
WD.set_disable_threat_below_zero(true)
WD.increase_boss_health_per_wave(true)
WD.increase_damage_per_wave(true)
WD.increase_health_per_wave(true)
WD.increase_average_unit_group_size(true)
WD.increase_max_active_unit_groups(true)
WD.enable_random_spawn_positions(true)
WD.set_track_bosses_only(true)
WD.set_pause_waves_custom_callback(Public.pause_waves_custom_callback_token)
WD.set_threat_event_custom_callback(Public.check_if_spawning_near_train_custom_callback)
```

Other direct uses: `WD.get_wave()`, `WD.get('paused')`, `WD.set('wave_interval', 4500)`,
`WD.set_main_target(locomotive)`, `WD.disable_spawning_biters(...)`,
`WD.set('surface_index', ...)` (via `Public.set_wd_surface_index()`).

> [!note] Defaults worth knowing
> `max_active_biters = 1280`, `max_active_unit_groups = 32`,
> `wave_interval = 3600`, `threat_gain_multiplier = 2`. Boss waves every 50
> waves double threat gain and raise damage/health; every 200 waves increases
> max groups.

## `modules/rpg/` — XP / spells

Per-player stats (strength/dexterity/magicka/vitality, XP/level, spell slots,
cooldowns) + a global XP pool with personal tax. Spells summon walls/chests/
belts/biters/etc. via mana.

Mountain Fortress configures it in `tasks.lua`:

```lua
RPG.disable_cooldowns_on_spells()   -- called at require time in main.lua
RPG.enable_health_and_mana_bars(true)
RPG.enable_wave_defense(true)
RPG.enable_mana(true)
RPG.personal_tax_rate(0.4)
RPG.enable_stone_path(true)
RPG.enable_aoe_punch(true)
RPG.enable_aoe_punch_globally(false)
RPG.enable_range_buffs(true)
RPG.enable_auto_allocate(true)
RPG.enable_explosive_bullets_globally(true)
RPG.enable_explosive_bullets(false)
RPG.set_x_marks_the_spot_custom_callback(...)
RPG.set_magicka_custom_callback(...)
RPG.set_surface_validation_token(Public.surface_validation_token)
RPG.set_x_position(700, axis)
```

Also uses `RPG.gain_xp`, `RPG.get_magicka`, `RPG.add_to_global_pool`,
`RPG.get_value_from_player`, `RPG.set_rpg_xp_yield`, and
`RPG.register_spell_cast_validator` (used by flag missions to block spells while
carrying a flag).

## `modules/collapse.lua` — the void wall

A line sweeps across the surface converting tiles to `out-of-map` (void),
destroying/killing entities it passes. Supports main + reverse collapse, speed/
amount/force mode, and kill-specific-entity whitelists.

Key calls: `Collapse.get_position()`, `has_collapse_started()`,
`start_now()/reverse_start_now()`, `set_speed()/set_amount()/set_force_mode()`,
`set_surface_index()`, `set_position()/set_direction()`, `set_max_line_size()`,
`set_kill_specific_entities(collapse_kill)`.

> [!note] `collapse_kill`
> `main.lua` configures collapse to kill turrets, mines, trains/wagons,
> characters, vehicles, assemblers, furnaces, and steel chests — with
> `Public.fishy_callback_token` as the per-entity callback.

`Collapse.read_tables_only = true` is set by wave defense so collapse's own
`on_tick` isn't registered twice.

## `modules/difficulty_vote_by_amount.lua` — difficulty voting

3-tier voting GUI; the winning tier sets a scalar `value` used to scale enemy
damage/health and wave pacing.

Mountain Fortress: `Difficulty.set_gui_width(20)`, `Difficulty.show_gui(false)`,
`Difficulty.set_tooltip(...)`, `Difficulty.reset_difficulty_poll(...)`,
`Difficulty.get('value')`, `Difficulty.top_button_name`.

> [!note] `modules/difficulty_vote.lua` is **not** used by Mountain Fortress
> (it's a different 7-tier system used by a few other modules).

## `modules/biter_health_booster_v2.lua` — boss buffs

Adds a per-entity health pool (with boss health bars), acid nova on boss death,
projectile bursts, boss loot (disabled), and randomized stun/slowdown stickers.

Mountain Fortress: `acid_nova(true)`, `check_on_entity_died(true)`,
`boss_spawns_projectiles(true)`, `enable_boss_loot(false)`,
`enable_randomize_stun_and_slowdown_sticker(true)`, `set_module_state(true)`,
`set_active_surface(...)`, `add_unit(...)`, `add_boss_unit(...)`.

> [!note] `modules/biter_health_booster.lua` (old, `storage.*`-based) is **not**
> used.

## `modules/explosives.lua` — destructive tiles

Explosives turn into a spreading cell-based terrain/entity damage system;
destructible tiles convert to `nuclear-ground`. Containers/cars/wagons carrying
explosives explode on death.

Mountain Fortress configures ~26 destructible tiles (`out-of-map` 1500,
`void-tile` 1500, water family 1000, `lab-dark-2` 1000, lava 500, etc.), a
whitelist (rails + `character`/`spidertron`/`car`/`tank`), the growth axis and
sideways limit (`Orient.zone_width()/2`), and the void sign from orientation.

## `modules/autostash.lua` — auto-sort inventory

An "Autostash" button that sorts/stashes inventory into nearby chests, furnaces,
or cargo wagons.

Mountain Fortress: `Autostash.bottom_button(true)`,
`Autostash.insert_into_furnace(true)`, `Autostash.insert_into_wagon(true)`.

## `modules/shotgun_buff.lua`

No config — `require` only. Buffs shotgun-shell damage research by 4× on
`physical-projectile-damage` completion.

## `modules/melee_mode.lua`

No config — `require` only. Adds a melee-mode toggle that moves the gun/ammo out
of the weapon slots and back.

## `modules/no_deconstruction_of_neutral_entities.lua`

No config — `require` only. Prevents deconstructing neutral-force entities
(except cliffs and item-entities).

## `modules/robot_limits.lua`

Mountain Fortress **disables** it: `RobotLimits.enable(false)`.

## Modules Mountain Fortress does **not** use

These exist in `modules/` but are **not** part of this scenario:

- `modules/immersive_cargo_wagons/` — mtn has its own under
  [[mountain_fortress/submodules#icw-trainwagon-interiors--linked-chests|icw/]].
- `modules/fjei/` — recipe lookup GUI (commented out in `control.lua`).
- `modules/charging_station.lua` — mtn has a local copy at
  `maps/mountain_fortress_v3/charging_station.lua`.
- `modules/spawn_ent/` (incl. `mountainRange.lua`) — only used by
  `maps/oarc`; mtn builds its fortress structures directly in `terrain.lua`.

## Related

- [[mountain_fortress/overview]]
- [[mountain_fortress/systems]]
- [[mountain_fortress/submodules]]
- [[architecture]]
