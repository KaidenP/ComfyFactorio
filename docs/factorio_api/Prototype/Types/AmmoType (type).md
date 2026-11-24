---
title: AmmoType
tags: [factorio-api, prototype, type]
---
# AmmoType

*Note: `AmmoType (type)`.*

Definition of actual parameters used in attack.

## Properties

### action
- **Type:** [[Trigger]]
- **Optional**
Describes actions taken upon attack happening.

### clamp_position
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When true, the gun will be able to shoot even when the target is out of range. Only applies when `target_type` equals `"position"`. The gun will fire at the maximum range in the direction of the target position.

### force_clamp_to_max_range
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If true, attacks will always be clamped to max range even if the target is within range. Used for shotguns.

### energy_consumption
- **Type:** [[Energy]]
- **Optional**
Energy consumption of a single shot, if applicable.

### range_modifier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Affects the `range` value of the shooting gun prototype's [[BaseAttackParameters]] to give a modified maximum range. The `min_range` value of the gun is unaffected.

This has no effect on artillery turrets and wagons even though the bonus appears in the GUI. [Forum thread](https://forums.factorio.com/103658).

### cooldown_modifier
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`

### consumption_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`

### target_type
- **Type:** `"entity"` | `"position"` | `"direction"`
- **Optional**
- **Default:** `"entity"`
`"entity"` fires at an entity, `"position"` fires directly at a position, `"direction"` fires in a direction.

If this is `"entity"`, `clamp_position` is forced to be `false`.

### source_type
- **Type:** [[AmmoSourceType]]
- **Optional**
Only exists (and is then mandatory) if the [[AmmoItemPrototype#ammo_type|AmmoItemPrototype::ammo_type]] this AmmoType is defined on has multiple ammo types.

Defines for which kind of entity this ammo type applies. Each entity kind can only be used once per array.

### target_filter
- **Type:** array<[[EntityID (type)]]>
- **Optional**
List of entities that can be targeted by this ammo type.
