---
title: NeighbourConnectableConnectionDefinition
tags: [factorio-api, prototype, type]
---
# NeighbourConnectableConnectionDefinition

*Note: `NeighbourConnectableConnectionDefinition (type)`.*

In order for 2 NeighbourConnectable to connect they need to share a connection point at the same position with opposite direction and both accept neighbor's category.

## Properties

### location
- **Type:** [[MapLocation (type)]]

### category
- **Type:** [[NeighbourConnectableConnectionCategory]]
Name of a category this connection should belong to. Used when deciding which connections are allowed to connect to this.

Cannot be an empty string.

### neighbour_category
- **Type:** array<[[NeighbourConnectableConnectionCategory]]>
- **Optional**
Table of neighbor categories this connection will connect to.
