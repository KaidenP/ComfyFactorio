---
title: PipeConnectionDefinition
tags: [factorio-api, prototype, type]
---
# PipeConnectionDefinition

*Note: `PipeConnectionDefinition (type)`.*

## Properties

### flow_direction
- **Type:** [[FluidFlowDirection (type)]]
- **Optional**
- **Default:** `"input-output"`
Allowed direction of fluid flow at this connection. Pipeline entities (`pipe`, `pipe-to-ground`, and `storage-tank`) do not support this property.

### connection_type
- **Type:** [[PipeConnectionType (type)]]
- **Optional**
- **Default:** `"normal"`
Selects set of rules to follow when looking for other FluidBox this connection should connect to.

### enable_working_visualisations
- **Type:** array<[[string (type)]]>
- **Optional**
Array of the [[WorkingVisualisation#name|WorkingVisualisation::name]] of working visualisations to enable when this pipe connection is present.

If the owning fluidbox has [[FluidBox#draw_only_when_connected|draw_only_when_connected]] set to `true`, then the working visualisation is only enabled if this pipe connection is *connected*.

### hide_connection_info
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`
If true, connection arrows and fluid icons will not be drawn for this connection when the entity is selected or in alt-mode.

### direction
- **Type:** [[defines.direction]]
- **Optional**
Primary direction this connection points to when entity direction is north and the entity is not mirrored. When entity is rotated or mirrored, effective direction will be computed based on this value.

Only loaded, and mandatory if `connection_type` is `"normal"` or `"underground"`.

### position
- **Type:** [[MapPosition (type)]]
- **Optional**
Position relative to entity's center where pipes can connect to this fluidbox regardless the directions of entity.

Only loaded if `connection_type` is `"normal"` or `"underground"`.

### positions
- **Type:** ([[MapPosition (type)]], [[MapPosition (type)]], [[MapPosition (type)]], [[MapPosition (type)]])
- **Optional**
The 4 separate positions corresponding to the 4 main directions of entity. Positions must correspond to directions going one after another.

This is used for example by "pumpjack" where connections are consistently near bottom-left corner (2 directions) or near top-right corner (2 directions).

Only loaded, and mandatory if `position` is not defined and if `connection_type` is `"normal"` or `"underground"`.

### alt_position
- **Type:** [[MapPosition (type)]]
- **Optional**
- **Default:** Value of `position` or first value of `positions`
Relative position of the pipe connection when entity direction is north-east.

Only loaded if `connection_type` is `"normal"` or `"underground"`.

### alt_direction
- **Type:** [[defines.direction]]
- **Optional**
- **Default:** Value of `direction`
Direction this connection should be facing when entity direction is north-east. When entity is rotated, effective direction will be computed based on this value.

Only loaded if `connection_type` is `"normal"` or `"underground"`.

### connection_category
- **Type:** [[string (type)]] | array<[[string (type)]]>
- **Optional**
- **Default:** `"default"`
Fluidboxes' pipe connections are only allowed to connect with each other if they share a connection category. For example a mod could have a "steam pipes" and "cryogenic pipes" category that should not connect with each other.

In case of a normal connection, a pipe connection can be in multiple connection categories. This allows to create a mod where pipes of different categories would not connect to each other while still making it possible for crafting machines and other entities to connect to any of the specified pipes.

By default, all pipe connections have the `"default"` category. So a pipe that should connect to a new category and standard pipes can have the `connection_category = {"my-new-pipe", "default"}`.

May have at most one category when `connection_type` is `"underground"`.

Only loaded if `connection_type` is `"normal"` or `"underground"`.

### max_underground_distance
- **Type:** [[uint8 (type)]]
- **Optional**
- **Default:** `0`
Only loaded if `connection_type` is `"underground"`.

### max_distance_tint
- **Type:** [[Color (type)]]
- **Optional**
Only loaded if `connection_type` is `"underground"`.

### underground_collision_mask
- **Type:** [[CollisionMaskConnector]]
- **Optional**
An underground connection may be defined as colliding with tiles in which case if any colliding tile is placed between underground ends the connection will not be established.

In order to connect, both ends must have the same collision mask specified.

Only loaded if `connection_type` is `"underground"`.

### linked_connection_id
- **Type:** [[FluidBoxLinkedConnectionID]]
- **Optional**
Expected to be unique inside of a single entity. Used to uniquely identify where a linked connection should connect to.

Only loaded, and mandatory if `connection_type` is `"linked"`.
