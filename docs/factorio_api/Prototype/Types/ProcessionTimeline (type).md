---
title: ProcessionTimeline
tags: [factorio-api, prototype, type]
---
# ProcessionTimeline

*Note: `ProcessionTimeline (type)`.*

A wrapper for a collection of [[ProcessionLayer|ProcessionLayers]].

## Properties

### duration
- **Type:** [[MapTick (type)]]
The time to play this cutscene regardless of individual layer durations.

### special_action_tick
- **Type:** [[MapTick (type)]]
- **Optional**
- **Default:** 1/2 of duration
Time to initiate usage specific actions:

- Ascending animation will detach from rocket on this tick.

- Descending animation will request hatch to be opened.

### draw_switch_tick
- **Type:** [[MapTick (type)]]
- **Optional**
- **Default:** 1/2 of duration
During procession, the pod will at some point start being drawn above the rest of the game:

- When ascending this tick will go from world to above.

- When descending this tick will go from above to world.

Notably, LUT override won't be applied until the pod is drawn above the game.

### intermezzo_min_duration
- **Type:** [[MapTick (type)]]
- **Optional**
- **Default:** `0`
The real duration of the intermezzo playing will be above this value.

### intermezzo_max_duration
- **Type:** [[MapTick (type)]]
- **Optional**
- **Default:** `0`
The real duration of the intermezzo playing will be below this value.

### layers
- **Type:** array<[[ProcessionLayer]]>

### audio_events
- **Type:** array<[[ProcessionAudioEvent]]>
- **Optional**
