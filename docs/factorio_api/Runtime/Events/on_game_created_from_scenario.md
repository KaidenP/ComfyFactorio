---
title: on_game_created_from_scenario
tags: [factorio-api, runtime, event]
---
# on_game_created_from_scenario

Called when a game is created from a scenario. This is fired for every mod, even when the scenario's save data already includes it. In those cases however, [[LuaBootstrap#on_init|LuaBootstrap::on_init]] is not fired.

This event is not fired when the scenario is loaded via the map editor.

## Data

### name
- **Type:** [[defines.events]]
Identifier of the event.

### tick
- **Type:** [[MapTick]]
Tick the event was generated.
