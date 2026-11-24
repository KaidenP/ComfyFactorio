---
title: TrainFilter
tags: [factorio-api, runtime, concept]
---
# TrainFilter

## Fields

### train_id
- **Type:** [[uint32]]
- **Optional**
Train ID filter

### surface
- **Type:** [[SurfaceIdentification]]
- **Optional**
Surface the train must be on in order to pass

### force
- **Type:** [[ForceID]]
- **Optional**
Train must contain at least one rolling stock of this force to pass

### stock
- **Type:** [[EntityID]] | array<[[EntityID]]>
- **Optional**
Train must contain a rolling stock of any of provided prototype to pass

### min_stocks
- **Type:** [[uint32]]
- **Optional**
Train must have at least that many stocks to pass

### max_stocks
- **Type:** [[uint32]]
- **Optional**
Train must have at most that many stocks to pass

### is_moving
- **Type:** [[boolean]]
- **Optional**
Checks if train is moving (has speed != 0) or not moving.

### has_passenger
- **Type:** [[boolean]]
- **Optional**
Checks if train has a passenger.

### is_manual
- **Type:** [[boolean]]
- **Optional**
Checks if train is in manual controller.

### group
- **Type:** [[string]]
- **Optional**
Train must belong to a group of a given name.
