---
title: SpaceConnectionDistanceTraveledAchievementPrototype
tags: [factorio-api, prototype]
---
# SpaceConnectionDistanceTraveledAchievementPrototype

> **Parent:** [[AchievementPrototype]] · **Type name:** `space-connection-distance-traveled-achievement`

## Properties

### tracked_connection
- **Type:** [[SpaceConnectionID (type)]]

### distance
- **Type:** [[uint32 (type)]]
How far a platform must travel to gain this achievement. Repeated trips over a shorter distance do not count.

### reversed
- **Type:** [[boolean (type)]]
The achievement is unidirectional, this property controls the direction (using space connection definition).

When false, a platform must go through [[SpaceConnectionPrototype#from|from]] location and travel in [[SpaceConnectionPrototype#to|to]] direction. When true, a platform must go through `to` location and travel in `from` direction.
