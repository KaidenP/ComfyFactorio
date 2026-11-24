---
title: Stripe
tags: [factorio-api, prototype, type]
---
# Stripe

Used as an alternative way to specify animations.

## Properties

### width_in_frames
- **Type:** [[uint32 (type)]]

### height_in_frames
- **Type:** [[uint32 (type)]]
Mandatory when Stripe is used in [[Animation]].

Optional when it is used in [[RotatedAnimation]], where it defaults to [[RotatedAnimation#direction_count|RotatedAnimation::direction_count]].

### filename
- **Type:** [[FileName]]

### x
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`

### y
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** `0`
