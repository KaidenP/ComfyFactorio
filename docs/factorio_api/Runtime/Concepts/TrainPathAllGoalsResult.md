---
title: TrainPathAllGoalsResult
tags: [factorio-api, runtime, concept]
---
# TrainPathAllGoalsResult

## Fields

### amount_accessible
- **Type:** [[uint32]]
Amount of goals that are accessible.

### accessible
- **Type:** array<[[boolean]]>
Array of the same length as requested goals: each field will tell if related goal is accessible for the train.

### penalties
- **Type:** array<[[double]]>
- **Optional**
Array of the same length as requested goals. Only present if request type was `"all-goals-penalties"`.

### steps_count
- **Type:** [[uint32]]
Amount of steps pathfinder performed. This is a measure of how expensive this search was.
