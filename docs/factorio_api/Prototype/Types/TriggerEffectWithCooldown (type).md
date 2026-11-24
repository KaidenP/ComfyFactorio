---
title: TriggerEffectWithCooldown
tags: [factorio-api, prototype, type]
---
# TriggerEffectWithCooldown

*Note: `TriggerEffectWithCooldown (type)`.*

A [[TriggerEffect]] with cooldown conditions, used to limit the frequency of trigger effects that would otherwise fire every single tick. If multiple cooldown conditions are defined, then all cooldowns must be satisfied before the effect can be triggered.

## Properties

### distance_cooldown
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The travel distance between triggers that the triggerer must travel between effects. Negative values will mean there is no cooldown.

### initial_distance_cooldown
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
The initial state of the distance cooldown. In other words, the distance the triggerer must travel before the first effect can be triggered. Useful for staggering multiple effects.

### time_cooldown
- **Type:** [[MapTick (type)]]
- **Optional**
- **Default:** `0`
The number of ticks that elapse between triggers.

### initial_time_cooldown
- **Type:** [[MapTick (type)]]
- **Optional**
- **Default:** `0`
The initial amount of time to wait before triggering the effect for the first time.

### effect
- **Type:** [[TriggerEffect]]
