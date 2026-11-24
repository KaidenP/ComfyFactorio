---
title: CargoBayConnections
tags: [factorio-api, prototype, type]
---
# CargoBayConnections

## Properties

### tileset
- **Type:** array<array<[[LayeredSpriteVariations]]>>
- **Optional**
An array of LayeredSpriteVariations groups. One tile can have a maximum of two groups. A group is selected based on tile position and a random variation is picked from that group. This allows having interleaved variations and makes sure the same variation isn't picked for surrounding tiles.

Supports at most 255 items.

### tileset_mapping
- **Type:** dictionary<[[uint8 (type)]] → [[uint8 (type)]] | array<[[uint8 (type)]]>>
- **Optional**
A mapping from a bitmask index to a tileset index. A bitmask index mapped to 0 won't be drawn.

Tile bitmask uses 8 bits. Bits are assigned from the top-left corner and going clockwise (top-left tile has bit 0 and right tile has bit 7).

Mandatory if `tileset` is defined.

### bridge_horizontal_narrow
- **Type:** [[LayeredSpriteVariations]]
- **Optional**

### bridge_horizontal_wide
- **Type:** [[LayeredSpriteVariations]]
- **Optional**

### bridge_vertical_narrow
- **Type:** [[LayeredSpriteVariations]]
- **Optional**

### bridge_vertical_wide
- **Type:** [[LayeredSpriteVariations]]
- **Optional**

### bridge_crossing
- **Type:** [[LayeredSpriteVariations]]
- **Optional**
