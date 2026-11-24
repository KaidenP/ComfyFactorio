---
title: CliffPlacementSettings
tags: [factorio-api, prototype, type]
---
# CliffPlacementSettings

*Note: `CliffPlacementSettings (type)`.*

## Properties

### name
- **Type:** [[EntityID (type)]]
- **Optional**
Name of the [[CliffPrototype]].

### control
- **Type:** [[AutoplaceControlID]]
- **Optional**
Name of the [[AutoplaceControl (prototype)|AutoplaceControl]].

### cliff_elevation_0
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `10`
Elevation at which the first row of cliffs is placed. Can not be set from the map generation GUI.

### cliff_elevation_interval
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `40`
Elevation difference between successive rows of cliffs. This is inversely proportional to 'frequency' in the map generation GUI. Specifically, when set from the GUI the value is `40 / frequency`.

### cliff_smoothing
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `1`
Smoothing makes cliffs straighter on rough elevation but makes placement inaccurate. 0 is no smoothing, 1 is full smoothing. Values outside of 0-1 are possible for specific effects but not recommended.

### richness
- **Type:** [[float (type)]]
- **Optional**
Corresponds to 'continuity' in the GUI. This value is not used directly, but is used by the 'cliffiness' noise expression, which in combination with elevation and the two cliff elevation properties drives cliff placement (cliffs are placed when elevation crosses the elevation contours defined by `cliff_elevation_0` and `cliff_elevation_interval` when 'cliffiness' is greater than `0.5`). The default 'cliffiness' expression interprets this value such that larger values result in longer unbroken walls of cliffs, and smaller values (between `0` and `1`) result in larger gaps in cliff walls.
