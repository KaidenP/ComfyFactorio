---
title: FluidBox
tags: [factorio-api, prototype, type]
---
# FluidBox

Used to set the fluid amount an entity can hold, as well as the connection points for pipes leading into and out of the entity.

Entities can have multiple fluidboxes. These can be part of a [[FluidEnergySource]], or be specified directly in the entity prototype.

## Properties

### volume
- **Type:** [[FluidAmount (type)]]
Must be greater than 0.

### pipe_connections
- **Type:** array<[[PipeConnectionDefinition (type)]]>
Connection points to connect to other fluidboxes. This is also marked as blue arrows in alt mode. Fluid may flow in or out depending on the `type` field of each connection.

Connection points may depend on the direction the entity is facing. These connection points cannot share positions with one another or the connection points of another fluid box belonging to the same entity.

Can't have more than 255 connections.

### filter
- **Type:** [[FluidID (type)]]
- **Optional**
Can be used to specify which fluid is allowed to enter this fluid box. See [here](https://forums.factorio.com/viewtopic.php?f=28&t=46302).

### render_layer
- **Type:** [[RenderLayer (type)]]
- **Optional**
- **Default:** `"object"`

### draw_only_when_connected
- **Type:** [[boolean (type)]]
- **Optional**
- **Default:** `false`

### volume_reservation_fraction
- **Type:** [[float (type)]]
- **Optional**
- **Default:** `0`
A fraction of the volume that will be "reserved" and cannot be removed by flow operations. This does nothing if the fluidbox is part of a fluid segment.

### pipe_covers
- **Type:** [[Sprite4Way]]
- **Optional**
The pictures to show when no fluid box is connected to this one.

### pipe_covers_frozen
- **Type:** [[Sprite4Way]]
- **Optional**

### pipe_picture
- **Type:** [[Sprite4Way]]
- **Optional**

### pipe_picture_frozen
- **Type:** [[Sprite4Way]]
- **Optional**

### mirrored_pipe_picture
- **Type:** [[Sprite4Way]]
- **Optional**
Pipe picture variation used when owner machine is flipped. If no picture is loaded, pipe_picture is used instead.

### mirrored_pipe_picture_frozen
- **Type:** [[Sprite4Way]]
- **Optional**
Frozen pipe picture variation used when owner machine is flipped. If no picture is loaded, pipe_picture_frozen is used instead.

### max_pipeline_extent
- **Type:** [[uint32 (type)]]
- **Optional**
- **Default:** Value of `UtilityConstants::default_pipeline_extent`
The max extent that a pipeline with this fluidbox can span. A given pipeline's extent is calculated as the min extent of all the fluidboxes that comprise it.

### production_type
- **Type:** [[ProductionType (type)]]
- **Optional**
- **Default:** `"none"`

### secondary_draw_order
- **Type:** [[int8 (type)]]
- **Optional**
- **Default:** `1`
Set the secondary draw order for all orientations. Used to determine render order for sprites with the same `render_layer` in the same position. Sprites with a higher `secondary_draw_order` are drawn on top.

### secondary_draw_orders
- **Type:** [[FluidBoxSecondaryDrawOrders]]
- **Optional**
Set the secondary draw order for each orientation. Used to determine render order for sprites with the same `render_layer` in the same position. Sprites with a higher `secondary_draw_order` are drawn on top.

The individual directions default to the value of `secondary_draw_order`.

### always_draw_covers
- **Type:** [[boolean (type)]]
- **Optional**
Defaults to true if `pipe_picture` is not defined, otherwise defaults to false.

### enable_working_visualisations
- **Type:** array<[[string (type)]]>
- **Optional**
Array of the [[WorkingVisualisation#name|WorkingVisualisation::name]] of working visualisations to enable when this fluidbox is present.

If `draw_only_when_connected` is `true`, then the working visualisation are only enabled when this is *connected*.

## Examples

```
fluid_box =
{
  volume = 200,
  pipe_covers = pipecoverspictures(),
  pipe_connections =
  {
    {flow_direction = "input-output", direction = defines.direction.west, position = {-1, 0.5}},
    {flow_direction = "input-output", direction = defines.direction.east, position = {1, 0.5}}
  },
  production_type = "input-output",
  filter = "water"
}
```
