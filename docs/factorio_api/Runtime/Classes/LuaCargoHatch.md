---
title: LuaCargoHatch
tags: [factorio-api, runtime, class]
---
# LuaCargoHatch

A cargo hatch.

## Attributes

### owner
- **Type:** [[LuaEntity]]

### busy
- **Type:** [[boolean]]

### reserved
- **Type:** [[boolean]]

### is_input_compatible
- **Type:** [[boolean]]

### is_output_compatible
- **Type:** [[boolean]]

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.

## Methods

### create_cargo_pod
Creates a cargo pod for output at the owning entity hatch location.

**Parameters:**
- **`cargo_pod_prototype`** — [[EntityID]] *(optional)*: The cargo pod prototype to create. If not provided, the default cargo pod prototype of the hatch is used.

**Returns:**
- [[LuaEntity]]
