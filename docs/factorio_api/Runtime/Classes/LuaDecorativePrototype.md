---
title: LuaDecorativePrototype
tags: [factorio-api, runtime, class]
---
# LuaDecorativePrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of an optimized decorative.

## Attributes

### collision_box
- **Type:** [[BoundingBox]]
The bounding box used for collision checking.

### collision_mask
- **Type:** [[CollisionMask]]
The collision masks this decorative uses

### autoplace_specification
- **Type:** [[AutoplaceSpecification]]
- **Optional**
Autoplace specification for this decorative prototype, if any.

### render_layer
- **Type:** [[RenderLayer]]

### decal
- **Type:** [[boolean]]

### grows_through_rail_path
- **Type:** [[boolean]]

### trigger_effect
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### placed_effect
- **Type:** array<[[TriggerEffectItem]]>
- **Optional**

### minimal_separation
- **Type:** [[double]]

### target_count
- **Type:** [[uint32]]

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
