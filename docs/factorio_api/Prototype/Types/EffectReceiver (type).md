---
title: EffectReceiver
tags: [factorio-api, prototype, type]
---
# EffectReceiver

*Note: `EffectReceiver (type)`.*

## Properties

### base_effect
- **Type:** [[Effect (type)]]
- **Optional**

### uses_module_effects
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### uses_beacon_effects
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### uses_surface_effects
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Controls whether [[LuaSurface#global_effect|LuaSurface::global_effect]] affects this receiver.

### uses_local_effects
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
Controls whether [[LuaEntity#local_effect|LuaEntity::local_effect]] affects this receiver.

### consumption_limits
- **Type:** [[EffectValueRange (type)]]
- **Optional**
- **Default:** `{ low = -0.8, high = 1000 }`
Limits total consumption effect value.

Low limit cannot be less than `-0.9999`. High limit cannot be greater than `1000`.

### speed_limits
- **Type:** [[EffectValueRange (type)]]
- **Optional**
- **Default:** `{ low = -0.8, high = 1000 }`
Limits total speed effect value.

Low limit cannot be less than `-0.9999`. High limit cannot be greater than `1000`.

### productivity_limits
- **Type:** [[EffectValueRange (type)]]
- **Optional**
- **Default:** `{ low = -0.8, high = 1000 }`
Limits total productivity effect value. This limit is applied before any productivity gained from research is added. Afterwards, productivity is clamped again to be non-negative. For crafting machines, it is also clamped to [[RecipePrototype#maximum_productivity|RecipePrototype::maximum_productivity]].

Low limit cannot be less than `-0.9999`. High limit cannot be greater than `1000`.

### pollution_limits
- **Type:** [[EffectValueRange (type)]]
- **Optional**
- **Default:** `{ low = -0.8, high = 1000 }`
Limits total pollution effect value.

Low limit cannot be less than `-0.9999`. High limit cannot be greater than `1000`.

### quality_limits
- **Type:** [[EffectValueRange (type)]]
- **Optional**
- **Default:** `{ low = 0, high = 1000 }`
Limits total quality effect value.

Low limit cannot be less than `-1000`. High limit cannot be greater than `1000`.
