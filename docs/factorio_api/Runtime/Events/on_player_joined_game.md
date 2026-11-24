---
title: on_player_joined_game
tags: [factorio-api, runtime, event]
---
# on_player_joined_game

Called after a player joins the game. This is not called when loading a save file in singleplayer, as the player doesn't actually leave the game, and the save is just on pause until they rejoin.

## Data

### player_index
- **Type:** [[uint32]]

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
