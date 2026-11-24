---
title: Alert
tags: [factorio-api, runtime, concept]
---
# Alert

## Fields

### tick
- **Type:** [[MapTick]]
The tick this alert was created.

### target
- **Type:** [[LuaEntity]]
- **Optional**

### prototype
- **Type:** [[LuaEntityPrototype]]
- **Optional**

### position
- **Type:** [[MapPosition]]
- **Optional**

### icon
- **Type:** [[SignalID]]
- **Optional**
The SignalID used for a custom alert. Only present for custom alerts.

### message
- **Type:** [[LocalisedString]]
- **Optional**
The message for a custom alert. Only present for custom alerts.
