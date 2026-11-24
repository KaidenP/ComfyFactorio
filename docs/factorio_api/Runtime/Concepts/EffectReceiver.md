---
title: EffectReceiver
tags: [factorio-api, runtime, concept]
---
# EffectReceiver

## Fields

### base_effect
- **Type:** [[Effect]]

### uses_module_effects
- **Type:** [[boolean]]

### uses_beacon_effects
- **Type:** [[boolean]]

### uses_surface_effects
- **Type:** [[boolean]]
Controls whether [[LuaSurface#global_effect|LuaSurface::global_effect]] affects this receiver.

### uses_local_effects
- **Type:** [[boolean]]
Controls whether [[LuaEntity#local_effect|LuaEntity::local_effect]] affects this receiver.

### consumption_limits
- **Type:** [[EffectValueRange]]

### speed_limits
- **Type:** [[EffectValueRange]]

### productivity_limits
- **Type:** [[EffectValueRange]]

### pollution_limits
- **Type:** [[EffectValueRange]]

### quality_limits
- **Type:** [[EffectValueRange]]
