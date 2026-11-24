---
title: TurretAttackModifier
tags: [factorio-api, prototype, type]
---
# TurretAttackModifier

> **Parent:** [[BaseModifier]]

## Properties

### type
- **Type:** `"turret-attack"`

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

### turret_id
- **Type:** [[EntityID (type)]]
Name of the [[EntityPrototype]] that is affected. This also works for non-turrets such as tanks, however, the bonus does not appear in the entity's tooltips.

### modifier
- **Type:** [[double (type)]]
Modification value, which will be added to the current turret attack modifier upon researching.
