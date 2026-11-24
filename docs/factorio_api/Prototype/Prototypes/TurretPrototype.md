---
title: TurretPrototype
tags: [factorio-api, prototype]
---
# TurretPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `turret`

A turret that needs no extra ammunition. See the children for turrets that need some kind of ammunition.

## Properties

### attack_parameters
- **Type:** [[AttackParameters (type)]]
Requires ammo_type in attack_parameters unless this is a [[AmmoTurretPrototype]].

### folded_animation
- **Type:** [[RotatedAnimation8Way]]

### call_for_help_radius
- **Type:** [[double (type)]]

### attack_target_mask
- **Type:** [[TriggerTargetMask (type)]]
- **Optional**
- **Default:** all masks

### ignore_target_mask
- **Type:** [[TriggerTargetMask (type)]]
- **Optional**
- **Default:** no masks

### shoot_in_prepare_state
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### start_attacking_only_when_can_shoot
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When `false` the turret will enter `starting_attack` state without checking its ammo or energy levels. [[FluidTurretPrototype]] forces this to `true`.

### leave_attacking_if_shoot_fails
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### turret_base_has_direction
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When `true` the turret's collision box will affected by its rotation.

### random_animation_offset
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### attack_from_start_frame
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### allow_turning_when_starting_attack
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### gun_animation_secondary_draw_order
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`

### gun_animation_render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### graphics_set
- **Type:** [[TurretGraphicsSet]]

### preparing_animation
- **Type:** [[RotatedAnimation8Way]]
- **Optional**

### prepared_animation
- **Type:** [[RotatedAnimation8Way]]
- **Optional**

### prepared_alternative_animation
- **Type:** [[RotatedAnimation8Way]]
- **Optional**

### starting_attack_animation
- **Type:** [[RotatedAnimation8Way]]
- **Optional**

### attacking_animation
- **Type:** [[RotatedAnimation8Way]]
- **Optional**

### energy_glow_animation
- **Type:** [[RotatedAnimation8Way]]
- **Optional**

### resource_indicator_animation
- **Type:** [[RotatedAnimation8Way]]
- **Optional**

### ending_attack_animation
- **Type:** [[RotatedAnimation8Way]]
- **Optional**

### folding_animation
- **Type:** [[RotatedAnimation8Way]]
- **Optional**

### integration
- **Type:** [[Sprite]]
- **Optional**

### special_effect
- **Type:** [[TurretSpecialEffect]]
- **Optional**

### glow_light_intensity
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
The intensity of light in the form of `energy_glow_animation` drawn on top of `energy_glow_animation`.

### energy_glow_animation_flicker_strength
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.2`
The range of the flickering of the alpha of `energy_glow_animation`. Default is range 0.2, so animation alpha can be anywhere between 0.8 and 1.0.

### starting_attack_sound
- **Type:** [[Sound]]
- **Optional**

### dying_sound
- **Type:** [[Sound]]
- **Optional**

### preparing_sound
- **Type:** [[Sound]]
- **Optional**

### folding_sound
- **Type:** [[Sound]]
- **Optional**

### prepared_sound
- **Type:** [[Sound]]
- **Optional**

### prepared_alternative_sound
- **Type:** [[Sound]]
- **Optional**

### rotating_sound
- **Type:** [[InterruptibleSound]]
- **Optional**

### default_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### default_speed_secondary
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed`

### default_speed_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed`

### default_starting_progress_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`

### rotation_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed`

### rotation_speed_secondary
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_secondary`

### rotation_speed_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_when_killed`

### rotation_starting_progress_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_starting_progress_when_killed`

### preparing_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed`
Controls the speed of the preparing_animation: `1 ÷ preparing_speed = duration of the preparing_animation`

### preparing_speed_secondary
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_secondary`

### preparing_speed_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_when_killed`

### preparing_starting_progress_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_starting_progress_when_killed`

### folded_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed`
It's randomized whether a particular turret uses the primary or the secondary speed for its animations.

Controls the speed of the folded_animation: `1 ÷ folded_speed = duration of the folded_animation`

### folded_speed_secondary
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_secondary`
It's randomized whether a particular turret uses the primary or the secondary speed for its animations.

Controls the speed of the folded_animation: `1 ÷ folded_speed_secondary = duration of the folded_animation`

### folded_speed_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_when_killed`

### folded_starting_progress_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_starting_progress_when_killed`

### prepared_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed`
It's randomized whether a particular turret uses the primary or the secondary speed for its animations.

Controls the speed of the prepared_animation: `1 ÷ prepared_speed = duration of the prepared_animation`

### prepared_speed_secondary
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_secondary`
It's randomized whether a particular turret uses the primary or the secondary speed for its animations.

Controls the speed of the prepared_animation: `1 ÷ prepared_speed_secondary = duration of the prepared_animation`

### prepared_speed_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_when_killed`

### prepared_starting_progress_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_starting_progress_when_killed`

### prepared_alternative_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed`
It's randomized whether a particular turret uses the primary or the secondary speed for its animations.

Controls the speed of the prepared_alternative_animation: `1 ÷ prepared_alternative_speed = duration of the prepared_alternative_animation`

### prepared_alternative_speed_secondary
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_secondary`
It's randomized whether a particular turret uses the primary or the secondary speed for its animations.

Controls the speed of the prepared_alternative_animation: `1 ÷ prepared_alternative_speed_secondary = duration of the prepared_alternative_animation`

### prepared_alternative_speed_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_when_killed`

### prepared_alternative_starting_progress_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_starting_progress_when_killed`

### prepared_alternative_chance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
The chance for `prepared_alternative_animation` to be used.

### starting_attack_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed`
Controls the speed of the starting_attack_animation: `1 ÷ starting_attack_speed = duration of the starting_attack_animation`

### starting_attack_speed_secondary
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_secondary`

### starting_attack_speed_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_when_killed`

### starting_attack_starting_progress_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_starting_progress_when_killed`

### attacking_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Controls the speed of the attacking_animation: `1 ÷ attacking_speed = duration of the attacking_animation`

### ending_attack_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed`
Controls the speed of the ending_attack_animation: `1 ÷ ending_attack_speed = duration of the ending_attack_animation`

### ending_attack_speed_secondary
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_secondary`

### ending_attack_speed_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_when_killed`

### ending_attack_starting_progress_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_starting_progress_when_killed`

### folding_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed`
Controls the speed of the folding_animation: `1 ÷ folding_speed = duration of the folding_animation`

### folding_speed_secondary
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_secondary`

### folding_speed_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_speed_when_killed`

### folding_starting_progress_when_killed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** Value of `default_starting_progress_when_killed`

### prepare_range
- **Type:** [[double (type)]]
- **Optional**
- **Default:** The range defined in the `attack_parameters`

### alert_when_attacking
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### spawn_decorations_on_expansion
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether `spawn_decoration` should be spawned when this turret is created through [enemy expansion](https://wiki.factorio.com/Enemies#Expansions).

### folded_animation_is_stateless
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### unfolds_before_dying
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### spawn_decoration
- **Type:** array<[[CreateDecorativesTriggerEffectItem]]>
- **Optional**
Decoratives to be created when the spawner is created by the [map generator](https://wiki.factorio.com/Map_generator). Placed when enemies expand if `spawn_decorations_on_expansion` is set to true.

### folded_state_corpse
- **Type:** [[EntityID (type)]] | array<[[EntityID (type)]]>
- **Optional**

### can_retarget_while_starting_attack
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### is_military_target
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
Whether this prototype should be a high priority target for enemy forces. See [Military units and structures](https://wiki.factorio.com/Military_units_and_structures).

### circuit_wire_max_distance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The maximum circuit wire distance for this entity.

### draw_copper_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### draw_circuit_wires
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### circuit_connector
- **Type:** array<[[CircuitConnectorDefinition]]>
- **Optional**
Set of [[CircuitConnectorDefinition|circuit connector definitions]] for all directions used by this turret. Required amount of elements is based on other prototype values: 8 elements if building-direction-8-way flag is set, or 16 elements if building-direction-16-way flag is set, or 4 elements if turret_base_has_direction is set to true, or 1 element.
