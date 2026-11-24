---
title: TrainStopFilter
tags: [factorio-api, runtime, concept]
---
# TrainStopFilter

## Fields

### surface
- **Type:** [[SurfaceIdentification]]
- **Optional**
Surface the train stop must be on in order to pass

### force
- **Type:** [[ForceID]]
- **Optional**
ForceID the train stop must have to pass

### is_full
- **Type:** [[boolean]]
- **Optional**
Checks if train stop is full (trains count >= trains limit or disabled) or not full.

### is_connected_to_rail
- **Type:** [[boolean]]
- **Optional**
Checks if train stop has a rail next to it.

### type
- **Type:** [[EntityID]] | array<[[EntityID]]>
- **Optional**
If given, only train stops of this type will pass

### station_name
- **Type:** [[string]] | array<[[string]]>
- **Optional**
Train stop must belong to given station name to pass

### limit_set_by_control_behavior
- **Type:** [[boolean]]
- **Optional**
If train stop has limit set by control behavior

### is_disabled
- **Type:** [[boolean]]
- **Optional**
If train stop is disabled by a control behavior
