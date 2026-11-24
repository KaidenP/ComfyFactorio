---
title: LuaFluidBoxPrototype
tags: [factorio-api, runtime, class]
---
# LuaFluidBoxPrototype

A prototype of a fluidbox owned by some [[LuaEntityPrototype]].

## Attributes

### entity
- **Type:** [[LuaEntityPrototype]]
The entity that this belongs to.

### index
- **Type:** [[uint32]]
The index of this fluidbox prototype in the owning entity.

### pipe_connections
- **Type:** array<[[PipeConnectionDefinition]]>
The pipe connection points.

### production_type
- **Type:** [[ProductionType]]
The production type.

### filter
- **Type:** [[LuaFluidPrototype]]
- **Optional**
The filter, if any is set.

### secondary_draw_orders
- **Type:** array<[[int32]]>
The secondary draw orders for the 4 possible connection directions.

### render_layer
- **Type:** [[RenderLayer]]
The render layer.

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### get_volume
Gets the volume of this fluidbox with the given quality.

**Parameters:**
- **`quality`** — [[QualityID]] *(optional)*

**Returns:**
- [[double]]
