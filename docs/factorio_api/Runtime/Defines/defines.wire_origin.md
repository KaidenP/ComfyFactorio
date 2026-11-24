---
title: wire_origin
tags: [factorio-api, define]
---
# wire_origin

*Note: `defines.wire_origin`.*

## Values

### player
These wires can be modified by players, scripts, and the game. They are visible to the player if the entity's `draw_circuit_wires` prototype property is set to `true` and both ends of it are on the same surface.

### script
These wires can be modified by scripts and the game. They are not visible to the player, irrespective of the `draw_circuit_wires` prototype property.

### radars
These wires can only be modified by the game. They are not visible to the player, irrespective of the `draw_circuit_wires` prototype property.
