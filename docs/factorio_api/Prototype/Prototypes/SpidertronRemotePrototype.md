---
title: SpidertronRemotePrototype
tags: [factorio-api, prototype]
---
# SpidertronRemotePrototype

> **Parent:** [[SelectionToolPrototype]] · **Type name:** `spidertron-remote`

The [spidertron remote](https://wiki.factorio.com/Spidertron_remote). This remote can only be used for entities of type [[SpiderVehiclePrototype]].

## Properties

### icon_color_indicator_mask
- **Type:** [[FileName]]
- **Optional**
Color mask for the icon. This is used to show the color of the spidertron remote LEDS in the GUI.

### stack_size
- **Type:** `1`
- **Overrides parent**
Count of items of the same name that can be stored in one inventory slot. Must be 1 when the `"not-stackable"` flag is set.
**Examples:**

```
stack_size = 1
```
