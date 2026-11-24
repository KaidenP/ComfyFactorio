---
title: HeatConnectionDefinition
tags: [factorio-api, prototype, type]
---
# HeatConnectionDefinition

*Note: `HeatConnectionDefinition (type)`.*

Defines the connections for [[HeatEnergySource]] and [[HeatBuffer]].

## Properties

### position
- **Type:** [[MapPosition (type)]]
The location of the heat pipe connection, relative to the center of the entity in the north-facing direction.

### direction
- **Type:** [[defines.direction]]
The "outward" direction of this heat connection. For a connection to succeed, the other heat connection must face the opposite direction (a south-facing connection needs a north-facing connection to succeed). A connection rotates with the entity.
