---
title: UpgradeItemPrototype
tags: [factorio-api, prototype]
---
# UpgradeItemPrototype

> **Parent:** [[SelectionToolPrototype]] · **Type name:** `upgrade-item`

An [upgrade planner](https://wiki.factorio.com/Upgrade_planner).

For an entity to be allowed as an upgrade source, it must be minable, may not have "not-upgradable" flag set and may not be [[PrototypeBase#hidden|hidden]]. Additionally, the source entity's mining result must not be an item product that is [[ItemPrototype#hidden|hidden]]. Mining results with no item products are allowed.

For an entity to be allowed as an upgrade target, it must have least 1 item that builds it that isn't hidden.

For two entities to be upgrades of each other, the two entities must have the same [[EntityPrototype#fast_replaceable_group|fast replaceable group]], the same [[EntityPrototype#collision_box|collision box]] and the same [[EntityPrototype#collision_mask|collision mask]]. Additionally, [[UndergroundBeltPrototype|underground belts]] cannot be upgraded to [[TransportBeltPrototype|transport belts]] and vice versa.

For an entity to be automatically upgraded to another entity without configuring the upgrade planner, the [[EntityPrototype#next_upgrade|next upgrade]] of the upgrade source entity must be set.

## Properties

### stack_size
- **Type:** `1`
- **Overrides parent**
Count of items of the same name that can be stored in one inventory slot. Must be 1 when the `"not-stackable"` flag is set.
**Examples:**

```
stack_size = 1
```

### draw_label_for_cursor_render
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
- **Overrides parent**
If the item will draw its label when held in the cursor in place of the item count.

### select
- **Type:** [[SelectionModeData]]
- **Overrides parent**
The [[SelectionModeData#mode|SelectionModeData::mode]] is hardcoded to `"upgrade"`.

The filters are parsed, but then ignored and forced to be empty.

### alt_select
- **Type:** [[SelectionModeData]]
- **Overrides parent**
The [[SelectionModeData#mode|SelectionModeData::mode]] is hardcoded to `"cancel-upgrade"`.

The filters are parsed, but then ignored and forced to be empty.

### always_include_tiles
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
- **Overrides parent**
This property is hardcoded to `false`.
