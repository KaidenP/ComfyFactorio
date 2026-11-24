---
title: ScriptedTechnologyTrigger
tags: [factorio-api, prototype, type]
---
# ScriptedTechnologyTrigger

Triggered only by calling [[LuaForce#script_trigger_research|LuaForce::script_trigger_research]]. Can be used to show custom scripted triggers in the technology GUI.

## Properties

### type
- **Type:** `"scripted"`

### trigger_description
- **Type:** [[LocalisedString (type)]]
- **Optional**

### icons
- **Type:** array<[[IconData]]>
- **Optional**
Can't be an empty array.

### icon
- **Type:** [[FileName]]
- **Optional**
Path to the icon file.

Only loaded if `icons` is not defined.

### icon_size
- **Type:** [[SpriteSizeType]]
- **Optional**
- **Default:** `64`
The size of the square icon, in pixels. E.g. `32` for a 32px by 32px icon. Must be larger than `0`.

Only loaded if `icons` is not defined.
