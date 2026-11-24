---
title: EntityPrototypeFlags
tags: [factorio-api, prototype, type]
---
# EntityPrototypeFlags

*Note: `EntityPrototypeFlags (type)`.*

An array containing the following values.

If an entity is a [[LuaEntityPrototype#is_building|building]] and has the `"player-creation"` flag set, it is considered for multiple enemy/unit behaviors:

- Autonomous enemy attacks (usually triggered by pollution) can only attack within chunks that contain at least one entity that is both a building and a player-creation.

- Enemy expansion considers entities that are both buildings and player-creations as "enemy" entities that may block expansion.

## Type

array<`"not-rotatable"` | `"placeable-neutral"` | `"placeable-player"` | `"placeable-enemy"` | `"placeable-off-grid"` | `"player-creation"` | `"building-direction-8-way"` | `"filter-directions"` | `"get-by-unit-number"` | `"breaths-air"` | `"not-repairable"` | `"not-on-map"` | `"not-deconstructable"` | `"not-blueprintable"` | `"always-show"` | `"hide-alt-info"` | `"not-flammable"` | `"no-automated-item-removal"` | `"no-automated-item-insertion"` | `"no-copy-paste"` | `"not-selectable-in-game"` | `"not-upgradable"` | `"not-in-kill-statistics"` | `"building-direction-16-way"` | `"no-logistic-connection"` | `"snap-to-rail-support-spot"` | `"not-in-made-in"` | `"not-in-bonus-gui"` | `"not-in-mined-by"`>

## Examples

```
flags = {"placeable-neutral", "player-creation"}
```
