---
title: TrainPathFinderOneGoalResult
tags: [factorio-api, runtime, concept]
---
# TrainPathFinderOneGoalResult

## Fields

### found_path
- **Type:** [[boolean]]
True if found path.

### goal_index
- **Type:** [[uint32]]
- **Optional**
If path was found, provides index of the specific goal to which the path goes to.

### start_index
- **Type:** [[uint32]]
- **Optional**
If path was found, provides index of the specific start from which the path to target goes from

### penalty
- **Type:** [[double]]
- **Optional**
Penalty of the path to goal if path was found.

### is_front
- **Type:** [[boolean]]
- **Optional**
If path was found, tells if the path was reached from the train's front end or from [[RailEndStart]] with [[RailEndStart#is_front|RailEndStart::is_front]] set.

### total_length
- **Type:** [[double]]
- **Optional**
If path was found and search was of type `"path"`, provides total length of all rails of the path.

### path
- **Type:** array<[[LuaEntity]]>
- **Optional**
Only if search was of type `"path"`, `return_path` was set to true and path was found. Contains all rails in order that are part of the found path.

### steps_count
- **Type:** [[uint32]]
Amount of steps pathfinder performed. This is a measure of how expensive this search was.
