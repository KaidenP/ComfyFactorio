---
title: SegmentPrototype
tags: [factorio-api, prototype]
---
# SegmentPrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `segment` · **Requires:** `space_age`

Entity representing an individual segment in a [[SegmentedUnitPrototype]]

## Properties

### dying_sound
- **Type:** [[Sound]]
- **Optional**
The sound to play when the entity dies.

If not specified, [[UtilitySounds#segment_dying_sound|UtilitySounds::segment_dying_sound]] is used.

### dying_sound_volume_modifier
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1.0`

### animation
- **Type:** [[RotatedAnimation]]
The animation to use of the entity.

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`
The layer to render the entity in.

### forward_overlap
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
The number of segments ahead of this one that should always be rendered atop this one, giving the illusion that at all orientations, those preceding segments overlap this current segment.

Must be 0 or greater, and the sum of `forward_overlap` and `backward_overlap` must be less than or equal to 4.

### backward_overlap
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
The number of segments behind this one that should always be rendered atop this one, giving the illusion that at all orientations, those following segments overlap this current segment.

Must be 0 or greater, and the sum of `forward_overlap` and `backward_overlap` must be less than or equal to 4.

### forward_padding
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The number of tiles of spacing to add in front of this segment. Can be negative. Scales with the segment scale when used in a [[SegmentEngineSpecification (type)|SegmentEngineSpecification]].

### backward_padding
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The number of tiles of spacing to add behind this segment. Can be negative. Scales with the segment scale when used in a [[SegmentEngineSpecification (type)|SegmentEngineSpecification]].

### update_effects
- **Type:** array<[[TriggerEffectWithCooldown (type)]]>
- **Optional**
The effects to trigger every tick.

### update_effects_while_enraged
- **Type:** array<[[TriggerEffectWithCooldown (type)]]>
- **Optional**
The effects to trigger every tick while enraged, in addition to `update_effects`.
