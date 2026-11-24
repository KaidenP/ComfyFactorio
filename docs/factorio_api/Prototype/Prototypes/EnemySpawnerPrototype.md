---
title: EnemySpawnerPrototype
tags: [factorio-api, prototype]
---
# EnemySpawnerPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `unit-spawner`

Can spawn entities. Used for biter/spitter nests.

## Properties

### graphics_set
- **Type:** [[EnemySpawnerGraphicsSet]]

### max_count_of_owned_units
- **Type:** [[uint32 (type)]]
Count of enemies this spawner can sustain.

### max_count_of_owned_defensive_units
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** Value of `max_count_of_owned_units`
Count of defensive enemies this spawner can sustain. Defensive units are units with [[UnitAISettings (type)#join_attacks|UnitAISettings::join_attacks]] set to false. If set below [[EnemySpawnerPrototype#max_count_of_owned_units|EnemySpawnerPrototype::max_count_of_owned_units]], the difference will be the space reserved for non-defensive units.

### max_friends_around_to_spawn
- **Type:** [[uint32 (type)]]
How many friendly units are required within the [[EnemySpawnerPrototype#spawning_radius|EnemySpawnerPrototype::spawning_radius]] of this spawner for it to stop producing more units.

### max_defensive_friends_around_to_spawn
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** Value of `max_friends_around_to_spawn`
How many friendly defensive units are required within the [[EnemySpawnerPrototype#spawning_radius|EnemySpawnerPrototype::spawning_radius]] of this spawner for it to stop producing more units. Defensive units are units with [[UnitAISettings (type)#join_attacks|UnitAISettings::join_attacks]] set to false. If set below [[EnemySpawnerPrototype#max_friends_around_to_spawn|EnemySpawnerPrototype::max_friends_around_to_spawn]], the difference will be the space reserved for non-defensive units.

### spawning_cooldown
- **Type:** ([[double (type)]], [[double (type)]])
Ticks for cooldown after unit is spawned. The first member of the tuple is min, the second member of the tuple is max.

The resulting spawning cooldown is a linear interpolation between min and max based on the current evolution factor.

### spawning_radius
- **Type:** [[double (type)]]
How far from the spawner can the units be spawned.

### spawning_spacing
- **Type:** [[double (type)]]
What spaces should be between the spawned units.

### max_richness_for_spawn_shift
- **Type:** [[double (type)]]
Max richness to determine spawn shift. Spawn shift is a linear interpolation between 0 and max_spawn_shift.

### max_spawn_shift
- **Type:** [[double (type)]]
Caps how much richness can be added on top of evolution when spawning units. [See also](https://www.reddit.com/r/factorio/comments/8pjscm/friday_facts_246_the_gui_update_part_3/e0bttnp/)

### call_for_help_radius
- **Type:** [[double (type)]]

### time_to_capture
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`

### spawn_blocked_trigger
- **Type:** [[Trigger]]
- **Optional**
Trigger that is activated when the spawner cannot find a valid spawn location.

### result_units
- **Type:** array<[[UnitSpawnDefinition (type)]]>
Array of the [[EntityPrototype|entities]] that this spawner can spawn and their spawn probabilities. The sum of probabilities is expected to be 1.0. The array must not be empty.

### dying_sound
- **Type:** [[Sound]]
- **Optional**

### absorptions_per_second
- **Type:** dictionary<[[AirbornePollutantID]] → [[EnemySpawnerAbsorption (type)]]>
- **Optional**

### min_darkness_to_spawn
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`

### max_darkness_to_spawn
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### spawn_decorations_on_expansion
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether `spawn_decoration` should be spawned when enemies [expand](https://wiki.factorio.com/Enemies#Expansions).

### spawn_decoration
- **Type:** array<[[CreateDecorativesTriggerEffectItem]]>
- **Optional**
Decoratives to be created when the spawner is created by the [map generator](https://wiki.factorio.com/Map_generator). Placed when enemies expand if `spawn_decorations_on_expansion` is set to true.

### captured_spawner_entity
- **Type:** [[EntityID (type)]]
- **Optional**

### is_military_target
- **Type:** `true`
- **Optional**
- **Default:** `true`
- **Overrides parent**
Whether this prototype should be a high priority target for enemy forces. See [Military units and structures](https://wiki.factorio.com/Military_units_and_structures).

### allow_run_time_change_of_is_military_target
- **Type:** `false`
- **Optional**
- **Default:** `false`
- **Overrides parent**
If this is true, this entities `is_military_target property` can be changed runtime (on the entity, not on the prototype itself).
