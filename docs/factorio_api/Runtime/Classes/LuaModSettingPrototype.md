---
title: LuaModSettingPrototype
tags: [factorio-api, runtime, class]
---
# LuaModSettingPrototype

> **Extends:** [[LuaPrototypeBase]]

Prototype of a mod setting.

## Attributes

### mod
- **Type:** [[string]]
The mod that owns this setting.

### setting_type
- **Type:** `"startup"` | `"runtime-global"` | `"runtime-per-user"`

### default_value
- **Type:** [[boolean]] | [[double]] | [[int32]] | [[string]] | [[Color]]
The default value of this setting.

### minimum_value
- **Type:** [[double]] | [[int32]]
- **Optional**
The minimum value for this setting. `nil` if this setting type doesn't support a minimum.

### maximum_value
- **Type:** [[double]] | [[int32]]
- **Optional**
The maximum value for this setting. `nil` if this setting type doesn't support a maximum.

### allowed_values
- **Type:** array<[[string]]> | array<[[int32]]> | array<[[double]]>
- **Optional**
The allowed values for this setting. `nil` if this setting doesn't use the a fixed set of values.

### allow_blank
- **Type:** [[boolean]]
- **Optional**
Whether this string setting allows blank values. `nil` if not a string setting.

### auto_trim
- **Type:** [[boolean]]
- **Optional**
Whether this string setting auto-trims values. `nil` if not a string setting

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
