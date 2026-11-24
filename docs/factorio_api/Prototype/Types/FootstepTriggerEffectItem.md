---
title: FootstepTriggerEffectItem
tags: [factorio-api, prototype, type]
---
# FootstepTriggerEffectItem

> **Parent:** [[CreateParticleTriggerEffectItem]]

## Properties

### tiles
- **Type:** array<[[TileID (type)]]>

### actions
- **Type:** array<[[CreateParticleTriggerEffectItem]]>
- **Optional**
Can be used to specify multiple CreateParticleTriggerEffectItems. If this property is defined, all properties inherited from CreateParticleTriggerEffectItem are ignored.

### use_as_default
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
When `true`, the trigger(s) defined in `actions` are the default triggers for tiles that don't have an associated footstep particle trigger. (ie. don't show up in one of the "tiles" lists).
