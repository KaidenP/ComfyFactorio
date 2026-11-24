---
title: ElectricEnergyInterfacePrototype
tags: [factorio-api, prototype]
---
# ElectricEnergyInterfacePrototype

> **Parent:** [[EntityWithOwnerPrototype]] · **Type name:** `electric-energy-interface`

Entity with electric energy source with that can have some of its values changed runtime. Useful for modding in energy consumers/producers.

## Properties

### energy_source
- **Type:** [[ElectricEnergySource]]

### energy_production
- **Type:** [[Energy]]
- **Optional**
- **Default:** `0`
**Examples:**

```
energy_production = "500GW"
```

### energy_usage
- **Type:** [[Energy]]
- **Optional**
- **Default:** `0`
**Examples:**

```
energy_usage = "10kW"
```

### gui_mode
- **Type:** `"all"` | `"none"` | `"admins"`
- **Optional**
- **Default:** `"none"`

### continuous_animation
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
Whether the electric energy interface animation always runs instead of being scaled to activity.

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### light
- **Type:** [[LightDefinition]]
- **Optional**
The light that this electric energy interface emits.

### picture
- **Type:** [[Sprite]]
- **Optional**

### pictures
- **Type:** [[Sprite4Way]]
- **Optional**
Only loaded if `picture` is not defined.

### animation
- **Type:** [[Animation]]
- **Optional**
Only loaded if both `picture` and `pictures` are not defined.

### animations
- **Type:** [[Animation4Way]]
- **Optional**
Only loaded if `picture`, `pictures`, and `animation` are not defined.

### allow_copy_paste
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**
