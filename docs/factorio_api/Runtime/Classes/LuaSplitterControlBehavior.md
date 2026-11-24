---
title: LuaSplitterControlBehavior
tags: [factorio-api, runtime, class]
---
# LuaSplitterControlBehavior

> **Extends:** [[LuaControlBehavior]]

Control behavior for splitter.

## Attributes

### set_input_side
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### input_left_condition
- **Type:** [[CircuitConditionDefinition]]
- **Writable:** [[CircuitConditionDefinition]]

### input_right_condition
- **Type:** [[CircuitConditionDefinition]]
- **Writable:** [[CircuitConditionDefinition]]

### set_output_side
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### output_left_condition
- **Type:** [[CircuitConditionDefinition]]
- **Writable:** [[CircuitConditionDefinition]]

### output_right_condition
- **Type:** [[CircuitConditionDefinition]]
- **Writable:** [[CircuitConditionDefinition]]

### set_filter
- **Type:** [[boolean]]
- **Writable:** [[boolean]]

### valid
- **Type:** [[boolean]]
Is this object valid? This Lua object holds a reference to an object within the game engine. It is possible that the game-engine object is removed whilst a mod still holds the corresponding Lua object. If that happens, the object becomes invalid, i.e. this attribute will be `false`. Mods are advised to check for object validity if any change to the game state might have occurred between the creation of the Lua object and its access.

### object_name
- **Type:** [[string]]
The class name of this object. Available even when `valid` is false. For LuaStruct objects it may also be suffixed with a dotted path to a member of the struct.
