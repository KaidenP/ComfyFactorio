---
title: on_player_toggled_alt_mode
tags: [factorio-api, runtime, event]
---
# on_player_toggled_alt_mode

Called when a player toggles alt mode, also known as "show entity info".

## Data

### player_index
- **Type:** [[uint32]]

### alt_mode
- **Type:** [[boolean]]
The new alt mode value. This value is a shortcut for accessing [[GameViewSettings#show_entity_info|GameViewSettings::show_entity_info]] on the player.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
