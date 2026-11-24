---
title: AmmoItemPrototype
tags: [factorio-api, prototype]
---
# AmmoItemPrototype

> **Parent:** [[ItemPrototype]] · **Type name:** `ammo`

Ammo used for a gun.

## Properties

### ammo_type
- **Type:** [[AmmoType (type)]] | array<[[AmmoType (type)]]>
When using a plain [[AmmoType (type)|AmmoType]] (no array), the ammo type applies to everything (`"default"`).

When using an array of AmmoTypes, they have the additional [[AmmoType (type)#source_type|AmmoType::source_type]] property.

### magazine_size
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Number of shots before ammo item is consumed. Must be >= `1`.

### reload_time
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
Amount of extra time (in ticks) it takes to reload the weapon after depleting the magazine. Must be >= `0`.

### ammo_category
- **Type:** [[AmmoCategoryID (type)]]

### shoot_protected
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
