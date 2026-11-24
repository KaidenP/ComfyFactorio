---
title: CustomInputEvent
tags: [factorio-api, runtime, event]
---
# CustomInputEvent

Called when a [[CustomInputPrototype]] is activated.

## Data

### player_index
- **Type:** [[uint32]]
The player that activated the custom input.

### input_name
- **Type:** [[string]]
The prototype name of the custom input that was activated.

### cursor_position
- **Type:** [[MapPosition]]
The mouse cursor position when the custom input was activated.

### cursor_direction
- **Type:** [[defines.direction]]
- **Optional**
Cursor direction.

### cursor_display_location
- **Type:** [[GuiLocation]]
The mouse cursor display location when the custom input was activated.

### selected_prototype
- **Type:** [[SelectedPrototypeData]]
- **Optional**
Information about the prototype that is selected when the custom input is used. Needs to be enabled on the custom input's prototype. `nil` if none is selected.

### element
- **Type:** [[LuaGuiElement]]
- **Optional**
The GUI element under the cursor when the custom input was activated.

### in_gui
- **Type:** [[boolean]]
If the cursor was over any GUI when the custom input was activated.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.

## Examples

```
-- This will be raised when a custom input with the name "my-potato-control" and action "lua" is pressed
script.on_event("my-potato-control", function(event)
  game.print("Keyboard shortcut pressed on tick: " ..tostring(event.tick))
end)
```
