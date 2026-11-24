---
title: ChainActiveTriggerPrototype
tags: [factorio-api, prototype]
---
# ChainActiveTriggerPrototype

> **Parent:** [[ActiveTriggerPrototype]] · **Type name:** `chain-active-trigger`

Jumps between targets and applies a [[Trigger]] to them.

## Properties

### action
- **Type:** [[Trigger]]
- **Optional**
The trigger to apply when jumping to a new target.

### max_jumps
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `5`
Max number of jumps per trigger.

### max_range_per_jump
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `5`
Max length of jumps.

### max_range
- **Type:** [[double (type)]]
- **Optional**
- **Default:** infinity
Max distance jumps are allowed to travel away from the original target.

### jump_delay_ticks
- **Type:** [[MapTick (type)]]
- **Optional**
- **Default:** `0`
Tick delay between each jump. `0` means that all jumps are instantaneous.

### fork_chance
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0`
Chance that a new fork will spawn after each jump. `0` for 0% chance and `1` for 100% chance.

Must be between 0 and 1.

### fork_chance_increase_per_quality_level
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `0.1`

### max_forks_per_jump
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `1`
Maximum number of forks that can spawn from a single jump.

### max_forks
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** max uint32
Maximum number of forks allowed to spawn for the entire chain.
