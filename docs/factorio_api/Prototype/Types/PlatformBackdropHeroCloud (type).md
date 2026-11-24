---
title: PlatformBackdropHeroCloud
tags: [factorio-api, prototype, type]
---
# PlatformBackdropHeroCloud

*Note: `PlatformBackdropHeroCloud (type)`.*

## Properties

### sprite_index
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
1, 2, 3 use cloud sprites 1, 2, 3 respectively. 0 will disable this cloud. Anything else is invalid.

### size
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0.5, 0.5}`
Cloud size as a proportion of the total planet size, meaning `1` spans whole planet.

### rotation_speed
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`

### rotate_with_planet
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`

### starting_frame_offset
- **Type:** [[uint16 (type)]]
- **Optional**
- **Default:** `0`
Random frame offset of the cloud animation if the graphic is an animation.

### position_deviation
- **Type:** [[Vector (type)]]
- **Optional**
- **Default:** `{0, 0}`
Random position offset of the cloud animation. Refreshed every loop.

### rotation_deviation
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.0`

### projection_style
- **Type:** `"none"` | `"front-only"` | `"front-and-back"` | `"front-and-back-inverted"`
- **Optional**
- **Default:** `"front-only"`

### positions
- **Type:** array<[[Vector (type)]]>
- **Optional**
With each planet revolution, the cloud smoothly travels along this path by approximating the provided points. If only single position is provided, it remains stationary at that point.
