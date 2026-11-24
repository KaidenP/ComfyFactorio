---
title: SegmentedUnitPrototype
tags: [factorio-api, prototype]
---
# SegmentedUnitPrototype

> **Parent:** [[SegmentPrototype]] · **Type name:** `segmented-unit` · **Requires:** `space_age`

Entity composed of multiple segment entities that trail behind the head.

## Properties

### vision_distance
- **Type:** [[double (type)]]
Vision distance, affects scanning radius for enemies to attack. Must be non-negative. Max 100.

### attack_parameters
- **Type:** [[AttackParameters (type)]]
- **Optional**
Attack parameters for when a segmented unit is attacking something.

### revenge_attack_parameters
- **Type:** [[AttackParameters (type)]]
- **Optional**
Attack parameters for when a segmented unit is attacking something in retaliation because the target first attacked it.

### territory_radius
- **Type:** [[uint32 (type)]]
The territory radius in chunks. The chunk in which the entity spawned is included.

### enraged_duration
- **Type:** [[MapTick (type)]]
The number of ticks to remain enraged after last taking damage.

### patrolling_speed
- **Type:** [[double (type)]]
The movement speed while patrolling, in tiles per tick. Cannot be negative.

### investigating_speed
- **Type:** [[double (type)]]
The movement speed while investigating, in tiles per tick. Cannot be negative.

### attacking_speed
- **Type:** [[double (type)]]
The movement speed while attacking, in tiles per tick. Cannot be negative.

### enraged_speed
- **Type:** [[double (type)]]
The movement speed while enraged, in tiles per tick. Cannot be negative.

### acceleration_rate
- **Type:** [[double (type)]]
The acceleration rate when moving from one state to another. Cannot be negative.

### turn_radius
- **Type:** [[double (type)]]
Turn radius, in tiles. Cannot be negative.

### patrolling_turn_radius
- **Type:** [[double (type)]]
- **Optional**
- **Default:** Value of `turn_radius`
Cannot be negative.

### turn_smoothing
- **Type:** [[double (type)]]
- **Optional**
- **Default:** `1`
Attempts to smooth out tight turns by limiting how quickly the unit can change turning directions. 0 means no turn smoothing, 1 means no turning whatsoever. Must be between 0 and 1.

### ticks_per_scan
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `120`
The number of ticks between territory scans. Greater values means longer time between scans, which means a slower reaction time. Cannot be `0`.

### segment_engine
- **Type:** [[SegmentEngineSpecification (type)]]
Specification of the segment engine, which should contain a list of the segments that compose the entity's body.

### roar
- **Type:** [[Sound]]
- **Optional**

### roar_probability
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.00277777785`
The default is 1.0f / (6.0f * 60.0f), average pause between roars is 6 seconds.

### hurt_roar
- **Type:** [[Sound]]
- **Optional**
Sound which plays when health ratio drops below any of `hurt_thresholds`.

### hurt_thresholds
- **Type:** array<[[float (type)]]>
- **Optional**
Only loaded, and mandatory if `hurt_roar` is defined.
