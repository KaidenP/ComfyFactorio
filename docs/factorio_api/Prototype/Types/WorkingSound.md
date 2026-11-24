---
title: WorkingSound
tags: [factorio-api, prototype, type]
---
# WorkingSound

> **Parent:** [[MainSound]]

This type is used to produce sound from in-game entities when they are working/idle.

## Type

struct | [[Sound]]

## Properties

### main_sounds
- **Type:** [[MainSound]] | array<[[MainSound]]>
- **Optional**
If this property is defined, all properties inherited from MainSound (and not overridden here) are ignored.

### max_sounds_per_prototype
- **Type:** [[uint8 (type)]]
- **Optional**
Sets a maximum limit on how many entities of the same prototype will play their working sound.

Inactive entities without an `idle_sound` don't count towards this limit.

Entities with their working sound fading out don't count towards this limit.

Unused when `persistent` is `true`.

### extra_sounds_ignore_limit
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If `true`, entities playing their extra sound don't count towards `max_sounds_per_prototype` limit. 'extra sound' refers to `idle_sound`, `activate_sound` or `deactivate_sound`.

Unused when `persistent` is `true`.

### persistent
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When `true`, working sounds for all entities of the same prototype are combined into one.

### use_doppler_shift
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### idle_sound
- **Type:** [[Sound]]
- **Optional**
The sound to be played when the entity is idle. Might not work with all entities that use working_sound.

Unused when `persistent` is `true`.

### activate_sound
- **Type:** [[Sound]]
- **Optional**
Might not work with all entities that use working_sound.

Unused when `persistent` is `true`.

### deactivate_sound
- **Type:** [[Sound]]
- **Optional**
Might not work with all entities that use working_sound.

Unused when `persistent` is `true`.

### sound_accents
- **Type:** [[SoundAccent]] | array<[[SoundAccent]]>
- **Optional**
Unused when `persistent` is `true`.

## Examples

```
-- refinery
working_sound =
{
  sound = {filename = "__base__/sound/oil-refinery.ogg"},
  idle_sound = {filename = "__base__/sound/idle1.ogg", volume = 0.6},
}
```

```
-- roboport
working_sound =
{
  sound = {filename = "__base__/sound/roboport-working.ogg", volume = 0.6, audible_distance_modifier = 0.5},
  max_sounds_per_prototype = 3,
  probability = 1 / (5 * 60) -- average pause between the sound is 5 seconds
}
```
