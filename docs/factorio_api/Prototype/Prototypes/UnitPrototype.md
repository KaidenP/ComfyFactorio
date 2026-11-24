---
title: UnitPrototype
tags: [factorio-api, prototype]
---
# UnitPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `unit`

Entity that moves around and attacks players, for example [biters and spitters](https://wiki.factorio.com/Enemies#Creatures).

## Properties

### run_animation
- **Type:** [[RotatedAnimation]]

### steering
- **Type:** [[SteeringSettings (type)]]
- **Optional**

### attack_parameters
- **Type:** [[AttackParameters (type)]]
Requires `animation` in attack_parameters. Requires `ammo_type` in attack_parameters.

### warcry
- **Type:** [[Sound]]
- **Optional**
A sound this unit makes when it sets out to attack.

### movement_speed
- **Type:** [[float (type)]]
Movement speed of this unit in the world, in tiles per tick. Must be equal to or greater than 0.

### distance_per_frame
- **Type:** [[float (type)]]
How fast the `run_animation` frames are advanced. The animations are advanced animation_speed frames per `distance_per_frame` that the unit moves.

`frames_advanced = (distance_moved ÷ distance_per_frame) * animation_speed`

### distraction_cooldown
- **Type:** [[uint32 (type)]]

### vision_distance
- **Type:** [[double (type)]]
Max is 100.

Note: Setting to 50 or above can lead to undocumented behavior of individual units creating groups on their own when attacking or being attacked.

### rotation_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.025`

### dying_sound
- **Type:** [[Sound]]
- **Optional**
The sound file to play this unit dies.

### min_pursue_time
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `600`
In ticks.

### has_belt_immunity
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If this unit is immune to movement by belts.

### max_pursue_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `50`

### radar_range
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
In chunks. The radius of how many chunks this unit charts around itself.

### ai_settings
- **Type:** [[UnitAISettings (type)]]
- **Optional**

### move_while_shooting
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### can_open_gates
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### affected_by_tiles
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether this unit is affected by tile [[TilePrototype#walking_speed_modifier|walking speed modifiers]].

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### light
- **Type:** [[LightDefinition]]
- **Optional**

### absorptions_to_join_attack
- **Type:** dictionary<[[AirbornePollutantID]] → [[float (type)]]>
- **Optional**
The pollution amount that has to be absorbed by the unit's [[EnemySpawnerPrototype|spawner]] before the unit will leave the spawner and attack the source of the pollution.

### spawning_time_modifier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Multiplier for the [[EnemySpawnerPrototype#spawning_cooldown|EnemySpawnerPrototype::spawning_cooldown]] after it spawns this unit.

### buildable_entities
- **Type:** array<[[EntityID (type)]]>
- **Optional**
A list of entity prototypes that this unit can build when given the build base command.

If empty or not specified, the unit cannot build anything.

### walking_sound
- **Type:** [[Sound]]
- **Optional**

### alternative_attacking_frame_sequence
- **Type:** [[UnitAlternativeFrameSequence]]
- **Optional**

### running_sound_animation_positions
- **Type:** array<[[float (type)]]>
- **Optional**
List of positions in the `run_animation` when the `walking_sound` is played.

Only loaded if `walking_sound` is defined.

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
