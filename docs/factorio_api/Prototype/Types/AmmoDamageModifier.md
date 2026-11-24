---
title: AmmoDamageModifier
tags: [factorio-api, prototype, type]
---
# AmmoDamageModifier

> **Parent:** [[BaseModifier]]

## Properties

### type
- **Type:** `"ammo-damage"`

### infer_icon
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If set to `false`, use the icon from [[UtilitySprites]] for this technology effect icon.

### use_icon_overlay_constant
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If `false`, do not draw the small "constant" icon over the technology effect icon.

### ammo_category
- **Type:** [[AmmoCategoryID (type)]]
Name of the [[AmmoCategory]] that is affected.

### modifier
- **Type:** [[double (type)]]
Modification value, which will be added to the current ammo damage modifier upon researching.
