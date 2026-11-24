---
title: NeighbourConnectable
tags: [factorio-api, prototype, type]
---
# NeighbourConnectable

*Note: `NeighbourConnectable (type)`.*

Defines how this entity connects to its neighbours

## Properties

### affected_by_direction
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `true`
If the connection positions and directions will be affected by entity's direction.

### neighbour_search_distance
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0.7`
Distance by which connection point is shifted along its direction to select a position where neighbor will be searched.

### connections
- **Type:** array<[[NeighbourConnectableConnectionDefinition (type)]]>
Definitions of the connection points.
