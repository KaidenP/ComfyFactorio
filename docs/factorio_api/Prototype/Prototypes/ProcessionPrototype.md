---
title: ProcessionPrototype
tags: [factorio-api, prototype]
---
# ProcessionPrototype

> **Parent:** [[Prototype]] · **Type name:** `procession`

Describes the duration and visuals of a departure, arrival or an intermezzo while traveling between surfaces. Usually provided inside of a [[ProcessionSet (type)|ProcessionSet]].

## Properties

### timeline
- **Type:** [[ProcessionTimeline (type)]]
Used when leaving or arriving to a station.

### ground_timeline
- **Type:** [[ProcessionTimeline (type)]]
- **Optional**
Used alternatively when landing to ground.

### usage
- **Type:** `"departure"` | `"arrival"` | `"intermezzo"`
Arrival and Departure are to be referenced by name. All intermezzos are collected during loading and filled in by `procession_style`.

### procession_style
- **Type:** [[uint32 (type)]] | array<[[uint32 (type)]]>
Indexes used to match transitions from different surfaces together. Only a single intermezzo of a given procession_style may exist.
**Examples:**

```
Going from Surface A -> Surface B
Surface A has departures: [1, 3, 4]
Surface B has arrivals:   [2, 3, 5]
This trip will select:
Departure 3 -> (Intermezzo 3) -> Arrival 3
```
