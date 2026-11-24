---
title: on_console_chat
tags: [factorio-api, runtime, event]
---
# on_console_chat

Called when a message is sent to the in-game console, either by a player or through the server interface.

This event only fires for plain messages, not for any commands (including `/shout` or `/whisper`).

## Data

### player_index
- **Type:** [[uint32]]
- **Optional**
The player doing the chatting, if any.

### message
- **Type:** [[string]]
The chat message that was sent.

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
