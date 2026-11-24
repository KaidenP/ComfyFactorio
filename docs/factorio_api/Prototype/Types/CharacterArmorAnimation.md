---
title: CharacterArmorAnimation
tags: [factorio-api, prototype, type]
---
# CharacterArmorAnimation

The data for one variation of [[CharacterPrototype#animations|character animations]].

## Properties

### idle
- **Type:** [[RotatedAnimation]]
- **Optional**

### idle_with_gun
- **Type:** [[RotatedAnimation]]

### running
- **Type:** [[RotatedAnimation]]
- **Optional**

### running_with_gun
- **Type:** [[RotatedAnimation]]
Must contain exactly 18 or 40 directions, so all of the combination of gun direction and moving direction can be covered. Some of these variations are used in reverse to save space. You can use the character animation in the base game for reference.

### mining_with_tool
- **Type:** [[RotatedAnimation]]

### flipped_shadow_running_with_gun
- **Type:** [[RotatedAnimation]]
- **Optional**
flipped_shadow_running_with_gun must be nil or contain exactly 18 directions, so all of the combination of gun direction and moving direction can be covered. Some of these variations are used in reverse to save space. You can use the character animation in the base game for reference. `flipped_shadow_running_with_gun` has to have same frame count as `running_with_gun`.

### idle_in_air
- **Type:** [[RotatedAnimation]]
- **Optional**

### idle_with_gun_in_air
- **Type:** [[RotatedAnimation]]
- **Optional**

### flying
- **Type:** [[RotatedAnimation]]
- **Optional**

### flying_with_gun
- **Type:** [[RotatedAnimation]]
- **Optional**
Must contain exactly 18 or 40 directions, so all of the combination of gun direction and moving direction can be covered. Some of these variations are used in reverse to save space. You can use the character animation in the base game for reference.

### take_off
- **Type:** [[RotatedAnimation]]
- **Optional**

### landing
- **Type:** [[RotatedAnimation]]
- **Optional**

### armors
- **Type:** array<[[ItemID (type)]]>
- **Optional**
The names of the armors this animation data is used for. Don't define this if you want the animations to be used for the player without armor.

### smoke_in_air
- **Type:** array<[[SmokeSource (type)]]>
- **Optional**
Smoke generator for when in air.

### smoke_cycles_per_tick
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Will be clamped to range [0, 1000]. When the character is flying, each [[SmokeSource (type)|SmokeSource]] in `smoke_in_air` will generate `smoke_cycles_per_tick` * [[SmokeSource (type)#frequency|SmokeSource::frequency]] smokes per tick on average.

### extra_smoke_cycles_per_tile
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Will be clamped to range [0, 1000]. When the character is flying, each [[SmokeSource (type)|SmokeSource]] in `smoke_in_air` will generate `extra_smoke_cycles_per_tile` * [[SmokeSource (type)#frequency|SmokeSource::frequency]] additional smokes per tile moved.

### mining_with_tool_particles_animation_positions
- **Type:** array<[[float (type)]]>
- **Optional**
List of positions in the mining with tool animation when the mining sound and mining particles are created.

Overrides [[CharacterPrototype#mining_with_tool_particles_animation_positions|CharacterPrototype::mining_with_tool_particles_animation_positions]] if defined.
