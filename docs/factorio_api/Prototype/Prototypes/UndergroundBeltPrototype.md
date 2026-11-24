---
title: UndergroundBeltPrototype
tags: [factorio-api, prototype]
---
# UndergroundBeltPrototype

> **Parent:** [[TransportBeltConnectablePrototype]] · **Type name:** `underground-belt`

An [underground belt](https://wiki.factorio.com/Underground_belt).

## Properties

### max_distance
- **Type:** [[uint8 (type)]]

### structure
- **Type:** [[UndergroundBeltStructure]]
- **Optional**

### underground_sprite
- **Type:** [[Sprite]]
- **Optional**

### underground_remove_belts_sprite
- **Type:** [[Sprite]]
- **Optional**

### max_distance_underground_remove_belts_sprite
- **Type:** [[Sprite]]
- **Optional**

### underground_collision_mask
- **Type:** [[CollisionMaskConnector]]
- **Optional**
- **Default:** no masks
The underground connection may be defined as colliding with tiles in which case if any colliding tile is placed between underground ends the connection will not be established.

### max_distance_tint
- **Type:** [[Color (type)]]
- **Optional**
