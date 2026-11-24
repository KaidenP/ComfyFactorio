---
title: GuiAnchor
tags: [factorio-api, runtime, concept]
---
# GuiAnchor

## Fields

### gui
- **Type:** [[defines.relative_gui_type]]

### position
- **Type:** [[defines.relative_gui_position]]

### type
- **Type:** [[string]]
- **Optional**
If provided, only anchors the GUI element when the opened things type matches the type.

### name
- **Type:** [[string]]
- **Optional**
If provided, only anchors the GUI element when the opened thing matches the name. `name` takes precedence over `names`.

### names
- **Type:** array<[[string]]>
- **Optional**
If provided, only anchors the GUI element when the opened thing matches one of the names. When reading an anchor, `names` is always populated.

### ghost_mode
- **Type:** `"both"` | `"only_ghosts"` | `"only_real"`
- **Optional**
Defaults to `"only_real"`.
