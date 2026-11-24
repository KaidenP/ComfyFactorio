---
title: AmbientSound
tags: [factorio-api, prototype]
---
# AmbientSound

> **Type name:** `ambient-sound`

This prototype is used to make sound while playing the game. This includes the [base game's music](https://store.steampowered.com/app/436090/Factorio__Soundtrack/), composed by Daniel James Taylor and the [Space Age's music](https://store.steampowered.com/app/3311770/Factorio_Space_Age__Soundtrack/), composed by Petr Wajsar.

## Properties

### type
- **Type:** `"ambient-sound"`
Specification of the type of the prototype.

### name
- **Type:** [[string (type)]]
Unique textual identification of the prototype.

### title
- **Type:** [[string (type)]]
- **Optional**
Alternative name of the track. It doesn't need to be unique.

### weight
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Cannot be less than zero.

Cannot be defined if `track_type` is `"hero-track"` or `"script-track"`.

### track_type
- **Type:** [[AmbientSoundType]]

### planets
- **Type:** array<[[SpaceLocationID (type)]]>
- **Optional**
The track can play only on specified planets.

If neither `planets` nor `surface_names` is given, the track plays on space platforms and in the space map.

Cannot be defined if `track_type` is `"script-track"`.

Cannot be defined when `play_on_all_surfaces` is true.

### surface_names
- **Type:** array<[[string (type)]]>
- **Optional**
The track can play only on surfaces with specified names. It's enough if the specified name is a sub-string of the surface name.

If neither `planets` nor `surface_names` is given, the track plays on space platforms and in the space map.

Cannot be defined if `track_type` is `"hero-track"` or `"script-track"`.

Cannot be defined when `play_on_all_surfaces` is true.

### play_on_all_surfaces
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
The track can play everywhere.

Cannot be defined if `track_type` is `"hero-track"` or `"script-track"`.

Cannot be true if `planets` or `surface_names` are defined.

### exclude_planets
- **Type:** array<[[SpaceLocationID (type)]]>
- **Optional**
The track cannot play on specified planets.

Can be used only if `play_on_all_surfaces` is true or `surface_names` are defined.

Cannot be used when `planets` are defined.

### exclude_surface_names
- **Type:** array<[[string (type)]]>
- **Optional**
The track cannot play on surfaces with specified name. It's enough if the specified name is a sub-string of the surface name.

Can be used only if `play_on_all_surfaces` is true or `surface_names` are defined.

Cannot exclude a name given in `surface_names`.

### sound
- **Type:** [[Sound]]
- **Optional**
Static music track.

One of `sound` or `variable_sound` must be defined. Both cannot be defined together.

### variable_sound
- **Type:** [[VariableAmbientSoundVariableSound]]
- **Optional**
Variable music track.

One of `sound` or `variable_sound` must be defined. Both cannot be defined together.

## Example

```
{
  type = "ambient-sound",
  name = "world-ambience-4",
  track_type = "interlude",
  sound =
  {
    filename = "__base__/sound/ambient/world-ambience-4.ogg",
    volume = 1.2
  }
}
```
