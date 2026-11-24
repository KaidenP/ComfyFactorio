---
title: WaitCondition
tags: [factorio-api, runtime, concept]
---
# WaitCondition

## Fields

### type
- **Type:** [[WaitConditionType]]

### compare_type
- **Type:** `"and"` | `"or"`
- **Optional**
Specifies how this condition is to be compared with the preceding conditions in the corresponding `wait_conditions` array. Always present when reading, defaults to `"and"` when writing.

### ticks
- **Type:** [[uint32]]
- **Optional**
Number of ticks to wait when `type` is `"time"`, or number of ticks of inactivity when `type` is `"inactivity"`.

### condition
- **Type:** [[CircuitCondition]] | [[BlueprintItemIDAndQualityIDPair]]
- **Optional**
This is a CircuitCondition and only present when `type` is `"item_count"`, `"circuit"`, `"fluid_count"`, `"fuel_item_count_all"`, or `"fuel_item_count_any"`, and a circuit condition is configured. This is a BlueprintItemIDAndQualityIDPair and only present when `type` is `"request_satisfied"` or `"request_not_satisfied"`

### planet
- **Type:** [[string]]
- **Optional**
Name of the space location. Only present when `type` is "`any_planet_import_zero`" and a planet is configured.

### station
- **Type:** [[string]]
- **Optional**
Name of the station. Only present when `type` is "`specific_destination_full`", "`specific_destination_not_full`", "`at_station`", or "`not_at_station`", and a station is configured.

### damage
- **Type:** [[uint32]]
- **Optional**
Amount of damage to take when `type` is `"damage_taken"`.
