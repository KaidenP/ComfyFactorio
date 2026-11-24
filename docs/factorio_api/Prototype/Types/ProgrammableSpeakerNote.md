---
title: ProgrammableSpeakerNote
tags: [factorio-api, prototype, type]
---
# ProgrammableSpeakerNote

## Properties

### name
- **Type:** [[string (type)]]

### sound
- **Type:** [[Sound]]
- **Optional**
Cannot contain aggregation.

One of `sound` or `cyclic_sound` must be defined. Both cannot be defined together.

### cyclic_sound
- **Type:** [[CyclicSound]]
- **Optional**
Cannot contain aggregations.

One of `sound` or `cyclic_sound` must be defined. Both cannot be defined together.
