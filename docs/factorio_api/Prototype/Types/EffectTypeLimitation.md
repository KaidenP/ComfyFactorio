---
title: EffectTypeLimitation
tags: [factorio-api, prototype, type]
---
# EffectTypeLimitation

A list of [[ModulePrototype|module]] effects, or just a single effect. Modules with other effects cannot be used on the machine. This means that both effects from modules and from surrounding beacons are restricted to the listed effects. If `allowed_effects` is an empty array, the machine cannot be affected by modules or beacons.

## Type

`"speed"` | `"productivity"` | `"consumption"` | `"pollution"` | `"quality"` | array<`"speed"` | `"productivity"` | `"consumption"` | `"pollution"` | `"quality"`>

## Examples

```
-- Allow all module types
allowed_effects = {"speed", "productivity", "consumption", "pollution", "quality"}
```

```
-- Allow only modules that affect speed
allowed_effects = "speed"
```
